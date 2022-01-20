# 관통PJT

## json

- data를 표현하는 방법중 하나
- key, value로 이루어져 있음



open()

​			<- 파일의 경로

​			<- 쓰기('w'), 읽기('r'), 수정('a')

​			<- encoding = 'UTF-8'



readline 1문장씩 읽음 (for, while)

```json
[
    {
        "title": "스파이더맨",
        "year": 2021
    },
    {
        "title": "돈룩업",
        "year": 2021
    },
    {
        "title": "러브레터",
        "year": 2021
    }
]
```



```python
import json

file_stream = open('data/data.json', 'r', encoding= 'UTF-8')

data = json.load(file_stream)

file_stream.close()

for each_dict in data:

    title = each_dict['title']
    year = each_dict['year']

    print(f"제목: {title} 개봉년도: {year}")
    
    #제목 :  ~ 개봉년도: ~
```

open 과 close는 짝꿍 [위 아래 코드는 같은 코드]

```python
import json

with open('data/data.json', 'r', encoding= 'UTF-8') as file_stream:
    data = json.load(file_stream)
    for each_dict in data:
        title = each_dict['title']
        year = each_dict['year']

    print(f"제목: {title} 개봉년도: {year}")
# with open으로 쓰면 open과 close를 담은 것
```





