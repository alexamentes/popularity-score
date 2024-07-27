import pytest
import statistics
from project import get_artist_dict
from project import sorted_artists_list
from project import get_statistics

def test_get_artist_dict():
    assert get_artist_dict("AC/DC", 83)=={"name":"AC/DC", "popularity":83}
    assert get_artist_dict("Metallica", 82)=={"name":"Metallica", "popularity":82}

def test_get_artist_dict_integer():
    with pytest.raises(ValueError):
        get_artist_dict("AC/DC", "83")
        get_artist_dict("artist", "popularity")

def test_sorted_artists_list():
    assert sorted_artists_list([{"name":"Metallica", "popularity":82},
                                {"name":"AC/DC", "popularity":83}])==[{"name":"AC/DC", "popularity":83},
                                                                      {"name":"Metallica", "popularity":82}]
    assert sorted_artists_list([{"name":"Metallica", "popularity":82},
                                {"name":"AC/DC", "popularity":83},
                                {"name":"Taylor Swift", "popularity":100},
                                {"name":"The Doors", "popularity":73}])==[{"name":"Taylor Swift", "popularity":100},
                                                                          {"name":"AC/DC", "popularity":83},
                                                                        {"name":"Metallica", "popularity":82},
                                                                        {"name":"The Doors", "popularity":73}]
    assert sorted_artists_list([{"n":"k", "popularity":1},
                                {"n":"p","popularity":4},
                                {"n":"l","popularity":2}])==[{"n":"p","popularity":4},
                                                             {"n":"l","popularity":2},
                                                               {"n":"k", "popularity":1}]
    assert sorted_artists_list([{"n":"k", "popularity":"a"},
                                {"n":"p","popularity":"f"},
                                {"n":"l","popularity":"d"}])==[{"n":"p","popularity":"f"},
                                                             {"n":"l","popularity":"d"},
                                                               {"n":"k", "popularity":"a"}]


def test_sorted_artists_list_exception():
    with pytest.raises(KeyError):
        sorted_artists_list([{"n":"k", "p":1},
                                {"n":"h","p":4},
                                {"n":"l","p":2}])

def test_get_statistics():
    assert get_statistics([1, 2, 3])=="Mean: 2.0, median: 2, mode: no unique mode"
    assert get_statistics([6, 2, 2])=="Mean: 3.3, median: 2, mode: 2"
    assert get_statistics([6, 2, 2, 6])=="Mean: 4.0, median: 4.0, mode: no unique mode"

def test_get_statistics_exception():
    with pytest.raises(TypeError):
        get_statistics("it is not a list of integers")
