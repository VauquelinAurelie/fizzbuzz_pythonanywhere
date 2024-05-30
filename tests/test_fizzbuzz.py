from main import calculate_fizzbuzz


def test_fizzbuzz_multiple_three():
    actual = calculate_fizzbuzz(3)
    print(actual)
    expected = "Fizz"
    assert actual == expected


def test_fizzbuzz_multiple_five():
    actual = calculate_fizzbuzz(5)
    print(actual)
    expected = "Buzz"
    assert actual == expected


def test_fizzbuzz_multiple_three_and_five():
    actual = calculate_fizzbuzz(15)
    print(actual)
    expected = "FizzBuzz"
    assert actual == expected
