# 과제 2 - 회사 조직도 만들기
#
# 구현 내용
#
# 사람 클래스를 하나 만듭니다. 사람의 기본 요소는 이름, 나이, 성별로 합시다.
# 직장 동료 클래스를 사람 클래스를 이용해서 만듭시다. 사람 기본 요소 외 별도의 추가 사항은 직급입니다.

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person("aj", "30", "man")
print(person.name)

class Coworker(Person):
    position = "대리"
    # def __init__(self, position): # 이렇게 하면 position이 추가 될 줄 알았지만 에러가 남
    #     self.position = position

coworker = Coworker("머", "왜", "안되")
print(coworker.name)
print(coworker.age)
print(coworker.gender)
print(coworker.position)

##### question
#override와 person 클래스를 불러 오는 건(?) 다른 개념인것 같음 ..
# print(coworker.name)말고 한 번에 coworker의 요소를 다 print 하고 싶은데..
