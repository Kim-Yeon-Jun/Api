#웹 사이트 주소에 부가 정보 추가하기
#기본 웹 사이트 주소를 유지하면서 경로를 변경해가며 데이터를 요청해야 하는 경우
# base_url = 'https://api.example.com/'
# sub_dir = 'events'
# url = base_url+sub_dir
# print(url)

import requests

base_url = 'https://api.github.com/'
sub_dirs = ['events','user','emails']

for sub_dir in sub_dirs:
    url_dir = base_url + sub_dir
    r = requests.get(url_dir)
    print(r.url)