from examon_core.examon import examon


@examon(
    choices=[1, 2, 3],
    tags=["anything"],
    hints=["what does this return?"],
    internal_id="internal_id",
    repository="examon_core_fixtures",
    version=1,
)
def question_1():
    print("This will get recorded")
    return 1
