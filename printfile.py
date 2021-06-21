def ask_user(msg: str = "this is the default prompt. No prompt has been written for this request"):
    user_input = int(input(msg + "\n"))
    return user_input

def step(a):
    return a
def output(x, z):
    o = x*z
    print(o)

def myfunction():
    x = ask_user(msg = "Give me the first number")
    y = ask_user(msg = "Give me the second number")
    a = ask_user(msg = "Give me a step")
    z = ask_user()
    if x<y or x>y:
        output(x,z)
        if x < y:
            while x < y:
                x += step(a)
                output(x,z)


        elif x > y:
            while x-step(a) > y:
                x -= step(a)

                output(x,z)
    elif x == y:
        print(x*y)


if __name__ == "__main__":
    myfunction()


