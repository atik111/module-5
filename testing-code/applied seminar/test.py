
from calc import predict_species

def test_minimum():
    # Arrange
    sepal_length = 4.00
    sepal_width = 1.80
    petal_length = 0.80
    petal_width = 0.10
    expected_output = 'setosa'

    # Act
    actual_output = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert actual_output == expected_output


def test_maximum():
    # Arrange
    sepal_length = 8.00
    sepal_width = 4.50
    petal_length = 7.00
    petal_width = 2.70
    expected_output = 'virginica'

    # Act
    actual_output = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert actual_output == expected_output


def test_versicolor():
    # Arrange
    sepal_length = 6.00
    sepal_width = 3.00
    petal_length = 4.00
    petal_width = 1.00
    expected_output = 'versicolor'

    # Act
    actual_output = predict_species(sepal_length, sepal_width, petal_length, petal_width)

    # Assert
    assert actual_output == expected_output