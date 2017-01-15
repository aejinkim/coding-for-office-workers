# 과제 1 - 맛집 고르기
#
# 구현 내용
#
# 처음 파이썬 파일을 실행 시키면, 한식, 중식, 일식 중 한 가지를 고르라는 내용이 나옵니다.
# 그 중에서 한 가지를 고르면 식당 이름을 하나 임의로 추천해 줍니다.

import random
input_q = input ("한식,중식,일식 중 무엇을 고르시겠습니까?")

korea = ['천리집', '함지박', '김밥천국', '비채나', '일호식', '밍글스']
chinese = ['골드피쉬', '쮸즈', '미스터서왕만두', '포담', '쟈니덤플링', '일일향']
japanese = ['정돈', '이치에', '오가와', '갓포아키', '히메시야', '토야']

if input_q == "한식":
    print (random .choice(korea))
elif input_q == "중식":
    print (random.choice(chinese))
else:
    print (random.choice(japanese))
