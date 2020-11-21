from flask import Flask, render_template, request, flash
import funktionen

app = Flask("TimeTool")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request.method == 'POST':  # Wenn User etwas im Formular eingibt.
        datum = request.form['datum']  # Eingaben werden zu Variablen.
        aufgabe = request.form['aufgabe']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        funktionen.neue_eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause)
        flash('Ihre Eingabe wurde gespeichert.')
    return render_template('index.html')


@app.route('/uebersicht')
def uebersicht():
    zeiterfassung = funktionen.erfasste_zeit_laden()
    return render_template('uebersicht.html', zeiterfassung=zeiterfassung)


@app.route('/grafiken')
def grafiken():
    zeiten = funktionen.zeiten_zusammenzaehlen()
    return render_template('grafiken.html')


@app.route('/loeschen')
@app.route('/loeschen/<key>')
def loeschen(key=False):
    if key:
        zeiterfassung = funktionen.erfasste_zeit_laden()
        del zeiterfassung[key]
        funktionen.zeiterfassung_abspeichern(zeiterfassung)
        return render_template('uebersicht.html', zeiterfassung=zeiterfassung)
    else:
        return render_template('uebersicht.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
