# HelloWorld 앱 만들기

[TOC]



## 프로젝트 생성하기

```kotlin
package com.example.helloworld

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }
}
```

- package com.example.helloworld
  - com 패키지 > example 패키지 > helloworld 패키지 > MainActivity.kt 파일이다
- 같은 이름의 파일이여도 패키지가 다르면 다른 파일로 인식함

## MainActivity.kt 코드 파일

- activity == screen
- **AppCompatActivity** = 기존 Activity 클래스 + 호환성 기능
- MainActivity -> AppCompatActivity -> Activity (상속)
- `savedInstanceState: Bundle` 
  - 특정한 상황[ex) 화면 방향 변경, 메모리 부족으로 인한 앱 종료] 을 매개변수 받을 수 있다
  - bundle자리는 int, string등 들어갈 수 있고 mapping형태로 저장할 수 있다.
  - 불러올 데이터가 없는 경우 Null
- `setContentView(R.layout.activity_main)`
  - R클래스는 자동생성되는 클래스로서 모든 리소스를 식별가능하게 해줌
  - ex) R.color.[추가한 색상 id] / R.string.[추가한 문자열 id] / R.layout.[추가한 레이아웃 이름]



## 레이아웃 알아보기

- app/res/layout 폴더안에 xml파일
- code, split, design 3가지 방법으로 수정이 가능하며 split이 가장 많이 씀



## 에뮬레이터로 실행하기

- Device Manager
  - virtual - 에뮬레이터 같은 가상 기기
  - physical - 실제 기기



## 실제 기기로 실행하기

- 개발자모드로 접근
  - 빌드 번호 7번 클릭
  - 개발자 모드 활성화
  - usb 디버깅 ON (데이터 전송이 가능한 usb)
  - 무선 디버깅 ON (Wi-fi)

