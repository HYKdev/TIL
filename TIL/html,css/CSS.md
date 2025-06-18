# CSS

Cascading Style Sheets

스타일을 지정하기 위한 언어

선택하고, 스타일을 지정

```css
selector
h1 {
	color: blue;	선언
	font-size: 15px;
	속성		값	
}
```

- 인라인
- 내부참조
- 외부참조 - 분리된 CSS파일 , 무조건 이거만 씀

## CSS selector

- 전체선택자, 요소 선택자

  ​	-*-                  h1,h2,h3

- 클래스 선택자   .class Name{} / <a class="class name">

- 아이디 선택자   #id_name{}  / <a id="id_name">

- 속성 선택자       button[type]   /  

- 결합자 A - B - C - B

- 자손 결합자, 자식 결합자
- 일반 형제 결합자 A~B
- 인접 형제 결합자 A+B
- 의사 클래스 ex) h2: hover

------------

참조 예시용

### 1. 동적 의사 클래스
- **:link** : 사용자가 아직 한 번도 해당 링크를 누르지 않은 상태 ( a요소 기본 )
- **:visited** : 사용자가 한 번이라도 해당 링크를 누른 상태
- **:hover** : 사용자의 마우스 커서가 위에 올라가 있는 상태
- **:active** : 사용자의 마우스 커서가 클릭중인 상태
- **:focus** : tab키로 focus가 맞춰진 상태
### 2. 상태 의사 클래스

- **:checked** : input의 checkbox나 raidobutton이 체크된 상태
- **:enabled** : input의 "type=text", select, option에서 사용자가 선택한 상태
- **:disabled** : input의 "type=text", select, option을 사용자가 선택할 수 없도록 만든 상태

### 3. 구조 의사 클래스
- **:first-child** : 모든 자식 요소 중에서 첫 번째에 위치하는 자식을 선택
- **:nth-child(n)** : 모든 자식 요소 중에서 n번째에 위치하는 자식을 선택
- **:last-child** : 모든 자식 요소 중에서 마지막에 위치하는 자식을 선택
- **:first-of-type** : 모든 자식 요소 중에서 첫 번째에 등장하는 특정 요소를 선택
- **:nth-of-type(n)** : 모든 자식 요소 중에서 n번째로 등장하는 특정 요소를 선택
- **:last-of-type** : 모든 자식 요소 중에서 마지막으로 등장하는 특정 요소를 선택



- **::first-letter** : 요소의 텍스트에서 첫 번째 글자에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::first-line** : 요소의 텍스트에서 첫 줄에 스타일을 적용한다.블록타입의 요소에만 사용 가능하다.
- **::before** : 요소의 콘텐츠 시작부분에 생성된 콘텐츠를 추가한다.
- **::after** : 요소의 콘텐츠 끝부분에 생성된 콘텐츠를 추가한다.

----------



선택자 with 개발자 도구

#sect1>ul>li:nth-child(1)



### CSS 선택자 정리

요소 선택자

클래스 선택자 (여러개 전용)

아이디 선택자 (1번만 사용)



### CSS 우선순위

인라인>id>class,속성,pseudo-class>요소,pseudo-element



### CSS 상속

속성중에는 상속이 되는 것과 되지 않는 것이 있다.

상속 되는 것

​	Text관련 요소

상속 되지 않는 것

​	Box model 관련 요소, position 관련 요소

inherit이라는 키워드를 쓰면 상속 되지 않는 것을 상속되게 가능하나 코드가 꼬일 위험이 있음



## CSS 기본스타일

### 크기단위

가변 크기 -> 상황에 따라서 크기가 바뀌는 단위

고정 크기 -> 부모,기타 등 일정한 크기 단위

"반응형"

1pt = 1/72 in

px

%

em - 부모요소 크기에 대한 배수단위 

1em = 100%

1.5em = 150%

rem - 최상위 요소 기준으로 배수단위



view port - 내가 보고 있는 화면, 디바이스 기준으로 상대적인 사이즈가 결정

vw,vh - 단위

width, height

1/100 = 1vh

100vw , 100vh - 화면 꽉채워지는 수치

100vmin - 



색상단위

색상키워드

RGB색상

a 투명도



CSS 문서 표현

텍스트

컬러, 배경



## Selctors 심화



## CSS Box model

모든 요소는 박스모델이고 

위에서 아래로 왼쪽에서 오른쪽

왼쪽 상단에 붙을려고 한다



content - 중심부

padding - content와 border사이의 거리

border 

margin 요소와 요소사이의 거리



box-sizing



## CSS Display

좌측상단 배치

디스플레이에 따라 크기와 배치가 달라진다



block

줄 바꿈이 일어나는 요소

inline

줄 바꿈이 일어나지 않는 행의 일부 요소



block 요소

div p form 



display: inline-block

block 처럼 w,h,m 속성을 모두 지정 할 수 있음

display: none

표시 x, 공간x

visibility: hidden은 해당 요소가 공간은 차지하나 화면에 표시x 

차이점 알아두기! (시험문제 가끔 나옴)



## CSS position

요소 위치를 지정

static

모든 태그의 기본 값

일반적인 요소의 배치 순서에 따름

부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치



relative 상대위치

- normal flow 유지
- 

absolute 절대위치

- normal flow 벗어남
- 부모/조상 요소를 기준으로 이동

fixed 고정위치

- normal flow 벗어남
- viewport 기준으로 이동





