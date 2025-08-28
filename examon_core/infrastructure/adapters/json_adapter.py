import json

from dataclasses_serialization.json import JSONSerializer  # type: ignore

from examon_core.entities import Question


class JSONAdapter:
    def convert(self, filename: str, questions: list[Question]) -> None:
        data = JSONSerializer.serialize(questions)
        with open(filename, "w") as f:
            json.dump(data, f)
