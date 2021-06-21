def ask_user_for_integer(msg: str = "this is the default prompt. No prompt has been written for this request"):
    user_input_int = int(input(msg + "\n"))
    return user_input_int

def ask_user_for_string(msg: str = "this is the default prompt. No prompt has been written for this request"):
    user_input_str = (input(msg + "\n"))
    return user_input_str

def myfunction():
    f = open("Numberfile", "w")
    x = ask_user_for_integer(msg = "Give me the first number")
    y = ask_user_for_integer(msg = "Give me the second number")
    b = ask_user_for_string(msg = "Tell me whether you want the numbers ascending or descending. Write ascending or descending")
    if b == "ascending":
        if x < y:
            print(x)
            f.write(str(x))
            f.write(str("\n"))
        else:
            print(y)
            f.write(str(y))
            f.write(str("\n"))
        while x < y:
            x += 1
            print(x)
            f.write(str(x))
            f.write(str("\n"))
        while y < x:
            y += 1
            print(y)
            f.write(str(y))
            f.write(str("\n"))
    elif b == "descending":
        if x < y:
            print(y)
            f.write(str(y))
            f.write(str("\n"))
        else:
            print(x)
            f.write(str(x))
            f.write(str("\n"))
        while x < y:
            y -= 1
            print(y)
            f.write(str(y))
            f.write(str("\n"))
        while y < x:
            x -= 1
            print(x)
            f.write(str(x))
            f.write(str("\n"))




if __name__ == "__main__":
    myfunction()
# What is up buddy
