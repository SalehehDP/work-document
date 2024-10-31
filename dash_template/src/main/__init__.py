from sys import path as sysPath
from os import path, getcwd

current_path = path.join(getcwd(), "src", "main")
sysPath.append(current_path)
