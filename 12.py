# 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
from typing import Dict
os.system("cls")

#Dictionary = {}

Dictionary = {n:3*n+1 for n in range (1,7)}
print (Dictionary)