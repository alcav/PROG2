from flask import Flask, render_template, request
import json
import funktionen


app = Flask("TimeTool")


@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request.method == 'POST': #Wenn User etwas im Formular eingibt.
        datum = request.form['datum'] #Eingaben werden zu Variablen.
        aufgabe = request.form['aufgabe']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        funktionen.eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause) #Funktion wird ausgeführt.
    return render_template('index.html')


@app.route('/uebersicht')
def auflisten():
    erfasste_zeit = funktionen.erfasste_zeit_laden()

    zeiterfassung_liste = ""
    for key, value in erfasste_zeit.items():
        zeile = str(key) + ": " + str(value) + "<br>"
        zeiterfassung_liste += zeile

    return zeiterfassung_liste


# def uebersicht():
    # return render_template('uebersicht.html')


@app.route('/grafiken')
def grafiken():
    return render_template('grafiken.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
