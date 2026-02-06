from flask import Flask, render_template

app = Flask(__name__)

# The first page (SpongeBob)
@app.route('/')
def index():
    return render_template('index.html')

# The second page (Crying Ghost)
@app.route('/please')
def please():
    return render_template('please.html')

@app.route('/thanks')
def thanks():
    return render_template('thanks.html')

@app.route('/final')
def final():
    return render_template('final.html')

@app.route('/page5')
def page5():
    return render_template('page5.html')


if __name__ == '__main__':
    app.run(debug=True)