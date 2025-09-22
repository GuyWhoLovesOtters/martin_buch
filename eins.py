def finde_maximum(a: int, b: int, c: int) -> int:
    # Aufgabe: Schreibe eine Funktion, die den größten Wert von a, b und c zurückgibt.
    if (a > b) & (a > c):
      return a
    elif b > c:
      return b
    else:
      return c


# Mit den folgenden Tests kannst du überprüfen, ob deine Funktion richtig funktioniert
print("Beginne Tests...")
assert finde_maximum(1, 2, 3) == 3, "Test 1 fehlgeschlagen"
assert finde_maximum(3, 2, 1) == 3, "Test 2 fehlgeschlagen"
assert finde_maximum(1, 3, 2) == 3, "Test 3 fehlgeschlagen"
assert finde_maximum(1, 1, 1) == 1, "Test 4 fehlgeschlagen"
assert finde_maximum(2, 1, 1) == 2, "Test 5 fehlgeschlagen"
assert finde_maximum(-3, -2, -5) == -2, "Test 6 fehlgeschlagen"
print("Super! Alle Tests bestanden.")