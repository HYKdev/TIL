# Array 2

## 2차원 배열

- 1차원 list를 묶어놓은 list
- 행렬의 갯수가 필요함
- 변수선언과 초기화 가능

## 배열 순회

**행 우선순회**

```python
for i in range(n):
	for j in range(m):
		Array[i][j]
```

**열 우선순회**

```python
for j in range(n):
    for i in range(m):
        Array[i][j]
```

**지그재그 순회**

```python
for i in range(n):
	for j in range(m):
        Array[i][j+(m-1-2*j)*(i%2)]
```

**델타를 이용한 2차 배열 탐색**

```python
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for k in range(4):
    nx = x + dx[k]
    ny = y + dy[k]
```

**전치 행렬**

```python
for i in range(n):
	for j in range(n):
        if i < j :
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
```

## 부분집합

- 원소가 n개일 때 , 2^n개 이다



## 비트 연산자

- &  AND 연산

- |  OR연산

- << 열을 왼쪽으로 이동

- '>>' 열을 오른쪽으로 이동

- 1 << n : 2^n 원소가n개 일 경웅의 모든 부분 집합의 수

- i & (1<<j) i의 j번째 비트가 1인지 아닌지 검사



## 검색(search)

- 저장되어 있는 자료 중에서 원하는 항목을 찾는 작업
- 탐색키 : 자료를 구별하여 인식할 수 있는 키



검색의 종류

- 순차검색

일렬로 된 자료를 순서대로 검색

수행시간이 급격히 증가하여 비효율적

정렬되어 있지 않으면 찾고자 하는 원소의 순서에 따라 비교횟수가 결정됨

정렬되어 있으면 원소의 키 값이 검색대상의 키 값보다 크면 찾는 원소가 없으므로 검색안함

평균 비교 회수가 반으로 줄어든다.

- 이진 검색

항목의 키값과 비교하여 다음 검색의 위치를 결정하고 검색을 진행

자료가 정렬된 상태여야 한다. 

- 해쉬
- 