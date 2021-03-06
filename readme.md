# Projektidee

## Ausgangslage
Mein Freund und ich bauen einen Kastenwagen zu einem Camper um. Um die Übersicht über die geleisteten Arbeitsstunden zu behalten, wurde dieses TimeTool von mir entwickelt.

## Funktion
Das TimeTool soll es erlauben die geleisteten Arbeitsstunden zu erfassen. Es soll schlussendlich eine Übersicht angezeigt werden, die alle bereits erfassten Arbeitzeiten darstellt. Die Übersicht soll das Datum, die Art der Arbeit und die Arbeitszeit beinhalten. Des Weiteren soll es auch möglich sein, bereits erfasste Arbeitsstunden wieder zu löschen oder anzupassen. Schlussendlich sollen die erfassten Daten grafisch dargestellt werden können.

## Workflow
Im Register Zeiterfassung können die geleisteten Arbeitsstunden erfasst werden. Bei der Erfassung wird das Datum, die Startzeit, die Endzeit sowie die Pause in Minuten eingetragen. Zudem wird mittels Checkbox ausgewählt, woran gearbeitet wurde. Die Auswahloptionen sind Isolation, Wandtäferung, Fenster, Möbelbau, Küche oder Sonstiges. Mit Klick auf dem Button "Hinzufügen" werden die Eingaben gespeichert und es wird eine entsprechende Bestätigung ausgegeben. Die Eingabe wird nicht gespeichert, wenn die Zeitsumme kleiner als 0 ist. In diesem Fall wird eine entsprechende Meldung ausgegeben. Im Register Übersicht werden sämtliche bereits erfassten Daten ausgegeben und es ist möglich, einzelne Arbeitsstunden zu löschen oder anzupassen. Im Register Grafik können die erfassten Daten grafisch ausgegeben werden.

## Funktionsbeschrieb

### Startseite (Zeiterfassung)
- Das Formular soll mittels Datum, Startzeit, Endzeit, Pause in Minuten und Auswahl einer Aufgabe ausgefüllt werden können. Bei den Aufgaben ist "Sonstiges" bereits vorgewählt. Es soll pro Zeiterfassung nur eine Aufgabe gewählt werden können.
- Falls ein Feld nicht ausgefüllt wird, soll beim Klicken auf den Button "Hinzufügen" eine Meldung erscheinen, die den Nutzer dazu auffordert, dieses Feld auszufüllen.
- Wenn alle Daten korrekt erfasst wurden und auf dem Button "Hinzufügen" geklickt wurde, soll eine Bestätigung erscheinen, dass der Eintrag gespeichert wurde. Danach soll der User auf die Seite Zeiterfassung verbleiben. Das Formular soll wieder leer sein, sodass der Nutzer eine neue Zeiterfassung machen kann. 
- Wenn die Zeitsumme kleiner als 0 ist, wird die Eingabe nicht gespeichert und es wird eine entsprechende Meldung ausgegeben. Damit soll verhindert werden, dass der Nutzer Minuszeiten erfasst. Es ist z. Bsp. nicht möglich, um 13:00 Uhr mit einer Arbeit anzufangen und am selben Datum um 11:00 Uhr damit fertig zu sein.
- Durch das Klicken auf den Button "TimeTool" soll der User auf die Seite Zeiterfassung verbleiben.
- Durch das Klicken auf den Button "Zeiterfassung" soll der User auf die Seite Zeiterfassung verbleiben.
- Durch das Klicken auf den Button "Übersicht" soll der User auf die Seite Übersicht weitergeleitet werden. 
- Durch das Klicken auf den Button "Grafik" soll der User auf die Seite Grafik weitergeleitet werden.

### Seite Übersicht
- Die Übersicht soll alle bereits erfassten Daten darstellen. Für jede Zeiterfassung wird das Datum, die Erfassungzeit, die Aufgabe und die Arbeitszeit angezeigt. Die Arbeitszeit soll die totale Arbeitszeit pro Zeiterfassung sein, d.h. Endzeit abzgl. Anfangszeit abzgl. Pause. Die Arbeitszeit soll in Stunden und Minuten dargestellt werden.
- Der Nutzer soll die Möglichkeit haben, die erfassten Daten nach Kategorien zu filtern. Wenn er mit der Filterfunktion eine Kategorie auswählt, soll nur die erfasste Arbeitszeit in dieser Kategorie angezeigt werden.
- ZEITEN ZUSAMMENZAEHLEN
- Falls noch keine Zeiten erfasst wurden, erscheint eine entsprechende Meldung mit der Aufforderung, die Zeit auf der Seite Zeiterfassung einzugeben.
- Es soll es dem User möglich sein, durch das Klicken auf den Button "Löschen" bereits erfasste Daten zu löschen und durch das Klicken auf den Button "Ändern" bereits erfasste Daten zu ändern. Sowohl die Kategorie als auch die Gesamtzeit können geändert werden.
- Durch das Klicken auf den Button "TimeTool" soll der User auf die Seite Zeiterfassung weitergeleitet werden.
- Durch das Klicken auf den Button "Zeiterfassung" soll der User auf die Seite Zeiterfassung weitergeleitet werden.
- Durch das Klicken auf den Button "Übersicht" soll der User auf die Seite Übersicht verbleiben. 
- Durch das Klicken auf den Button "Grafik" soll der User auf die Seite Grafik weitergeleitet werden.

### Seite Grafik
- Mittels eines Kuchendiagramms kann eingesehen werden, wie viel % man woran gearbeitet hat. Alle sechs Kategorien Isolation, Wandtäferung, Fenster, Möbelbau, Küche und Sonstiges sind im Diagramm enthalten.
- Durch das Klicken auf den Button "TimeTool" soll der User auf die Seite Zeiterfassung weitergeleitet werden.
- Durch das Klicken auf den Button "Zeiterfassung" soll der User auf die Seite Zeiterfassung weitergeleitet werden.
- Durch das Klicken auf den Button "Übersicht" soll der User auf die Seite Übersicht weitergeleitet werden. 
- Durch das Klicken auf den Button "Grafik" soll der User auf die Seite Grafik verbleiben.


## Ablaufdiagramm
![alt text](https://github.com/alcav/PROG2/blob/master/Ablaufdiagramm_v5.jpg)