from flask import Flask, render_template, request
from analyzer.metrics import analyze_code
from ai_engine.suggestions import get_suggestion

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    analysis = suggestion = None
    code = ""
    if request.method == "POST":
        code = request.form["code"]
        analysis = analyze_code(code)
        suggestion = get_suggestion(code)
    return render_template("index.html", code=code, analysis=analysis, suggestion=suggestion)

if __name__ == "__main__":
    app.run(debug=True)
