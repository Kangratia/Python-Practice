# 201 ~ 202
# def print_coin():
#     print("비트코인")
# print_coin()

# 203
# 201번에서 정의한 print_coin 함수를 100번호출하라.
# for i in range(100):
#     print_coin()

# 204
# "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.

# def print_coin():
#     for i in range(100):
#         print("비트코인")
# print_coin()

# 205
# 아래의 에러가 발생하는 이유에 대해 설명하라.
# hello()
# def hello():
#     print("Hi")
# 실행 예
# NameError: name 'hello' is not defined
# 함수가 정의되기 전에 호출되어서 에러가 발생합니다.

# 206
# 아래 코드의 실행 결과를 예측하라.
# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()
# A B C A B #answer

# 207
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message() :
#     print("B")
# print("C")
# message()
#ACB

# 208
# 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# print("A")
# def message1() :
#     print("B")
# print("C")
# def message2() :
#     print("D")
# message1()
# print("E")
# message2()
# A C B E D

# 209
# def message1():
#     print("A")
# def message2():
#     print("B")
#     message1()
# message2()
# BA

# 210
# def message1():
#     print("A")
# def message2():
#     print("B")
# def message3():
#     for i in range (3) :
#         message2()
#         print("C")
#     message1()
# message3()
# B C B C B C A