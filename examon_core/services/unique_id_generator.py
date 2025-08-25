import hashlib

from examon_core.protocols.unique_id_generation_protocol import (
    UniqueIdGenerationProtocol,
)


class UniqueIdGenerator(UniqueIdGenerationProtocol):
    def run(self, function_src: str) -> str:
        m = hashlib.md5()
        m.update(function_src.encode())
        return str(int(m.hexdigest(), 16))[0:32]
