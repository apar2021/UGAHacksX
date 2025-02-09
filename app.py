from flask import Flask, jsonify, request,render_template
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')
@app.route("/about")
def about():
    return render_template('about.html')
@app.route("/artist-register")
def artist-register():
    return render_template('artist-register.html')
@app.route("/band-register")
def band-register():
    return render_template('band-register.html')
if __name__ == "__main__":
    app.run(debug=True)
