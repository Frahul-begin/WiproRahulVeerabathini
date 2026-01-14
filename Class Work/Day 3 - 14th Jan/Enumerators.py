fruites = ['apple','orange','banana']
for index, value in enumerate(fruites):
    print(index, value)

from enum import Enum

class color(Enum):
    Red = 1
    Green = 2
    Yellow = 3
print(color.Red.value)
print(color.Red.name)
