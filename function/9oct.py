def f():
    def h():
        print("Hello Your inside h function")
        f()
    h()
    print("Outside h function.")
f()