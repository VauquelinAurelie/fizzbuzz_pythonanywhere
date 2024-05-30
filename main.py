from bottle import default_app, route, template, request, error, post, debug, run


def calculate_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


def main():
    for number in range(1, 101):
        print(calculate_fizzbuzz(number))


# if __name__ == "__main__":
#     main()


@route('/')
def index():
    return template('fizzbuzz')


application = default_app()

# run(host='localhost', port=8080)
