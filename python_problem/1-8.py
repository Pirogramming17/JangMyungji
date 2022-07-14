def brGame_p1(p1, called):
    for _ in range(p1):
        called += 1
        print("playerA: {0}".format(called))

        if called == 31:
            break

    return called


def validate_input(prompt, valid_list):
    while True:
        value = input(prompt)
        if value in valid_list:
            value = int(value)
            break
        else:
            print("1,2,3 중 하나를 입력하세요.")
    return value

def brGame_p2(p2, called):
    for _ in range(p2):
        called += 1
        print("playerB: {0}".format(called))

        if called == 31:
            break

    return called

