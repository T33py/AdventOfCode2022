class file:
    name:str
    size: int

class directory:
    def __init__(self) -> None:
        self.parent: 'directory'
        self.name: str
        self.files: list
        self.directories: list
        