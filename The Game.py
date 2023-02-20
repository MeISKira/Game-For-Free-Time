import random
import colorama
import os
import time

Cw = colorama.Fore.WHITE
Cb = colorama.Fore.BLACK
Cc = colorama.Fore.CYAN
Cr = colorama.Fore.RED
Cg = colorama.Fore.GREEN

while True:
    num_Random = random.randint(1, 10)
    user_input = int(input(Cw + 'Enter Number Random [1, 10] >> '))
    print(Cg + f'You Win num is {num_Random}') if num_Random == user_input else print(Cr + f'You Loss num is {num_Random}')
    time.sleep(0.6)
    os.system('cls')