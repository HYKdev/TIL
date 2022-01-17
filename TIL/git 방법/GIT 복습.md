# GIT

	## repository

​	커밋이 저장되는 곳 (저장소)

- git init 로컬 레포지토리 생성

- .git 이라는 폴더가 생성이 되고, git이 관리하는 모든 정보

- git status : 현재 레포지토리에 git이 어떤 상태인가를 체크
- README.md : 내 레포지토리에 대한 설명서 같은 역할을 하는 파일
- git add . : staging area로 올리는 역할 / git에게 추척하는 파일임을 선언
- git config [user.name / user.email]  

- git commit 치고 엔터치면 CLI  메모장 같은 느낌 / Vim이라는 프로그램 실행
- i : 수정모드
- esc : 수정모드 종료

- :wq (write quit) : 저장 하고 나감

- vi README.md : 편집모드 들어가는 방법

- git remote add origin url

  ​						이름  주소       

  - git push -u origin master

​								이름	뭐를

​					맨 처음 할 때는 u옵션을 줘야 함

​					-u : set up

- public : 볼 수 있고, 다운(clone) 받을 수 있고, push는 나만 가능
- private : 볼 수 없고, 다운 불가, push는 나만 가능

- repo 안에 repo는 금지

- push 전에는 pull이 있다. ★

  가장 최신 버전을 땡겨와서 작업 하기 !

