# Dans le fichier real_estate_analysis/tests/test_exemple.py

def test_verif_addition():
    """Une fonction de test simple pour vérifier l'addition."""
    assert 1 + 1 == 2
    assert 2 + 3 == 5

def test_verif_chaine():
    """Une autre fonction de test pour vérifier la longueur d'une chaîne."""
    ma_chaine = "Pytest"
    assert len(ma_chaine) == 6