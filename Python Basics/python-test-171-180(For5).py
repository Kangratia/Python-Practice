# 171
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 32100
# 32150
# 32000
# 32500
# price_list = [32100, 32150, 32000, 32500]
# for i in range(4):
#     print(price_list[i]) # answer
# for i in range(len(price_list)):
#     print(price_list[i]) # better answer

# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 0 32100
# 1 32150
# 2 32000
# 3 32500
# for i in range(len(price_list)):
#     print(i, price_list[i])
# for i, data in enumerate(price_list):
#     print(i, data) # answer

# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 3 32100
# 2 32150
# 1 32000
# 0 32500
# price_list = [32100, 32150, 32000, 32500]
# for i in range(len(price_list)):
#     print((len(price_list) - 1) - i, price_list[i])

# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.
# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500
# price_list = [32100, 32150, 32000, 32500]
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])

# 175
# my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 가 나
# 나 다
# 다 라
# 어렵다면 한단계씩 생각해 봅시다. for문을 사용하지 않고 인덱싱만을 사용해서 코드를 작성해보면 인덱스간의 규칙관계가 눈에 들어옵니다. 
# 같은 행에 있는 두 개의 데이터는 인덱스가 +1 차이납니다. 또한 행이 증가할 때마다 인덱스가 +1 씩 증가합니다.
# my_list = ["가", "나", "다", "라"]
# print(my_list[0], my_list[1])
# print(my_list[1], my_list[2])
# print(my_list[2], my_list[3])
# 분석한 규칙을 바탕으로 반복문을 작성합시다. 아래는 첫 열 "가 나 다" 를 한 라인에 하나씩 출력하는 코드입니다. 
# for 문이 인덱스를 0, 1, 2 차례로 바인딩하고 인덱싱을 사용해 값을 출력합니다.
# for i in [0, 1, 2]:
#     print(my_list[i])
# 한 행에 두 개의 데이터를 출력하고 싶기 때문에 이전 코드의 print 문에 출력하고 싶은 데이터를 추가합니다. 
# 같은 행의 두 데이터는 인덱스 차이가 +1 이라는 것을 잊지마세요. * i가 0일 때는 0, 1 위치의 값이 출력됩니다. 
# * i가 1일 때는 1, 2 위치의 값이 출력됩니다. * i가 2일 때는 2, 3 위치의 값이 출력됩니다.
# for i in [0, 1, 2]:
#     print(my_list[i], my_list[i+1])
# 위의 코드를 사용해도 원하는 출력값을 얻을 수 있지만 아래는 코드를 보다 일반적인 형태로 변경했습니다. 
# len 함수를 사용한 것을 눈여겨 보세요.
# for i in range( len(my_list) - 1 ) : # 괄호 안에는 3 -1 = 2임. 즉 0, 1, 2가 i에 들어감
#   print(my_list[i], my_list[i+1]) # 가, 나 (0) 나, 다 (1)
# 아래와 같이 작성해도 됩니다. 인덱스를 갖고 노는 겁니다. for문을 단계별로 풀어 써가며 확인해보세요.
# for i in range( 1, len(my_list) ) :
#   print(my_list[i-1], my_list[i])

# 176
# 리스트를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라", "마"]
# 가 나 다
# 나 다 라
# 다 라 마
# my_list = ["가", "나", "다", "라", "마"]
# for i in range(len(my_list)-2):
#     print(my_list[i],my_list[i+1],my_list[i+2])

# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가
# my_list = ["가", "나", "다", "라"]
# for i in range(len(my_list) - 1, 0, -1):
#     print(my_list[i], my_list[i-1])
# for i in range(len(my_list)-1):
#     print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])

# 178
# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과의 차분값을 화면에 출력하라.
my_list = [100, 200, 400, 800]
# 예를들어 100을 기준으로 우측에 위치한 200과의 차분 값를 화면에 출력하고, 
# 200을 기준으로 우측에 위치한 400과의 차분값을 화면에 출력한다. 
# 이어서 400을 기준으로 우측에 위치한 800과의 차분값을 화면에 출력한다.
for i in range(len(my_list)-1):
     print (my_list[i+1]-my_list[i])

# 179
# 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을 계산하고 이를 화면에 출력하라.
my_list = [100, 200, 400, 800, 1000, 1300]
#첫 번째 줄에는 100, 200, 400의 평균값이 출력된다. 
#두 번째 줄에는 200, 400, 800의 평균값이 출력된다. 
#같은 방식으로 나머지 데이터의 평균을 출력한다.
# for i in range(len(my_list)-2):
#      print ((my_list[i]+my_list[i+1]+my_list[i+2])/3)

# 180
# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 
# 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
     volatility.append(high_prices[i] - low_prices[i])
print(volatility)

