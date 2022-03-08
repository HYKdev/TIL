# django Model

## Model

django 데이터의 구조를 미리 잡아 두는 것

단일한 데이터에 대한 정보를 가짐

​	데이터들의 필수적인 필드들과 동작들을 포함

★ model을 통해 데이터에 접근하고 관리할 수 있다.

DB - 체계화된 데이터의 모임

쿼리 - 쿼리를 날린다(DB를 조작한다.) sql / 데이터를 조회하기 위한 명령어

스키마 - 데이터베이스에서 자료의 구조, 표현방법, 관계등을 정의한 구조 (설계도)

테이블 - 데이터를 추가하는 건 row 속성은 column

레코드 - 행 1줄

pk - 데이터베이스 관리 및 관계 설정시 주요하게 활용 (일반적으로는 id라고 부름)



## ORM

- Object Relational Mapping

객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 프로그래밍 기술 

DB

1. 테이블 있는 SQL
2. 테이블 없는 NOSQL - 빠르게 변하는 데이터를 저장하는 곳



DB - SQL statement - ORM - Python Object - Python

장점 

- SQL을 잘알지 못해도 DB조작 가능
- 높은 생산성

단점

- ORM만으로 완전한 서비스를 구현하기 어려움
- 효율성이 좀 떨어짐

현대 웹 프레임워크의 요점은 웹 개발의 속도를 높이는 것(생산성)



데이터의 구조

앱 별로 나눌 수 있지만 굳이?

pk를 따로 지정해주지 않으면 id가 알아서 0,1,2,3,4 지정해서 들어감



field option

null - db에 저장될 때 null값이 들어갈지 말지

blank - 빈 값으로 지정해도 될지



charField는 max_length가 필수

TextField는 제한 없음



model 조작(생성, 수정, 삭제)

-> 마이그레이션 생성, 반영(적용)



1. charField, TextField

2. python manage.py makemigrations
   마이그레이션 만드는 방법

3. python manage.py migrate
   마이그레이션을 실제 db에 적용하는것

python manage.py sqlmigrate articles 0001
                                                 app_name 마이그레이션 number
=> sql 명령어
CREATE TABLE "articles_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(30) NOT NULL, 
"content" text NOT NULL)



python manage.py showmigrations
마이그레이션이 적용 됐는지 확인하는 명령어



  created_at = models.DateTimeField(auto_now_add=True)

  updated_at = models.DateTimeField(auto_now=True)

변경될 때 마다는 auto_now

최초 생성일때는 auto_now_add



필드 추가후 makemigrations를 하면 기존에 있던 데이터에 추가하는 거라서 그에 맞는 옵션을 줘야 한다.



from articles.models import Article

Article.objects.all()

article = Article()

 article.title = "첫번째 글"

 article.content = "푸틴이 정신을 차려야할텐데 ..."

article.save()

article = Article.objects.all()[0]

article.title

article.content

article = Article(title="두번째 글", content="점심뭐먹지?")

Article.objects.create(title="세번째 글", content="살빼야 하는데?")



exit() 나가기

pip freeze > requirements.txt

현재 pip list들이 requirements.txt에 기록해줌



installed_apps 에는 정해진 순서대로 적어주는게 좋음

## Migrations



## Database API



## CRUD

Create

1. 인스턴스를 만들고 save하는 방법

- article = Article()
- article.title = " ----- "
- article.content = " --- "
- article.save()

2. keyword 인자를 넘기는 방식

- article = Article(title= " ---- ", content = " ---- ")

3. create() 이용하는 방법

- Article.objects.create((title=" ---- ", content=" ---- ")



READ

- 모든 데이터 조회 - all
- 한개의 데이터 조회 - get
- 여러개의 조건에 맞는 데이터 조회 - filter

https://docs.djangoproject.com/en/3.2/ref/models/querysets/#filter



UPDATE

article = Article.objects.get(pk=4)

article.title = "변경할 내용"

article.save()



DELETE

article = Article.ojbects.get(pk=4)

article.delete()



http method

get - 기본값, 서버 리소스를 요청할 때 (R) (URL query string)

post - 리소스를 생성 수정 삭제 (CUD) (body)



csrf token

middleware



## Admin Site

