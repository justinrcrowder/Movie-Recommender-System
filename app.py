from flask import Flask, render_template, request, redirect, url_for
import frontend

app = Flask(__name__)


@app.route('/')
def index():
    items = frontend.movies['title'].values
    return render_template('index.html', items=items)


@app.route('/selected', methods=['POST'])
def selected_item():
    selected = request.form['dropdown']
    return redirect(url_for('display_selection', selected=selected))


@app.route('/display', methods=['GET'])
def display_selection():
    title = request.args.get('selected')
    recommendations = frontend.recommend(title)
    return render_template('display.html', selected=request.args.get('selected'), recommendations=recommendations)


if __name__ == "__main__":
    app.run(debug=True)
