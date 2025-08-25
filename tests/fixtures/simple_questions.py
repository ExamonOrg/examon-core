from examon_core.examon import examon


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
    return 2 + 1


@examon(
    choices=["Hello Bob", "Hello"],
)
def question2():
    name = "Sam"
    return f"Hello, {name}"


@examon(
    tags=["Python Data & Structure Basics", "Strings"],
    choices=["applebanana", "apple banana", "bananaapple"],
    hints=[
        "String concatenation joins two strings together.",
        "What happens when you use + with two strings?",
        "Try combining 'apple' and 'banana'.",
    ],
)
def question3():
    return "apple" + "banana"
