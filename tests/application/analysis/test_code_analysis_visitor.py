import ast

from examon_core.application.analysis.code_analysis_visitor import CodeAnalysisVisitor


class TestCodeAnalysisVisitor:
    def test_count(self, very_complex_code):
        tree = ast.parse(very_complex_code)
        m = CodeAnalysisVisitor()
        m.visit(tree)
        assert m.functions == {"__init__", "fun_a", "fun_b", "fun_c", "fun_d"}
        assert "print" in m.calls
        assert "range" in m.calls
        assert "dict" in m.calls
        assert "len" in m.calls
        assert m.modules == {"sys", "os"}
        keys = list(m.counts.keys())

        assert "Return" in keys
        assert "Delete" in keys
        assert "Expr" in keys
        assert "Name" in keys
        assert "Load" in keys
