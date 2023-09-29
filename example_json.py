import json
python_dict= {
    "이름" : "홍길동",
    "나이":25,
    "거주지" : "서울",
    "신체정보" : {"키" : 175.4, "몸무게" : 71.2},
    "취미" : ["등산","자전거","독서"]
}

print(type(python_dict))
print('json 형식으로 변환')#<class 'dict'>

json_data = json.dumps(python_dict)
print(type(json_data))#<class 'str'>

print(json_data)
#{"\uc774\ub984": "\ud64d\uae38\ub3d9", "\ub098\uc774": 25, "\uac70\uc8fc\uc9c0": "\uc11c\uc6b8", 
# "\uc2e0\uccb4\uc815\ubcf4": {"\ud0a4": 175.4, "\ubab8\ubb34\uac8c": 71.2}, 
# "\ucde8\ubbf8": ["\ub4f1\uc0b0", "\uc790\uc804\uac70", "\ub3c5\uc11c"]}

#적절한 변환을 거치 json형식
json_data2 = json.dumps(python_dict, indent = 3, sort_keys = True, ensure_ascii=False)
print(json_data2)

#json.dumps : indent : 들여쓰기, sort_keys : 파이썬 데이터가 딕셔너리 타입일 때 True로 지정하면 키(key)를 기준으로 정렬, 
#           ensure_ascii : 아스키 코드로 구성된 문자열인지 여부, 기본값은 True이나 변환하고자 하는 파이썬 데이터에 한글이 포함되어있으면 False로 지정

dict_data = json.loads(json_data)
print(dict_data['신체정보']['몸무게']) #71.2
print(dict_data['취미'])#['등산', '자전거', '독서']
print(dict_data['취미'][0])#등산