from flask import Flask, render_template, request
import json
import funktionen    #noch nicht genutzt.........


app = Flask("TimeTool")


@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('index.html')
# Hier kommt eine Funktion, die in den Funktionen definiert wird.........
# Damit sollen die Einträge als dict in json abgespeichert werden können .........


@app.route('/uebersicht')
def uebersicht():
    return render_template('uebersicht.html')


@app.route('/grafiken')
def grafiken():
    return render_template('grafiken.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)

