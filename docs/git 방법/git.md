# Git

- 분산 버전 관리 시스템



- 코드의 히스토리(버전)을 관리하는 도구

- 개발되어온 과정 파악 가능

- 이전 버전과의 변경 사항 비교 및 분석

<img src="git.assets/%EB%B2%84%EC%A0%84%EA%B4%80%EB%A6%AC.PNG" alt="버전관리" style="zoom:33%;" />

A 버전관리 전

B 버전관리 후



- 처음 만든게 맞거나 저번주에 만들었던게 맞은 경우 버전관리를 통해 돌아갈 수 있음



- 중앙집중 ex) 은행

- 분산형 ex) 블록체인, 비트코인

- 변조 불가능



unix Linux windows 

macos

CLI (command line interface) <-> GUI 



- unix 명령어    

​		ls [현재 위치의 폴더 파일 목록보기]

​		clear [터미널 내용 정리]

​		cd 경로 [현재 위치 이동하기]

​		cd .. [상위 폴더로 이동]

​		mkdir 이름 [폴더 생성하기]

​		touch 이름 [파일 생성하기]

​		rm 이름 [파일 삭제]

​		rm -r [폴더 삭제]

- 명령 프롬프트

​		DIR

​		clr

- 명령어 자동완성 tab
- -r : recursive



- git bash

​		code . => vscode 실행



- 터미널 단축키

​		ctrl shit `



# repository

## 	특정 디렉토리를 버전 관리하는 저장소



working directory - 내가 작업하고 있는 실제 디렉토리

staging area - 잠깐 변경사항만 남겨 놓는 곳으로서 특정 버전으로 관리하고 있는 파일이 있는 곳

Repository - 커밋들이 저장되는 곳



특정 버전으로 남긴다 = 커밋 한다

​											3가지 영역을 바탕으로  동작



git                  git init

git add 변화를 감지하고 버전관리 시작



git commit -m ""

git log



staging area

남기고 싶은 관리하고 싶은!



### git status

​	현재 git으로 관리되고 있는 파일들의 상태를 알 수 있어요



main ,  branch

master , init add.txt



신원확인 x 

git add       o  신원확인이 필요없음 (컴퓨터에 잠깐 저장하는 개념)

git commit x  신원확인이 필요함



- git status

​	현재 git으로 관리되고 있는 파일들의 상태를 알 수 있어요

- git add .

​	추적되지 않는 모든 파일과 추적 하고 있는 파일 중 수정 된 파일을 모두 staging area에 올려요

- git commit -m "message"

​								메세지 내용은 자세하게

- git config user.name "user_name"

- git config user.email "user_email"

- git log

​	git의 commit history 보기

- git diff

​	두 commit 간 차이 보기

- git remote add origin url{remote_repo}

- git push -u origin master

  local->remote

- git pull

  remote->local



- github에서 코드 수정 x

- 각자 local에서 코드를 수정해서 push pull 이용



- git remote add origin {remote_repo}

​                              별명    url주소

- git push -u origin master

​                     별명    local branch



- git clone {remote_repo}
- git push origin master