# 231
# 아래 코드를 실행한 결과를 예상하라.
# def n_plus_1 (n) :
#     result = n + 1
# n_plus_1(3)
# print (result)
# 에러가 발생합니다.
# NameError Traceback (most recent call last)
# <ipython-input-2-78e20c8ecef0> in <module>()
# 3 
# 4 n_plus_1(3)
# ----> 5 print (result)
# 6
# NameError: name 'result' is not defined
# 함수 내부에서 사용한 변수는 함수 밖에서는 접근이 불가능합니다. 
# (문법이 그래요) 함수 내부에서 계산한 값을 전달하기 위해서는 return을 사용해야 합니다.

# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
def make_url(name):
    domain = "www."+ name + ".com"
    return domain
result = make_url("naver")
print (result)

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# make_list("abcd")
# ['a', 'b', 'c', 'd']
def make_list(string):
    my_list = []
    for i in string:
        my_list.append(i)
    return my_list #answer
def make_list1 (string) :
    return list(string)
domain = make_list("abcd")
print (domain)
domain1 = make_list1("abcd")
print (domain1)

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]
def pickup_even(list):
    my_even_list=[]
    for i in list:
        if i % 2 ==0:
            my_even_list.append(i)
    return my_even_list
number = pickup_even([3, 4, 5, 6, 7, 8])
print(number)

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
def convert_int(string):
    return int(string.replace(',',''))
number_22 = (convert_int("123,544,333"))
print (number_22)

# 236
# 아래 코드의 실행 결과를 예측하라.
# def 함수(num) :
#     return num + 4
# a = 함수(10)
# b = 함수(a)
# c = 함수(b)
# print(c)
#22
# 정답확인
# 4번 라인에서 함수로 10이 입력돼서 14가 반환됩니다. a 변수에는 14가 저장됩니다. 
# 5번 라인에서 함수로 14가 입력돼서 18이 반환됩니다. 변수 b에는 18이 바인딩됩니다. 
# 6번 라인에서 함수로 18가 입력돼서 22가 반환됩니다. 변수 c에는 22가 바인딩됩니다.

# 237
# def 함수(num) :
#     return num + 4
# c = 함수(함수(함수(10)))
# print(c)
# 22
# 함수가 여러번 중첩돼 있습니다. 안쪽 부터 차례로 해석하면 됩니다. 
# 함수(10)의 결과 14, 함수(14) 결과 18, 함수(18) 결과 22 가 반환됩니다. 
# 결국 36번과 동일한 코드를 축약해서 작성해 놓은 겁니다.

# 238
# 아래 코드의 실행 결과를 예측하라.
def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10)
c = 함수2(a)
print(c)
# 140
# 7번 라인에서 함수1으로 10이 입력돼서 14가 반환됩니다. a 변수에는 14가 저장됩니다. 
# 8번 라인에서 함수2로 a에 저장된 14가 입력돼서 140이 반환됩니다. 변수 c에는 140이 바인딩됩니다.

# 239
# 아래 코드의 실행 결과를 예측하라.
def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)
# 16

# 240
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)
c = 함수2(2)
print(c)
#28



            
