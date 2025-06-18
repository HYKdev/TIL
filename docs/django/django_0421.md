server

- web server

   - api server



1. request, web page - response의 body

2. request, 요청한 것 처리 - 그 결과를 response의 body



장바구니 과정

client --------------1. request, 장바구니에 000을 담아줘-------------------------------------> server

​		<----------------------3. response--------------------------------------------------------------	2. 처리 view-model

​								{ 'result': 'success', 'msg':'additemtocart'}

​							이러한 것을 body에 담아서 하는 걸 API server   형식(json)



http - 클라이언트와 서버가 서로 어떤 형식으로 데이터를 보내줄건지를 약속한 것

ftp, ssh, telnet,smtp, http, https

http의 특성

stateless - connectless 때문에 발생한 것, 서버가 클라이언트를 기억하지 못함(식별 불가능)

​				매번 요청할 때마다, 내가 누군지를 서버에게 알려줘야해요.

connectioness - 클라이언트와 서버가 한 번 응답을 주고 받으면, 연결을 끊는다.

​						리소스를 끊기 위해서 한 번씩만 응답함

=> 이것이 불편해서 쿠키와 세션이 등장!

쿠키 - 클라이언트 ! 너가 기억해서 나한테(서버) 들고와

​		쿠키에 담긴 정보가 접근하기 쉬워서 해킹위험성이 높음 -> 보안이 취약

세션 - 민감한 정보, 서버가 기억해줄게



http method

클라 - > 서버 request

c - post

r - get

u - put

d - delete

request - head 와 body로 나누어져 있음

head - 요청에 대한 부가정보 (method)

body - 실제 데이터

body는 있을 수도 있고 없을 수도 있음

post할 때 바디에 담아서 보냄



headers

authority, path, method scheme, 쿠키 등 각각의 정보가 담겨 있는 것



http response - head와 body로 나누어져 있음

head - 요청에 대한 부가정보 (status code)

body - 실제 데이터



status code는 그냥 숫자이고

status message는 각각의 상태 코드에 대한 출력해야할 메세지를 담고 있다

200 ok

404 not found



http status code

100 - 서버가 클라이언트한테, 정보성 응답

/ 100 - continue

200 - 일반적인, 정상적인 상황

/ 200 - ok

/ 201 - created

300 - 

/ 301 - moved (permanently)

/304 - not modified (수정되지 않았음) [캐쉬랑 연결되어 있음]

400 - 클라이언트 에러

/ 400 - bad request

/ 401 - unauthorized

/ 403 - forbidden

/404 - not found

/429 - Too many requests

500 - 서버 잘못

/ 500 - internal server error

/ 503 - service unavailable [트래픽 폭주, 수강신청같은 경우]

/ 

resource - 서버에 존재하는 정보, 자원, 데이터



api - web api 

약속 - > 어떻게 설계해도 기능적으로 문제x

rest api(약속) 

-> 표현적인 상태 이전

1. URL은 리소스를 나타내기 위해서만 사용하고, 리소스에 대한 처리는 메서드로 표현한다.
2. Document는 단수명사로, collection은 복수 명사로 표현한다.



