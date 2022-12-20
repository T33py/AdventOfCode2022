from fs import file
from fs import directory

class terminal:
    

    def __init__(self):
        self.current_directory:directory = directory()
        self.current_directory.name = '/'
        self.current_directory.directories = []
        self.current_directory.files = []
        self.base_dir = self.current_directory
        

    def execute_command(self, input:str):
        command = input.replace('$ ', '')

        if command[0:2] == 'cd':
            goto = command.split(' ')[1]
            self.cd(goto)
            

        elif command[0:2] == 'ls':
            self.ls()
        
        elif command == 'tree':
            self.tree()

        else:
            print(f'Unknown command: {command}')

        return

    def tree(self, indent:str = ''):
        self.display_directory(self.current_directory, indent)
        indent = indent+'..'
        goto = []

        for f in self.current_directory.files:
            self.display_file(f, indent)
        
        for dir in self.current_directory.directories:
            goto.append(dir)

        for dir in goto:
            self.current_directory = dir
            self.tree(indent)
        
        return

    def cd(self, goto: str):
        print(f'goto: {goto}')
        if goto == '/':
            self.current_directory = self.base_dir
        elif goto == '..':
            if self.current_directory.name != '/':
                self.current_directory = self.current_directory.parent
        else:
            for dir in self.current_directory.directories:
                if dir.name == goto:
                    self.current_directory = dir
        return

    def ls(self, indent:str = ''):
        for dir in self.current_directory.directories:
            self.display_directory(dir, indent)
        for f in self.current_directory.files:
            self.display_file(f, indent)
        return

    def display_file(self, f:file, indent:str = ''):
        print(f'{indent}{f.name} {f.size}')
        return

    def display_directory(self, d:directory, indent:str = ''):
        print(indent + d.name)
        return

    def create_dir(self, name:str):
        print(f'create directory: {name} in {self.current_directory.name}')
        dir = directory()
        dir.parent = self.current_directory
        dir.name = name
        dir.files = []
        dir.directories = []
        self.current_directory.directories.append(dir)

    def create_file(self, name:str, size:int):
        print(f'create file: {name} in {self.current_directory.name}')
        f = file()
        f.name = name
        f.size = size
        self.current_directory.files.append(f)

    def is_command(self, input:str):
        if '$' in input:
            return True
        return False