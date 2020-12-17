from day16_1 import Field, is_valid


def test_Field():
    f1 = Field("departure time: 29-483 or 491-963")
    assert f1._name == "departure time"
    assert f1._range1 == (29, 483)
    assert f1._range2 == (491, 963)

    assert f1.is_valid(29)
    assert f1.is_valid(483)
    assert f1.is_valid(491)
    assert f1.is_valid(963)
    assert not f1.is_valid(484)
    assert not f1.is_valid(0)
    assert not f1.is_valid(1000)


def test_is_valid():
    fields = []
    fields.append(Field("class: 1-3 or 5-7"))
    fields.append(Field("row: 6-11 or 33-44"))
    fields.append(Field("seat: 13-40 or 45-50"))

    assert is_valid(7, fields)
