import os


class FileCollector:
    def __init__(self, file_ext: str = ".py"):
        self.file_ext = file_ext

    def collect_files(self, paths: list[str]) -> list[str]:
        py_files = []
        for path in paths:
            if os.path.isfile(path) and path.endswith(self.file_ext):
                py_files.append(path)
            elif os.path.isdir(path):
                for root, _, files in os.walk(path):
                    for file in files:
                        if file.endswith(self.file_ext):
                            py_files.append(os.path.join(root, file))
        return py_files
