from flask import Flask, render_template, request
import json

app = Flask("TimeTool")


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        return 'hello'
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

