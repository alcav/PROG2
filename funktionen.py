import json


def eingabe_speichern(datum, aufgabe, anfangszeit, endzeit, pause):
    try:
        with open("zeiterfassung.txt", "r") as open_file:
            zeiterfassung = json.load(open_file)

    except FileNotFoundError:
        zeiterfassung = []

    datum = ('aufgabe', 'anfangszeit', 'endzeit', 'pause')  # Das ist ein Tuple = eine unveränderbare Liste.
