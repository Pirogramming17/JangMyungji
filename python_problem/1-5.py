import random

print('베스킨라빈스 31 게임')
print('1부터 31까지의 숫자를 번갈아 불러 31을 부르는 사람이 지는 게임 입니다.')

num = 0

turn = 0 
while  num < 31:
    if turn == 0:
        p1 = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        while p1 not in [1, 2, 3]:
            p1 = int(input('1,2,3 중 하나를 입력하세요'))
            p1 = int(p1)

        for _ in range(p1):
            num += 1
            print('playerA:', format(num))

        turn += 1
        turn %= 2


    elif turn == 1:
        p2 = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        while p2 not in [1, 2, 3]:
            p2 = int(input('1,2,3 중 하나를 입력하세요'))
            p2 = int(p2)

        for _ in range(p2):
            num += 1
            print('playerB:', format(num))

        turn += 1
        turn %= 2


    
