from examon_core.application.execute.unrestricted_driver import (
    UnrestrictedDriver,
)


def execute(driver, code: str) -> list[str]:
    try:
        driver.setup()
        return driver.execute(code)
    finally:
        driver.teardown()


class TestUnrestrictedDriver:
    def test_print_logs(self, print_logs_code):
        assert execute(UnrestrictedDriver(), print_logs_code) == [
            "hello",
            "hello2",
            "3",
        ]

    def test_complex_code(self, complex_print_logs_code):
        assert execute(UnrestrictedDriver(), complex_print_logs_code) == [
            "1",
            "3",
            "6",
            "6",
        ]

    def test_print_logs_with_params(self, print_logs_with_params_code):
        assert execute(UnrestrictedDriver(), print_logs_with_params_code) == ["5", "39"]

    def test_unknown_error(self, source_code):
        execute(UnrestrictedDriver(), source_code)

    def test_functools_(self, lru_cache_source_code):
        execute(UnrestrictedDriver(), lru_cache_source_code)

    def test_with_block(self, source_code_with_block):
        execute(UnrestrictedDriver(), source_code_with_block)

    def test_unpack(self, unpack_source_code):
        execute(UnrestrictedDriver(), unpack_source_code)

    def test_unpack_2(self, splat_source_code):
        execute(UnrestrictedDriver(), splat_source_code)

    def test_class(self, classes_source_code):
        execute(UnrestrictedDriver(), classes_source_code)
