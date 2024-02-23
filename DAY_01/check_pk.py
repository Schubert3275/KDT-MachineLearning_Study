"""
설치 패키지 버전 체크
"""

import pandas as pd
import sklearn
import matplotlib
import seaborn
import bs4

print(f"Pandas        version : {pd.__version__}")
print(f"Scikit-learn  version : {sklearn.__version__}")
print(f"matplotlib    version : {matplotlib.__version__}")
print(f"seaborn       version : {seaborn.__version__}")
print(f"bs4           version : {bs4.__version__}")

"""
API
Application Programming Interface
- 창(윈도우) 생성 함수
- 버튼 생성 함수

클래스
- 구성 요소 : 메서드(함수) + 속성/필드(변수)
- 구성 요소 종류
    - 클래스 변수 / 클래스 메서드     : 인스턴스 생성 없이 사용 가능, cls
    - 인스턴스 변수 / 인스턴스 메서드 : 반드시 인스턴스 생성 해야만 사용 가능, self

객체/인스턴스
- 

오버라이딩 => 반드시 상속 관계
오버로딩   => 함수 이름 동일 & 매개변수 다르게 생성
상속       => class A(B, C, D): pass
- 다중 상속
"""
