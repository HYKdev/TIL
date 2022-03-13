# git branch

<그림>

나뭇가지 형태로 만들어 독립적으로 만들어 줌

원본이 안정적으로 보존이 됨

(master) - master branch -상용 [실제 서비스에서 사용되는 코드]



- `git branch` : 브랜치 목록 확인
- `git branch [브랜치 이름] `: 새로운 브랜치 생성
- `git branch -d [브랜치 이름] `: 특정 브랜치 삭제(병합된 브랜치만 삭제)
- `git branch -D [브랜치 이름]` : 강제 삭제
- `git switch [브랜치 이름]` : 다른 브랜치로 이동
- `git switch -c [브랜치 이름]` : 브랜치를 새로 생성과 동시에 이동
- `git log --oneline` :
- `git log --oneline --all` : 
- `git log --oneline --all  -- graph` : 
- 

merge(병합)

- `git merge [병합할 브랜치 이름]` : 
  - merge 하기전에 일단 다른 브랜치를 합치려고 하는, 즉 메인 브랜치로 swith 해야 함



## 1. fast-forward

## 2. 3-way merge(merge commit)

## 3. merge conflict

- merge하는 두 브랜치에서 같은 파일의 같은 부분을 동시에 수정하고 merge하면, git은 해당 부분을 자동으로 merge해주지 못함
- 반면 동일 파일이더라도 서로 다른 부분을 수정했다면 conflict 없이 자동으로 merge commit 된다.