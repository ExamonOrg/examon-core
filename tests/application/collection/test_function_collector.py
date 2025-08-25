import os

from examon_core.application.extract.function_collector import (
    FunctionCollector,
)


def get_fixture(filename):
    path = os.path.join(os.path.dirname(__file__), f"../../fixtures/{filename}")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


class TestFunctionCollector:
    def test_finds_all_questions(self):
        result = FunctionCollector().extract(get_fixture("simple_questions.py"))

        assert len(result) == 3

    def test_builds_question(self):
        result = FunctionCollector().extract(get_fixture("simple_question.py"))

        assert len(result) == 1
        assert (
            result[0].function_src
            == "@examon(choices=[1, 2, 3], tags=['anything'], hints=['what does this return?'], internal_id='internal_id', repository='examon_core_fixtures', version=1)\ndef question_1():\n    print('This will get recorded')\n    return 1"
        )
        assert result[0].tags == ["anything"]
        assert result[0].hints == ["what does this return?"]
