import json
from datetime import datetime


def eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause):
    try:
        with open("zeiterfassung.json") as open_file:  # Wenn die Datei "zeiterfassung.json" vorhanden ist, wird sie geöffnet.
            zeiterfassung = json.load(open_file) # json.load wandelt den Text in der JSON-Struktur in Python-Dictionarys bzw. Listen um.

    except FileNotFoundError:
        zeiterfassung = {}  # Wenn noch keine Datei "zeiterfassung.json" vorhanden ist, wird ein leeres Dict erstellt.



    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    datum = datum + ", " + current_time

    startzeit_obj = datetime.strptime(startzeit, '%H:%M')
    endzeit_obj = datetime.strptime(endzeit, '%H:%M')
    pause_obj = datetime.strptime(pause, '%M')

    gesamtzeit = endzeit_obj - startzeit_obj
    gesamtzeit = gesamtzeit - pause_obj

    zeiterfassung[datum] = aufgabe, gesamtzeit

    with open("zeiterfassung.json", "w") as open_file:  # "zeiterfassung.json" wird im Schreibmodus geöffnet. Die Eingaben werden im Dict abgespeichert.
        json.dump(zeiterfassung, open_file)  # json.dump() wandelt Python-Dictionarys bzw. Listen in Text in der JSON-Struktur um.

    # Die .json Datei wird geöffnet (read) oder neu erstellt und danach neu abgespeichert (write).
    # Quelle: https://strftime.org/


def erfasste_zeit_laden():

    try:
        with open("zeiterfassung.json") as open_file:
            zeiterfassung = json.load(open_file)
    except FileNotFoundError:
        zeiterfassung = {}

    return zeiterfassung
