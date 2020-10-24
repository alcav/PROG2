from flask import Flask, render_template, request
import json
import funktionen


app = Flask("TimeTool")


@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request_method == 'POST':
        datum = request.form['datum']
        aufgabe = request.form['aufgabe']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        funktionen.eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause)
    return render_template('index.html')

# Hier wird eine Funktion ausgeführt, die in den Funktionen definiert wird.........
# Damit sollen die Einträge als dict in json abgespeichert werden können .........


@app.route('/uebersicht')
def uebersicht():
    return render_template('uebersicht.html')


@app.route('/grafiken')
def grafiken():
    return render_template('grafiken.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
