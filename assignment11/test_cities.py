from city_functions import city_str

def test_city_country():
    result = city_str("Santiago", "Chile")
    assert result == "Santiago, Chile"

def test_city_country_population():
    result = city_str("Santiago", "Chile", 5000000)
    assert result == "Santiago, Chile - population 5000000"
