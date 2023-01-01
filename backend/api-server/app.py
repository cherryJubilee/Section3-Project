from flask import Flask, request
import dbConnector
import pickle

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    return 'hello'


def predict_mbti(answer_data):
    model = None
    with open('temp/model.pkl', 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    X_test = [list(answer_data)]
    y_pred = model.predict(X_test)
    return y_pred


@app.route('/survey/<data>', methods=['GET', 'POST'])
def submit_survey(data):
    answer = []
    for i in data[:8]:
        if i in ["1", "2", "3", "4", "5"]:  # answer선택지 검증 (1 ~ 5)
            answer.append(i)
    answer.append(data[8:])
    print('1111')
    # try SQL Insert
    try:
        dbConnector.insertData(answer)
    except Exception as e:
        print(f'INSERT FAIL: {e}')
    print('2222')
    # MBTI 예측
    try:
        mbti = predict_mbti(data[:8])
        print(f'mbti: {mbti}')
    except Exception as e:
        print(f'PREDICT FAIL: {e}')
    return answer


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
