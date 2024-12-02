from menu import select_menu


def test_menu_selection(monkeypatch):
    inputs = iter(['A'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    selection = select_menu()
    assert selection == 'A'
