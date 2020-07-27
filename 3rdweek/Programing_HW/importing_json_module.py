# Python은 기본적으로 JSON 표준 라이브러리(json)을 제공함
# import json 을 사용하여 JSON 라이브러리를 사용할 수 있다. (python 2.6 이상)
# JSON 라이브러리를 사용하면 Python 타입의  Object를 JSON 문자열로 변경 가능 (JSON 인코딩).
# 또한 json 문자열을 다시 Python 타입으로 변경할 수 있다 (JSON 디코딩).

# 1. JSON 인코딩.
# Python object (Dic, List, Tuple 등) 을 JSON 문자열로 변경하는 것.
# 우선 JSON 라이브러리를 인코딩 한 후, json.dumps() 메서드를 사용하여 Python Object를 문자열로 변환

# 예.
import json

# 테스트용 python dictionary
customer = {
    'id' : 152352,
    'name' : '강진수',
    'history' : [
        {'date' : '2015-03-11', 'item' : 'iPhone'},
        {'date' : '2016-02-23', 'itme' : 'Monitor'},
    ]
}

# JSON 인코딩
jsonString = json.dumps(customer, indent=4)   # indent 를 지정하면 줄바꿈되어 출력됨.

# 문자열 출력
print(jsonString)
print(type(jsonString))   # class str

# 2. JSON 디코딩

# JSON 문자열을 Python 타입 (Dic, List, Tuple 등)으로 변경하는 것.
# json.loads() 메서드를 이용하여 문자열을 Python 타입으로 변경한다.

# 예.
import json

# 테스트용 json 문자열
jsonString = '{"name" : "강진수", "id" : 152352, "history" : [{"date": "2015-03-11", "item" : "iPhone"}, {"date" : "2016-02-23", "item" : "Monitor"}]}'

# json 디코딩
dict = json.loads(jsonString)

# Dictionary 데이터 체크
print(dict['name'])
for h in dict['history']:
    print(h['date'], h['item'])
