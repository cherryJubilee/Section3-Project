from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, classification_report
from sklearn.ensemble import RandomForestClassifier
from scipy.stats import randint
from category_encoders import OrdinalEncoder
import pandas as pd
import pymysql

conn = pymysql.connect(
    host='db',
    port=3306,
    user='root',
    password='12345678',
    db='survey_proj'
)

full_scan_query = "SELECT * FROM survej_proj"

df = pd.read_sql_query(full_scan_query, conn, index_col=0)
conn.close()

target = 'answer_mbti'
features = df.drop(columns=target).columns
train, val = train_test_split(
    df, train_size=0.80, test_size=0.20, stratify=df[target], random_state=2)

X_train = train[features]
y_train = train[target]
X_val = val[features]
y_val = val[target]

"""Target = answer_mbti의 분포"""

# 타겟 데이터 범주의 비율을 확인합니다.
y_train.value_counts(normalize=True)

"""## 기준모델  
- 분류에서는 타겟의 최빈값 사용
"""

# 기준모델
train[target].value_counts(normalize=True).max()

# mode(): Return the highest frequency value in a Series.
major = y_train.mode()[0]

# 타겟 샘플 수 만큼 0이 담긴 리스트를 만듭니다. 기준모델로 타겟인 credit 값을 전부 0으로 찍는 모델이다.)
y_pred = [major] * len(y_train)

# 최다 클래스의 빈도가 정확도가 됩니다.
print("training accuracy: ", round(accuracy_score(y_train, y_pred), 2))


# 검증세트 에서도 정확도를 확인해 볼 수 있습니다.
y_val = val[target]
y_pred = [major] * len(y_val)
print("validation accuracy: ", accuracy_score(y_val, y_pred))
print(classification_report(y_val, y_pred))

"""## 1. RandomForest"""

# RandomForest 파이프라인

pipe = make_pipeline(OrdinalEncoder(),
                     RandomForestClassifier(random_state=42, class_weight='balanced', n_jobs=-1))

# RandomizedSearchCV를 이용해서 각 하이퍼 파라미터에 대해서 학습을 할 범위를 정해준다.
dists = {'randomforestclassifier__criterion': ['gini', 'entropy', 'log_loss'],
         # 몇개의 결정트리 모델을 만들어서 랜덤 포레스트 모델을 만들지 결정하는 하이퍼 파라미터이다.
         'randomforestclassifier__n_estimators': randint(50, 100),
         # 몇번의 분기를 거쳐서 분류하는 결정트리 모델을 만들 것인지 결정하는 하이퍼 파라미터이다.
         'randomforestclassifier__max_depth': [5, 10, 15, 20, None],
         'randomforestclassifier__min_samples_split': randint(10, 100),
         'randomforestclassifier__min_samples_leaf': randint(10, 100),
         'randomforestclassifier__max_features': ['sqrt', 'log2', None]
         }


# randomized Search CV 진행조건을 설정해준다.
clf = RandomizedSearchCV(
    pipe,  # 파이프라인으로 학습된 모델
    param_distributions=dists,  # 하이퍼파라미터 튜닝 값으로 진행한다.
    n_iter=10,  # 반복 횟수
    cv=3,  # 교차검증 횟수 (==> n_iter * cv 의 숫자만큼 진행됨)
    scoring='f1',  # 오차 평가방법
    verbose=1,  # 훈련 중지여부를 화면에 출력 (1= progress bar/2= one line per epoch)
    n_jobs=-1,  # 컴퓨터의 모든 가용 자원을 이용해서 학습을 진행하라는 코드이다.
)

# randomized Search CV로 train data 학습 진행
clf.fit(X_train, y_train)

print('최적 하이퍼파라미터: ', clf.best_params_)
print('accuracy: ', clf.best_score_)

# 만들어진 모델에서 가장 성능이 좋은 모델을 불러옵니다.
best_model_rf = clf.best_estimator_

y_pred_train = best_model_rf.predict(X_train)
y_pred_val = best_model_rf.predict(X_val)

print('훈련 정확도: ', accuracy_score(y_train, y_pred_train))
print('검증 정확도: ', accuracy_score(y_val, y_pred_val))
print(classification_report(y_val, y_pred_val))

# 새로운 데이터 한 샘플을 선택해 학습한 모델을 통해 예측해 봅니다
X_test = [[5, 1, 1, 1, 1, 1, 5, 1]]
y_pred = best_model_rf.predict(X_test)

print(y_pred)
