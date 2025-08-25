import click

from examon_core.application.default_factory import default_instance
from examon_core.application.extract.function_collector import FunctionCollector
from examon_core.infrastructure.adapters.json_adapter import JSONAdapter
from examon_core.infrastructure.collection.file_collector import FileCollector


@click.command()
@click.argument("paths", nargs=-1, type=click.Path(exists=True))
@click.option("--file_name", default="output.json", help="Output file name")
def main(paths: tuple[str, ...], file_name: str) -> None:
    files = FileCollector().collect_files(list(paths))
    results = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            examon_functions = [
                default_instance().decorate(question)
                for question in FunctionCollector().extract(f.read())
            ]
            if examon_functions:
                results.extend(examon_functions)

    JSONAdapter().convert(file_name, results)
    click.echo(f"File generated: {file_name}")


if __name__ == "__main__":
    main()
