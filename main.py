from flask import Flask, render_template, request, flash
import funktionen
import plotly
import plotly.graph_objects as go

app = Flask("TimeTool")
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' # Wird für flash benötigt

kategorien_farben = {
    "Isolation": "#F5F6CE",
    "Wandtäferung": "#CEF6E3",
    "Fenster": "#CEECF5",
    "Möbelbau": "#F6CEF5",
    "Küche": "#F6CED8",
    "Sonstiges": "#F6D8CE"
}

@app.route('/', methods=['GET', 'POST'])
def speichern():
    if request.method == 'POST':  # Wenn User etwas im Formular (siehe index.html) eingibt
        datum = request.form['datum']  # Eingaben werden zu Variablen
        kategorie = request.form['kategorie']
        startzeit = request.form['startzeit']
        endzeit = request.form['endzeit']
        pause = request.form['pause']
        erfolgreich = funktionen.neue_eingabe_speichern(datum, kategorie, startzeit, endzeit, pause)  # Funktion gibt erfolgreich zurück
        if erfolgreich:   # erfolgreich ist True oder False
            flash('Ihre Eingabe wurde gespeichert.')
        else:
            flash('Ihre Eingabe konnte nicht gespeichert werden, da die Zeitsumme kleiner als 0 ist.')
    return render_template('index.html', kategorien=kategorien_farben.keys())


@app.route('/uebersicht')
def uebersicht():
    zeiterfassung = funktionen.erfasste_zeit_laden()
    return render_template('uebersicht.html',
                           zeiterfassung=zeiterfassung,
                           farben=kategorien_farben,
                           kategorien=kategorien_farben.keys())


@app.route('/grafik')
def grafik():
    labels, values = funktionen.zeiten_zusammenzaehlen()
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    div = plotly.io.to_html(fig, include_plotlyjs=True, full_html=False)
    return render_template('grafik.html', plotly_div=div)


@app.route('/loeschen')
@app.route('/loeschen/<key>')
def loeschen(key=False):  # WIESO HIER KEY FALSE???????????????????????????????????
    if key:
        zeiterfassung = funktionen.erfasste_zeit_laden()  # Die .json Einträge werden als Dict geladen
        del zeiterfassung[key]  # Der entsprechende Eintrag wird aus dem Dict gelöscht
        funktionen.zeiterfassung_abspeichern(zeiterfassung)  # Der Dict wird in .json abgespeichert
        return render_template('uebersicht.html', zeiterfassung=zeiterfassung, farben=kategorien_farben)
    else:
        return render_template('uebersicht.html')


@app.route('/aendern', methods=['GET', 'POST'])
@app.route('/aendern/<key>', methods=['GET', 'POST'])
def aendern(key=False):
    if key:
        if request.method == 'POST':  # Wenn User etwas in Formular (siehe aenderbare_uebersicht.html) eingibt
            zeiterfassung = funktionen.erfasste_zeit_laden()
            neue_kategorie = request.form['neue_kategorie']  # Eingaben werden zu Variablen
            neue_zeit = request.form['neue_zeit']
            zeiterfassung[key] = str(neue_kategorie), str(neue_zeit)  # Der Eintrag im Dictionary wird aktualisiert
            funktionen.zeiterfassung_abspeichern(zeiterfassung)
            return render_template('uebersicht.html', zeiterfassung=zeiterfassung, farben=kategorien_farben)
        else:  # Wenn Formular noch nicht ausgefüllt wurde, also request.method nicht gleich POST
            zeiterfassung = funktionen.erfasste_zeit_laden()
            aenderbare_kategorie = zeiterfassung[key]  # Die Werte zum angewählten Schlüssel werden zur Variablen anderbare_kategorie
            return render_template('aenderbare_uebersicht.html',
                                   zeiterfassung=zeiterfassung,
                                   aenderbare_kategorie=aenderbare_kategorie,  # Diese Variable wird an das .html Format weitergegeben
                                   farben=kategorien_farben,
                                   key = key,
                                   kategorien=kategorien_farben.keys())


if __name__ == "__main__":
    app.run(debug=True, port=5000)
