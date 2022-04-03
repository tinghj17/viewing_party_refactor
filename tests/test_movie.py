import pytest
from viewing_party.movie import Movie

# Arrange
m_title = "Mulan"
genre = "Documentary"
rating = 8
host = "Disney"

# Act 
m1 = Movie(m_title, genre, rating, host)

def test_attributes():
    # Assert
    assert m1.title == "Mulan"

def test_change_rating():
    # Arrange
    new_rating = 10

    assert m1.rating == 8

    # Act
    # m2 = Movie("Up", "Cartoon", 7, "Disney")
    m1.update_rating(new_rating)

    # Assert
    assert m1.rating == 10
