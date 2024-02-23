"""
클래스 생성 (1)
- 구성 요소 : 속성 + 메서드 => 모두 없는 클래스
- 기본 상속 : Object ==> __속성명__, __메서드명__()
"""  # fmt: skip
class A:
    pass


"""
클래스 생성 (2)
- 구성 요소 : 속성 + 메서드 => 인스턴스 변수와 메서드
- 기본 상속 : Object ==> __속성명__, __메서드명__()
"""  # fmt: skip
class B:
    # 인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name) -> None:
        # self로 지정된 힙 메모리 주소에서부터 속성 저장
        self.num = num
        self.name = name

    # 인스턴스 메서드
    def printInfo(self):
        print(f"num  : {self.num}")
        print(f"name : {self.name}")

    # 연산자 맵핑 메서드 구현
    # 연산자 +와 맵핑된 메서드
    def __add__(self, other):
        print("__add__")
        return self.num + other.num

    def __sub__(self, other):
        return self.num - other.num


"""
클래스 생성 (3)
- 구성 요소 : 속성 + 메서드 => 인스턴스 변수와 메서드
- 기본 상속 : Object ==> __속성명__, __메서드명__()
"""  # fmt: skip
class C:
    # 클래스 변수 => C 클래스로 생성된 모든 인스턴스에서 공유
    #             => 인스턴스 생성 없이 사용 가능
    loc = "Daegu"

    # 인스턴스 객체 생성 및 속성 초기화 메서드
    def __init__(self, num, name) -> None:
        # self로 지정된 힙 메모리 주소에서부터 속성 저장
        self.num = num
        self.name = name

    # 인스턴스 메서드
    def printInfo(self):
        print(f"num  : {self.num}")
        print(f"name : {self.name}")


"""
클래스 생성 (4)
- 구성 요소 : 속성 + 메서드 => 클래스 변수와 메서드
- 기본 상속 : Object ==> __속성명__, __메서드명__()
"""  # fmt: skip
class DCalc:
    # 클래스 변수 => C 클래스로 생성된 모든 인스턴스에서 공유
    #             => 인스턴스 생성 없이 사용 가능
    name = "CASIO"

    # 클래스 메서드
    @classmethod
    def addNum(cls, a, b):
        print(cls)
        return a + b

    @classmethod
    def minuNum(cls, a, b):
        return a - b


"""
객체/인스턴스 생성
=> 생성 함수 : 클래스 이름()
=> A()
"""
a1 = A()
b1 = B(100, "BB")
b2 = B(30, "B2")
c1 = C(1000, "CCC")

"""
객체/인스턴스의 연산
"""
print("ABC" + "123")
print([1, 2, 3] + [10, 20, 30])
print("============>", b1 + b2)
print("============>", b1 - b2)

"""
객체/인스턴스의 속성/메서드
=> 사용 방법 : 객체/인스턴스 변수명.속성
=>             객체/인스턴스 변수명.메서드()
"""
print("A 인스턴스 a1의 속성과 메서드 =>", a1.__dict__)
print("A 인스턴스 a1의 속성과 메서드 =>", a1.__dir__())
print("A 클래스의 속성과 메서드 =>", A.__dict__)

print("-" * 100)

print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dict__)
print("B 인스턴스 b1의 속성과 메서드 =>", b1.__dir__())
print("B 클래스의 속성과 메서드 =>", B.__dict__)

print("-" * 100)

# 인스턴스 메서드 사용
c1.printInfo()

# 인스턴스 속성 사용
print(c1.name)

# 클래스 속성 사용
print("loc =>", C.loc, c1.loc)

# 인스턴스 메서드는 클래스명으로 사용 불가!!!
# C.printInfo()

print(f"DCalc.name : {DCalc.name}")
print("DCalc")
