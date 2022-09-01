import oyes
from time import sleep
from random import randint

# 화면 초기화, 이전 값 0으로 초기화
os.system('cls')
oldNum = 0

for i in range(1,101):
    randNum = randint(0,100)
    diff = (randNum - oldNum)

    if diff > 0: color = "31"
    else: color = "34"
    
    print(f'{randNum}   (\033[{color}m{diff:+}\033[0m)')
    oldNum = randNum
    sleep(0.5)
    os.system('cls')