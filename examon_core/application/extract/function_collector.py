import ast

from examon_core.entities import Question


class FunctionCollector:
    def extract(self, source: str) -> list[Question]:
        tree = ast.parse(source)
        questions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                if self.__has_examon_decorator(node):
                    f = ast.unparse(node)
                    kwargs = self.__get_examon_decorator_kwargs(node)
                    tags = kwargs.get("tags")
                    choices = kwargs.get("choices")
                    hints = kwargs.get("hints")
                    tags = tags if isinstance(tags, list) else None
                    choices = choices if isinstance(choices, list) else None
                    hints = hints if isinstance(hints, list) else None
                    questions.append(
                        Question(
                            function_src=f,
                            tags=tags,
                            choices=choices,
                            hints=hints,
                        )
                    )
        return questions

    def __has_examon_decorator(self, node: ast.FunctionDef) -> bool:
        for decorator in node.decorator_list:
            if (isinstance(decorator, ast.Name) and decorator.id == "examon") or (
                isinstance(decorator, ast.Call)
                and getattr(decorator.func, "id", None) == "examon"
            ):
                return True
        return False

    def __get_examon_decorator_kwargs(self, node: ast.FunctionDef) -> dict[str, object]:
        for decorator in node.decorator_list:
            if (
                isinstance(decorator, ast.Call)
                and getattr(decorator.func, "id", None) == "examon"
            ):
                provided = {
                    str(kw.arg): ast.literal_eval(kw.value)
                    for kw in decorator.keywords
                    if kw.arg is not None
                }
                return provided
            elif isinstance(decorator, ast.Name) and decorator.id == "examon":
                return {}
        return {}
