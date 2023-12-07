# 041 upper 메서드
#다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
#ticker = "btc_krw"

ticker = "btc_krw"
ticker = ticker.upper()
print (ticker)

# 042 lower 메서드
#다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
#ticker = "BTC_KRW"

ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043 capitalize 메서드
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

greeting = 'hello'
greeting = greeting.capitalize()
print (greeting)

# 044 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
#file_name = "보고서.xlsx"

file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 045 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
#file_name = "보고서.xlsx"
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls"))) #튜플이 들어감

# 046 startswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

# 047 split 메서드
# 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
#a = "hello world"
a = "hello world"
a = a.split(" ")
print (a[1])

# 048 split 메서드
# 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
ticker = "btc_krw"
ticker = ticker.split("_")
print (ticker[1])

# 049 split 메서드
# 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"

data = "2020-05-01"
data = data.split("-")
year = data[0]
month = data[1]
date = data[2]
print (year, month, date) # 내 정답

# 050 rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "

data = "039490     "
data = data.rstrip()
print (data) # rstrip() 메서드를 사용하면 오른쪽 공백이 제거된 새로운 문자열 객체가 반환됩니다. 그 값을 data라는 변수가 새로 바인딩합니다. 기존의 공백이 포함된 문자열은 메모리에서 자동으로 삭제됩니다.

