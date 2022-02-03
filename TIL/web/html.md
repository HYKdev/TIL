# HTML

- 웹페이지를 작성하는 도구
- 마크업 문법의 일종
- 태그를 사용해서 제작함
- WHATWG 표준
- 검색할 때는 mdn 앞에 붙이고 궁금한 내용
- w3school 궁금한거 있을 때 찾아보기

## 개발환경

- vscode 사용
  - open in browser - alt+b
- 들여 쓰기 2칸



웹 사이트를 만드는 것 - 웹 프로그래밍

프론트 엔드 / 백 엔드

html 웹페이지 구조생성

hyper text markup language

텍스트를 뛰어넘는 마크로 둘러싸인 언어

태그로 데이터와 문서의 구조를 표현



css 웹페이지 스타일링

js 웹페이지 기능추가 및 조작



## 기본구조

html

head 문서에 대한 정보를 작성

body 우리가 보는 사이트를 만드는 곳

메타 데이터 - 데이터의 데이터 , 다른 데이터를 설명해주는 데이터

ex) 도서관에서 가-1-2 책의 위치를 알려주는 데이터

DOM 트리

텍스트 파일인 HTML문서를 브라우저에서 렌더링 하기 위한 구조

각 요소에 접근/수정에 필요한 프로퍼티와 메서드를 제공

요소(element)

여는 태그 / 닫는 태그

H1 = h1 같지만 h1이 정석

디버깅이 쉽지 않음 좀 틀려도 작동은 함

br  = \n 같은 동작

속성(attribute)

- <a 속성명 = "속성값"></a>   

- 공백 x, 쌍따옴표 사용

- 태그의 부가적인 정보를 설정
- 요소는 속성을 가질 수 있고, 경로나 크기와 같은 추가적인 정보 제공
- 이름과 값이 하나의 쌍으로 존재
- 모든 태그에 사용 가능한 속성(global attribute)
  - id, class, style ....
- <a> 는 탭인덱스가 자동으로 들어감
- 시맨틱 태그
  - HTML5에서 의미를 담은 태그
  - 위치를 어디에다가 둘지
  - ★ div, span,p를 제외한 대부분의 것들
  - 검색엔진최적화를 위해서 메타태그,시맨틱 태그를 활용



## 문서 구조화

- 인라인 / 블록 요소
- 텍스트 요소
- 그룹 컨텐츠
- p vs div
  - p 태그는 인라인 요소만 가능,  p태그 안에 div태그 x
  - div태그안에 p태그는 가능, 주로 구역 나눌 때 많이 사용함
- table
  - thead, tbody tfoot
  - tr th td
  - 가로를 먼저 구성하고 세로 구성
  - colspan, rowspan  셀병합 ★ (문제내기 좋음)
  - 세로인거를 두개 합치니까 colspan
  - 가로인거를 두개 합치니까 rowspan
  - caption 표 설명
  - 

- form
  - 데이터를 서버에 제출하기 위한 태그, 사용자의 데이터를 받는 곳
  - ★ action - form을 처리할 서버의 URL 
  - ★ method - form을 제출할 때 사용할 HTTP메서드 GET혹은 POST
  - get vs post

- input
  - 다양한 타입을 가지는 입력 데이터 유형
  - name
  - value
  - type= "text" 문자열로 받겠다, name="q"
  - label - 사용자는 선택할 수 있는 영역이 늘어나 다양한 환경에서 편하게 사용 가능
  - input에 있는 id속성을 label에는 for속성을 활용하여 상호 연관을 시킴 
  - ex ) 성별 남 / 여 / 기타
  - text, password, email, number, file 등등 많다
  - check box / radio
  - color date hidden
  - 

vscode에서 직접 해보기에서 챙겨가야할 것

- label, for, type, name id 서버로 전송하는 submit

checkbox와 radio에 name 같게하고 다르게 하는 차이 이해하기



