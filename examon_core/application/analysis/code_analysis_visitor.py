import ast
from collections import defaultdict
from types import MethodType
from typing import Any, Callable, DefaultDict, Set

from examon_core.application.analysis.visit_methods import visit_methods


class CodeAnalysisVisitor(ast.NodeVisitor):
    def __init__(self) -> None:
        self.functions: Set[str] = set()
        self.calls: Set[str] = set()
        self.modules: Set[str] = set()
        self.counts: DefaultDict[str, int] = defaultdict(int)
        for visit_method in visit_methods:
            self.counts[visit_method] = 0
            env_setter: Callable[[Any, ast.AST], None] = self.make_visit(visit_method)
            method = MethodType(env_setter, self)
            setattr(self, f"visit_{visit_method}", method)

    def record(self, node: ast.AST) -> None:
        self.counts[type(node).__name__] += 1

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self.functions.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node: ast.Call) -> None:
        if isinstance(node.func, ast.Name):
            self.calls.add(node.func.id)
        elif isinstance(node.func, ast.Attribute):
            self.calls.add(node.func.attr)
        self.generic_visit(node)

    def visit_Import(self, node: ast.Import) -> None:
        for name in node.names:
            self.modules.add(name.name.split(".")[0])

    def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
        if node.module is not None and node.level == 0:
            self.modules.add(node.module.split(".")[0])

    @staticmethod
    def make_visit(_: str) -> Callable[[Any, ast.AST], None]:
        def visit(self: "CodeAnalysisVisitor", node: ast.AST) -> None:
            self.record(node)
            self.generic_visit(node)

        return visit
