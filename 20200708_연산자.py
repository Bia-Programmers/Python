'''
----------------------------------------
https://biago.ga/
2020 비아고등학교 프로그래밍 동아리 ( 파이썬 )
주제 : 연산자 ( 2020.07.08 )
Made By KimJei.
-----------------------------------------
'''

print(1+1) #2
print(3-2) #1
print(5*2) #10
print(6/3) #2

print(2**3) #2^3 = 8
print(5%3) # 나머지 구하기 2
print(10%3) # 나머지인 1

# ** 표현은 제곱하는 수로, 예를 들면 3**5면 3의 5제곱이라는 소리.

print(5//3) # //은 몫을 구하는 커맨드임.
print(10//3) # 몫인 3

print(10 > 3) # 참이기 때문에 true를 출력할꺼임
print(4 >= 7) # 부호와 같다를 같이 붙이면 크거나 같다로 표현 , false
print(10<3) # False
print (5 <= 5) # True

print(3 == 3) # True
print(4 == 2 ) # False
print(3 + 4 == 7 ) #True

# == 표현은 해당 사칙연산이 ~~와 같다 라는것을 표현하는것.

print(1 !=3) # !은 같지 않다라는것을 표현. True
print(not(1 !=3)) #False 

# not 커맨드를 붙이게 되면 반대의 조건이 붙으므로, 괄호 안에 있는 식이 참이라 해도
# not이 붙여저 있으면 반대가 됨, 거짓이 된다. ( 참 = True , 거짓 = False )

print((3 > 0) and ( 3 < 5)) # True
print((3 > 0 & ( 3 < 5))) # True

# and 명령어는 두개의 사칙연산이 모두 맞아야 하거나 모두 틀려야 함. 
# 하나는 맞고 하나는 틀리면 False로 표현된다.

# and 명령어 대신 & 로도 and 명령어를 대신할수 있다.

print ((3 > 0 ) or (3 > 5)) # True
print ((3 > 0 ) | ( 3 > 5 )) # True

# or은 둘중에 하나라도 참이면 True 라고 표현, 하나라도 거짓이면 False로 표현된다.
# or은 | 로도 or 명령어를 대신할수 있다.

print(5 > 4 > 3) # True # 공식이 성립함.
print( 5 > 4 > 7) # False , 공식이 성립하지 않음