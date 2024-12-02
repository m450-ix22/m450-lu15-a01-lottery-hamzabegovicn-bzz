from authenticate import login
from person import Person


def test_authenticate_login(monkeypatch):
    people = [Person("TestUser", "password123", 10.0)]

    def mock_input(prompt):
        return "password123"

    monkeypatch.setattr("builtins.input", mock_input)
    monkeypatch.setattr("authenticate.load_people", lambda: people)
    user = login()
    assert user.givenname == "TestUser"
