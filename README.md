## 머신러닝

<details>
<summary>사용 교재</summary>

![](./images/핸즈온%20머신러닝.png)

</details>

### DAY01

---

<details>
<summary> 클래스 기초 </summary>

> 클래스 속성, 클래스 메서드
> 인스턴스 속성, 인스터스 메서드
> 오버라이딩, 오버로딩
> 상속

</details>
<details>
<summary> 머신러닝 기초 </summary>

> 머신러닝 소개
> 머신러닝용 라이브러리 소개
> 머신러닝 프로세스 설명
> 생선 분류

</details>

---

| 파일명                  | 내용                   |
| ----------------------- | ---------------------- |
| `DAY_01\check_pk.py`    | 설치 패키지 버전 확인  |
| `DAY_01\ex_class.py`    | 클래스 기초            |
| `DAY_01\ex_class_02.py` | 클래스 상속            |
| `DAY_01\ex_fish.ipynb`  | scikit-learn 생선 분류 |

### DAY02

---

<details>
<summary> K-Nearest Neighbor </summary>

> KNN을 사용한 생선 분류
> 학습용/테스트용 데이터 생성

</details>

---

| 파일명                             | 내용            |
| ---------------------------------- | --------------- |
| `DAY_02\ex_find_fish_knn.ipynb`    | 생선 분류 - KNN |
| `DAY_02\ex_sampling.ipynb`         | 판다스 sampling |
| `DAY_02\ex_find_fish_knn_02.ipynb` | 생선 분류 - KNN |
| `DAY_02\ex_find_fish_knn_03.ipynb` | 생선 분류 - KNN |

#### DAY02 실습과제

---

    1. Wine 품질 선별 모델

### DAY03

---

<details>
<summary> Scikit-Learn 전처리 </summary>

> 정규화
> 이산화/범주화
> 인코딩
> 선형회귀
> 과대적합, 과소적합, 최적적합

</details>

---

| 파일명                               | 내용                |
| ------------------------------------ | ------------------- |
| `DAY_03\ex_fish_regression.ipynb`    | LinearRegression    |
| `DAY_03\ex_fish_knnRegression.ipynb` | KNeighborsRegressor |

#### DAY03 실습과제

---

    1. 당뇨병 예측 모델 구현

### DAY04

---

<details>
<summary> 선형회귀 </summary>

> 이상치 데이터 처리
> Z-Score
> IQR

</details>
<details>
<summary> 다중회귀 </summary>

> 피쳐 스케일링
> StandardScaler
> MinMaxScaler
> RobustScaler

</details>
<details>
<summary> 특징 생성 </summary>

> 다항식 생성
> PolynomialFeatures

</details>

---

| 파일명                                  | 내용               |
| --------------------------------------- | ------------------ |
| `DAY_04\ex_outlier.ipynb`               | 이상치 데이터 처리 |
| `DAY_04\ex_multi_LinerRegression.ipynb` | 다중회귀           |
| `DAY_04\ex_poly_LinearRegression.ipynb` | 피쳐 추가 생성     |

#### DAY04 실습과제

---

    1. AutoMPG 연비 예측 모델 구현

### DAY05

---

<details>
<summary> 비선형 Regression </summary>

> LogisticRegression
> a, b 업데이트 최적화 기법

</details>
<details>
<summary> OVR, OVO 모듈 </summary>

> OneVsRestClassifier
> OneVsOneClassifier

</details>
<details>
<summary> 모델 성능 평가 </summary>

> accuracy_score
> precision_score
> f1_score
> recall_score
> confusion_matrix
> classification_report

</details>

---

| 파일명                                    | 내용                            |
| ----------------------------------------- | ------------------------------- |
| `DAY_05\ex_logistic_Regression.ipynb`     | 선형 모델 기반의 분류 모델 구현 |
| `DAY_05\ex_fish_logisticRegression.ipynb` | 생선 분류 모델 / 모델 성능 평가 |
| `DAY_05\ex_ovr.ipynb`                     | OVR 모듈 활용                   |

#### DAY05 실습과제

---

    1. Breast Cancer Wisconsin 종양 분류 모델 구현

### DAY06

---

<details>
<summary> 모델 성능 평가 </summary>

> accuracy_score
> precision_score
> f1_score
> recall_score
> confusion_matrix
> classification_report

</details>
<details>
<summary> 확률적경사하강법 </summary>

> SGDClassifier

</details>

---

| 파일명                                       | 내용                  |
| -------------------------------------------- | --------------------- |
| `DAY_06\ex_classification_performance.ipynb` | 분류 모델 성능지표    |
| `DAY_06\ex_sgd_regressor.ipynb`              | 미니배치기반 기계학습 |

#### DAY06 실습과제

---

    1. MNIST 이미지 이진 분류/다중 분류

### DAY07

---

<details>
<summary> 이미지 데이터 분류 </summary>

> MNIST

</details>
<details>
<summary> 규제, 정규화 </summary>

> Ridge
> Lasso

</details>

---

| 파일명                                 | 내용                             |
| -------------------------------------- | -------------------------------- |
| `DAY_07\ex_mnist_classification.ipynb` | MNIST 이미지 데이터 분류         |
| `DAY_07\ex_fish_ridge_lasso.ipynb`     | 가중치 값을 조절해 과대적합 해결 |
| `DAY_07\ex_kfold.ipynb`                | 교차 검증                        |
| `DAY_07\ex_cv_validation.ipynb`        | 교차 검증 단순화                 |

#### DAY07 실습과제

---

    1.
