# 071 my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print (type(my_variable)) #괄호는 튜플을 정의하는 기호입니다.

# 072 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라. (순위 정보는 저장하지 않는다.)
# 순위	영화1	닥터 스트레인지 2	스플릿 3	럭키
movie_rank= ('닥터 스트레인지', '스플릿', '럭키')
print (type(movie_rank))

# 073 숫자 1 이 저장된 튜플을 생성하라.
#number = (1, ) # 괄호와 함께 하나의 정숫값을 저장하면 튜플이 정의 될 것같지만 그렇지 않습니다. type()을 출력해보면 파이썬은 튜플이 아닌 정수로 인식합니다.
#print (type(number)) # 하나의 데이터가 저장되는 경우, 쉼표를 입력해만 합니다.

# 074 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
#t = (1, 2, 3)
#t[0] = 'a' #tuple은 원소(element)의 값을 변경할 수 없습니다.

# 075 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
# 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.
t = 1, 2, 3, 4
print(type(t))

# 076 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
t = ('a', 'b', 'c')
#t[0] = 'A' # TypeError: 'tuple' object does not support item assignment
t = ('A','B','C')
print(t)

# 077 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
interest = ('삼성전자', 'LG전자', 'SK Hynix')
#interest = ['삼성전자', 'LG전자', 'SK Hynix']
#print (type(interest)) #my answer
data = list(interest)
print (data)

# 078 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
interest = ['삼성전자', 'LG전자', 'SK Hynix']
data1 = tuple(interest)
print(data1)

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
# 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
data = tuple(range(2, 100, 2))
print (data) 
# The key points:
#range() lets us define the start, stop and step.
#tuple() converts any sequence or iterator into a tuple.
#print() outputs the tuple neatly.