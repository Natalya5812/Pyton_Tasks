# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

import os
os.system("cls")

# Version1:
#N = int (input ("Введите произвольное число: "))
#if ((N%5==0 and N%10==0 or N%15==0) and N%30!=0): 
#    print ("Условия выполняются!")
#else:
#    print ("Условие не выполняется...")

# Version2:
N = int (input ("Введите произвольное число: "))
print (bool((N%5==0 and N%10==0 or N%15==0) and N%30!=0))


