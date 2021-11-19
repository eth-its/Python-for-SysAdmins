def say_hello_upper(*words):
    print("Hello:", *[word.upper() for word in words])