# Die Klasse Knoten werden wir in dieser Aufgabe benutzen, aber nicht verändern.
# Es gilt weiterhin: Ein Knoten speichert einen Inhalt und eine Referenz auf den nächsten Knoten.

from __future__ import annotations   # brauchen wir, weil wir in der Klasse Knoten den Typ Knoten verwenden
from typing import Any

class Knoten:
    def __init__(self, inhalt):
        """ Konstruktor für die Klasse Knoten: speichert den Inhalt und legt
        eine Referenz auf den nächsten Knoten an. """
        self.inhalt: Any = inhalt   # Any = inhalt kann beliebiger Datentyp sein
        self.naechster: Knoten|None = None    # Typ-Annotation: naechster ist ein Knoten oder None

    def __str__(self):
        return str(self.inhalt)
    

class VerketteteListe:
    def __init__(self):
        self.erster: Knoten|None = None   # Der erste Knoten in der Liste (Listenkopf)    

    def __str__(self) -> str:
        """ Gibt die Liste als Zeichenkette, getrennt durch Pfeile, zurück. """
        inhalte = []
        knoten = self.erster
        while knoten is not None:
            inhalte.append(knoten.inhalt)
            knoten = knoten.naechster
        return " -> ".join(inhalte)

    def einfuegen_vorne(self, pInhalt):
        """Fügt einen neuen Knoten mit pInhalt am Anfang der Liste ein."""
        neu = Knoten(pInhalt)   # "Verpacke" den Inhalt in einen Knoten
        neu.naechster = self.erster  # Nachfolger des neuen Knotens ist der bisherige Listenkopf
        self.erster = neu  # Der neue Knoten ist ab jetzt der Listenkopf

   # AUFGABE: Implementiere die folgenden Methoden für die Klasse VerketteteListe:
    
    def ist_leer(self) -> bool:
        """gibt True zurück, wenn die Liste leer ist, sonst False"""
        knoten = self.erster
        if knoten == None:
            return True
        else:
            return False
        ...  # Hier Lösung ergänzen

    def anzahl_elemente(self) -> int:
        """ Gibt die Anzahl der Elemente in der Liste zurück. """
        knoten = self.erster 
        Count = 0 
        while knoten is not None: 
            Count += 1 
            Knoten = knoten.naechster 
        return Count
        ...  # Hier Lösung ergänzen
    
    def gib_inhalt(self, index: int) -> Any:
        """ Gibt den Inhalt des Knotens an der Stelle index zurück. """
        # ACHTUNG: Gib nicht den Knoten selbst zurück, sondern nur den Inhalt!
        # D.h. dein Code sollte sowas enthalten wie: return aktuell.inhalt
        knoten = self.erster
        naechster = self.erster
        count = 0
        while index != count:
            count +=1
            knoten = naechster
            naechster = naechster.naechster
        return knoten.inhalt
        ...  # Hier Lösung ergänzen
    
    def ersetzen(self, index, neuer_inhalt: Any) -> None:
        """ Ersetzt den Inhalt des Knotens an der Stelle index durch neuer_inhalt. """
        neu = Knoten(neuer_inhalt)
        knoten = self.erster
        naechster = self.erster
        count = 0
        while index != count:
            count +=1
            knoten = naechster
            naechster = naechster.naechster
        neu.naechster = naechster.naechster
        knoten.naechster = neu
        ...  # Hier Lösung ergänzen



# Mit den folgenden Tests kannst du deine Implementierung überprüfen.
# Führe einfach diese Zelle aus, um die Tests zu starten.

test = TestsVerketteteListe(VerketteteListe)
reihenfolge = ["ist_leer", "anzahl_elemente", "gib_inhalt", "ersetzen"]
test.fuehre_tests_aus(reihenfolge)