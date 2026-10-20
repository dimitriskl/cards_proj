from cards import Card
import pytest
import cards

#helpers
def assert_identical(c1: Card, c2: Card):
     __tracebackhide__ = True
     assert c1 == c2
     if c1.id != c2.id:
          pytest.fail(f"id's don't match. {c1.id} != {c2.id}")

#tests
def test_field_access():
    c = Card("something", "brian", "todo", 123)
    assert c.summary == "something"
    assert c.owner == "brian"
    assert c.state == "todo"
    assert c.id == 123

def test_defaults():
    c = Card()
    assert c.summary is None
    assert c.owner is None
    assert c.state == "todo"
    assert c.id is None

def test_equality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("something", "brian", "todo", 123)
    assert c1 == c2

def test_inequality():
    c1 = Card("something", "brian", "todo", 123)
    c2 = Card("completly different", "okken", 123)
    assert c1 != c2

def test_from_dict():
    c1 = Card("something", "brian", "todo", 123)
    c2_dict = {
        "summary": "something",
        "owner" : "brian",
        "state" : "todo",
        "id" : 123
    }
    c2 = Card.from_dict(c2_dict)
    assert c1 == c2

def test_to_dict():
        #GIVEN a Card object with known content
        c1 = Card("something", "brian", "todo", 123)

        #WHEN we call to_dict() on the object 
        c2 = c1.to_dict()

        #THEN the result will be a dictionary with known content
        c2_expected = {
            "summary" : "something",
            "owner" : "brian",
            "state" : "todo",
            "id" : 123
        }
        assert c2 == c2_expected
    
def test_identical():
     c1 = Card("foo", id=123)
     c2 = Card("foo", id=123)
     assert_identical(c1, c2)

def test_no_path_raises():
     with pytest.raises(TypeError):
        cards.CardsDB()

def test_raises_with_info():
     match_regex = "missing 1 .* positional argument"
     with pytest.raises(TypeError, match=match_regex):
          cards.CardsDB()

def test_raises_with_info_alt():
    with pytest.raises(TypeError) as exc_info:
          cards.CardsDB()
    expected = "missing 1 required positional argument"
    assert expected in str(exc_info.value)