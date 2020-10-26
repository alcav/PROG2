import json


def eingabe_speichern(datum, aufgabe, startzeit, endzeit, pause):
    try:
        with open("zeiterfassung.json") as open_file:  # Wenn Datei "zeiterfassung.json" vorhanden, wird sie geöffnet.
            zeiterfassung = json.load(open_file)

    except FileNotFoundError:  # Wenn noch keine Datei "zeiterfassung.json" vorhanden, wird ein neues Dict erstellt.
        zeiterfassung = {}

    zeiterfassung[datum] = aufgabe, startzeit, endzeit, pause

    with open("zeiterfassung.json", "w") as open_file:  # Die Eingaben werden im Dict abgespeichert.
        json.dump(zeiterfassung, open_file)  # json.dump() function converts a Python object into a json string.


def erfasste_zeit_laden():

    try:
        with open("zeiterfassung.json") as open_file:
            zeiterfassung = json.load(open_file)
    except FileNotFoundError:
        zeiterfassung = {}

    return zeiterfassung