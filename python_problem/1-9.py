import random

print('베스킨라빈스 31 게임')
print('1부터 31까지의 숫자를 번갈아 불러 31을 부르는 사람이 지는 게임 입니다.')

number = 0

turn = 0 
while True:
    if turn == 0:
        p1 = int(input('부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :'))
        for _ in range(p1):
            number += 1
            print('player:', number)

        turn += 1
        turn %= 2

    elif turn == 1:   
        c1 = random.randint(1, 3)
        for _ in range(c1):
            number += 1
            print('computer', number)

        turn += 1
        turn %= 2

    if number >= 31:
        break

if turn == 0:
    print('player win!')
else:
    print('computer win!')
