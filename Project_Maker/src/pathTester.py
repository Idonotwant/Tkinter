import os
import pathlib

print(os.getcwd())

print(__file__)
print(os.path.abspath(__file__))

print(os.path.pardir)
print(os.sep)

print("pathlib")
print(pathlib.__file__)
print(pathlib.Path.cwd().parent)
print(pathlib.Path.parent)