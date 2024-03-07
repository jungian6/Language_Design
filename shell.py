import main

while True:
    text = input("calc> ")
    result, error = main.run('<stdin>', text)

    if error: print(error.as_string())
    elif result: print(repr(result))