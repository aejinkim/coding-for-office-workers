# 과제 3 - 가위 바위 보 게임
#
# 구현 내용
#
# 사용자에게 가위, 바위, 보 중 하나를 물어봅니다.
# 사용자가 가위, 바위, 보를 고르면, 컴퓨터도 같이 가위, 바위, 보를 내고 승패를 가릅니다.
# 다합쳐 3번을 지거나, 3번을 이기면 게임은 최종 스코어를 보여 주면서 끝이 납니다.

import random
game = ["가위","바위","보"]

count_win = 0
count_lose = 0

def rockPaperScissors():
    user = input("가위,바위,보 중 어떤걸 내겠습니까?")
    computer = random.choice(game)

    print("user:" + user)
    print("computer:" + computer)

    if user == computer:
        print("비겼습니다")
        return 0

    elif user == "가위" and computer == "바위":
        print("컴퓨터가 이겼습니다")
        return -1
    elif user == "가위" and computer == "보":
        print("당신이 이겼습니다")
        return 1
    elif user == "바위" and computer == "보":
        print("컴퓨터가 이겼습니다")
        return -1
    elif user == "바위" and computer == "가위":
        print("당신이 이겼습니다")
        return 1
    elif user == "보" and computer == "가위":
        print("컴퓨터가 이겼습니다")
        return -1
    elif user == "보" and computer == "바위":
        print("당신이 이겼습니다")
        return 1

while count_win < 3 and count_lose < 3:
    result = rockPaperScissors()
    if result == 1:
        count_win = count_win + 1
    elif result == -1:
        count_lose = count_lose + 1
if count_win == 3:
    print("최종 승리하였습니다")
else:
    print("안타깝네요")

print("count_lose:" + str(count_lose))
print("count_win:" + str(count_win))
