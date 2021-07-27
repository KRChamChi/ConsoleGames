import random
import os

print("안녕하세요! 랜덤 숫자 맞추기에 오신 것을 환영합니다!\n")
print("Easy : 1 Normal : 2 || Hard : 3 || Insane : 4 || Chaos : 5\n")
print("범위 : \n1 Easy : 1~5 \n2 Normal : 1~10 \n3 Hard : 1~20 \n4 Insane : 1~50 \n5 Chaos : 1~100\n6 Custom : a~b \n")
print("난이도를 선택해주세요!")
a = int(input())

if a==6:
    print("커스텀에서 사용할 숫자를 작성해주세요\n주의사항: a는 b보다 작아야 합니다.")
    cus = int(input())
    tom = int(input())

easy = random.randint(1, 5)
normal = random.randint(1, 10)
hard = random.randint(1, 20)
insane = random.randint(1, 50)
chaos = random.randint(1, 100)
custom = random.randint(cus, tom)

print("난이도를 선택하셨으면 숫자를 써주세요!")

b = int(input())
if a==1:
    if b==easy:
        print("SUCCES!!")

    else:
        print("FAILED")

if a==2:
    if b==normal:
        print("SUCCES!!")

    else:
        print("FAILED")

if a==3:
    if b==hard:
        print("SUCCES!!")

    else:
        print("FAILED")

if a==4:
    if b==insane:
        print("SUCCES!!")

    else:
        print("FAILED")

if a==5:
    if b==chaos:
        print("SUCCES!!")

    else:
        print("FAILED")

if a==6:
    if b==custom:
        print("SUCCES!!")

    else:
        print("FAILED")

os.system('pause')

