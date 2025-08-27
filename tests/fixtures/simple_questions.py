from examon_core.examon import examon

@examon(
    choices=["Hello Bob", "Hello"],
)
def question2():
    name = "Michael"
    return f"Hello, {name}"


@examon(
    tags=["Python Data & Structure Basics", "Numbers"],
    choices=["2", "3", "4"],
    hints=[
        "Addition combines two numbers into a larger one.",
        "What is 2 plus 1?",
        "Try counting up from 2.",
    ],
)
def question1():
    return 2 + 1 + 2 + 9


@examon(
    tags=["Python Data & Structure Basics", "Strings"],
    choices=["fizz", "buzzfizz", "12345"],
    hints=["5 mod 2 equals 1"],
)
def question3():
    result = ""
    for n in [1, 2, 3, 4, 5]:
        word = "fizz" if n % 2 == 0 else "buzz"
        print(word)
        result += word
    return result
