# 211
# 함수의 호출 결과를 예측하라.
# def 함수(문자열) :
#     print(문자열)
# 함수("안녕")
# 함수("Hi")
#안녕 Hi

# 212
# 함수의 호출 결과를 예측하라.
# def 함수(a, b) :
#     print(a + b)
# 함수(3, 4)
# 함수(7, 8)
# 7, 15

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(문자열) :
#     print(문자열)
# 함수()
# TypeError: 함수() missing 1 required positional argument: '문자열'
# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를 입력해야한다.

# 214
#def 함수(a, b) :
#     print(a + b)
# 함수("안녕", 3)
# TypeError: must be str, not int
# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로 설계됐습니다. 
# 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는 더할 수 없다는 에러가 발생합니다.

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
def smile(str):
    print(str,":D")
smile("Hi")

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
def smile(str):
    print(str,":D")
smile("안녕하세요")

# 217
# 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(price):
    print(price*1.3)
print_upper_price(55545)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum (num1, num2):
    print(num1 + num2)
print_sum (5, 10)

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.

# def print_arithmetic_operation(a, b):
#     print(a, '+', b, '=', a + b)
#     print(a, '-', b, '=', a - b)
#     print(a, "*", b, "=", a * b)
#     print(a, "/", b, "=", a / b)
# print_arithmetic_operation(1, 5)

def print_arithmetic_operation(a,b):
    print("{}+{}={}".format(a, b, a+b))
    print("{}+{}={}".format(a, b, a-b))
    print("{}+{}={}".format(a, b, a*b))
    print("{}+{}={}".format(a, b, a/b))

print_arithmetic_operation(5,60)            

# 220
# 세 개의 숫자를 입력받아 가장 큰수를 출력하는 print_max 함수를 정의하라. 단 if 문을 사용해서 수를 비교하라.
def print_max(a, b, c):
    if a > b and a > c:
        print (a)
    elif b > a and b > c:
        print (b)
    else:
        print (c)
print_max(6,5,4)
