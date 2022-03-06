# Django

- 파이썬 무료 오픈소스 웹 app framework

## web framework

- 웹 서비스를 만드는데 필요한 도구들
- 재사용성을 높여주는 것
- 

cllient --- 요청 --> 서버

client <-- 응답 --- 서버

웹브라우저(크롬)

정적 웹 페이지

- 모든 상황에서 모든 사용자에게 동일한 정보를 표시

동적 웹 페이지

- 추가적인 처리 과정 이후 클라이언트에게 응답을 보냄
- 방문자와 상호작용하기 때문에 페이지 내용은 그때그때 다름
- 유저가 요청을 보내면 응답(웹페이지)을 받음



framework architecture

- MVC design pattern
- django는 MTV pattern이라고함
- Model - 데이터베이스의 기록을 관리 [DB]
- Template - (mvc pattern에서는 view역할) 실제 내용을 보여주는데 사용 [HTML]
- ★ View - HTTP 요청을 수신하고 HTTP응답을 반환, template에게 응답의 서식 설정을 맡김 [조작, 가공]

|    MVC     |   MTV    |
| :--------: | :------: |
|   model    |  model   |
|    view    | template |
| controller |   view   |

1. HTTP Request
2. URLS
3. View (model, template와 상호작용함)
4. HTTP Response

![](django.assets/%ED%99%94%EB%A9%B4%20%EC%BA%A1%EC%B2%98%202022-03-02%20131527.png)



LTS (장기 지원 버전)



Project & Application

project

- 

★ Application

- 

url -> view -> template 데이터 흐름 순서로 작성

1. 가상환경 생성 및 활성화
2. django 설치
3. 프로젝트 생성
4. 서버 켜서 로켓 확인하기
5. 앱 생성
6. 앱 등록

trailing coma 하도록 권장함



TDD- 검색해서 한번 알아보기

모든 뷰는 함수 형태로 작성한다.

404(잘못된 요청), 200(정상) 상태코드

```python
def index(request):
	가공하는 코드
    return render(request, 'index.html',C)
				A             B       C
    C자리는 model과 데이터를 가공해서 만들어진 데이터의 자리
```



경로 ( 샌드위치 구조 )

app/templates/aritcles(app이름)/index.html

Django 가이드 라인

​					127.0.0.1:8000

IP(컴퓨터의 주소)			port(이 컴퓨터랑 프로그램이 소통하는 창구)



## HTML Form

action : 입력 데이터가 전송될 URL 지정

method : 입력 데이터 전달 방식 지정

- get - 
- post - 

input element

- type 속성에 따라 동작 방식이 달라짐
- ★ name - 양식을 제출했을 때 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
- GET/POST 방식으로 서버에 전달하는 파라미터(name은 key, value는 value)로 매핑함
- GET방식 URL => ~/dinner/?name=aiden&address=seoul [쿼리스트링]

label element

- input에 id속성 부여
- label에는 input의 id와 동일한 값의 for속성이 필요

HTTP

request method 종류

- **GET, POST,** PUT, DELETE ...



GET

- 서버로부터 정보를 조회하는데 사용
- 데이터를 가져올 때만 사용해야 함
- Query String Parameters를 통해 전송



디폴트가 get방식



URL

- dispatcher(발송자, 운항 관리자) 로서의 URL
- 

variable Routing

- 변수 값에 따라 하나의 path()에 여러 페이지를 연결 시킬 수 있음
- 

url path converters

- str - 작성하지 않을 경우 기본값
- int
- slug

★ include

