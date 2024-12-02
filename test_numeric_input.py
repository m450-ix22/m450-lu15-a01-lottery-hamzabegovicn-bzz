from numeric_input import read_int, read_float


def test_numeric_input_read_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "15")
    assert read_int("Eingabe > ", 10, 20) == 15


def test_numeric_input_read_float(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "25.5")
    assert read_float("Eingabe > ", 10.0, 50.0) == 25.5
