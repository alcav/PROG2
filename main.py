from flask import Flask, render_template, request
import funktionen


app = Flask("TimeTool")


@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request.method == 'POST': # Wenn User etwas im Formular eingibt.
        datum = request.form['datum'] # Eingaben werden zu Variablen.
        aufgabe = request.form['aufgabe']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        funktionen.eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause) # Funktion wird ausgeführt.
    return render_template('index.html')


@app.route('/uebersicht')
def uebersicht():
    zeiterfassung = funktionen.erfasste_zeit_laden()
    return render_template('uebersicht.html', zeit = zeiterfassung)


@app.route('/grafiken')
def grafiken():
    return render_template('grafiken.html')


@app.route('/loeschen')
def loeschen():
    return render_template('loeschen.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
