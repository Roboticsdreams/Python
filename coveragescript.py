import os

currentDirectory = os.getcwd()
os.chdir(currentDirectory)
os.system("python -m unittest")
os.system("coverage run -m unittest")
os.system("coverage report")
os.system("coverage html")

