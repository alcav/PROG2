from flask import Flask, render_template, request, flash
import funktionen
import plotly.express as px
import plotly
import plotly.graph_objects as go


app = Flask("TimeTool")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request.method == 'POST':  # Wenn User etwas im Formular eingibt.
        datum = request.form['datum']  # Eingaben werden zu Variablen.
        kategorie = request.form['kategorie']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        erfolgreich = funktionen.neue_eingabe_speichern(datum, kategorie, startzeit, endzeit, pause)  # Funktion gibt erfolgreich zurück
        if erfolgreich:   # erfolgreich ist True oder False
            flash('Ihre Eingabe wurde gespeichert.')
        else:
            flash('Ihre Eingabe konnte nicht gespeichert werden, da die Zeitsumme kleiner als 0 ist.')
    return render_template('index.html')


@app.route('/uebersicht')
def uebersicht():
    farben = {"Isolation": "color:red", "Sonstiges": "color:blue"}
    zeiterfassung = funktionen.erfasste_zeit_laden()
    return render_template('uebersicht.html', zeiterfassung=zeiterfassung, farben_dict=farben)


@app.route('/grafiken')
def grafiken():
    labels, values = funktionen.zeiten_zusammenzaehlen()
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)
    return render_template('grafiken.html', plotly_div=div)


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


@app.route('/aendern')
@app.route('/aendern/<key>')
def aendern(key=False):
    if key:
        zeiterfassung = funktionen.erfasste_zeit_laden()
        eintrag_aendern = zeiterfassung[key]
        key = key
        return render_template('aenderbare_uebersicht.html', zeiterfassung=zeiterfassung, eintrag_aendern=eintrag_aendern, key = key)
    else:
        return render_template('uebersicht.html')


@app.route('/speichern', methods=['GET', 'POST'])
@app.route('/speichern/<key>', methods=['GET', 'POST'])
def neu_speichern(key=False):
    if key:
        if request.method == 'POST':
            zeiterfassung = funktionen.erfasste_zeit_laden()
            neue_kategorie = request.form['neue_kategorie']
            neue_zeit = request.form['neue_zeit']
            zeiterfassung[key] = str(neue_kategorie), str(neue_zeit)
            funktionen.zeiterfassung_abspeichern(zeiterfassung)
            return render_template('uebersicht.html')
    else:
        return render_template('uebersicht.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
