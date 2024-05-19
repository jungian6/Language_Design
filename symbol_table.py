from main import *

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        """Get a value from the symbol table by name"""
        value = self.symbols.get(name, None)
        if value is None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        """Set a value in the symbol table"""
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]
