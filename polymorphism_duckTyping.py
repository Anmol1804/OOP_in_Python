# Polymorphism - Many forms

# 1. Duck Typing

class PyCharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    def execute(self):
        print("Spell Check")
        print("Cobvention Check")
        print("Compiling")
        print("Running")

class Laptop:
    def code(self, ide):
        ide.execute()


ide = MyEditor()

lap1 = Laptop()
lap1.code(ide)