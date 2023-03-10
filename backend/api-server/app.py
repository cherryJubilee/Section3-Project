from flask import Flask, request, redirect
import dbConnector
import pickle

app = Flask(__name__)

url = "http://hyewon-section3.s3-website.ap-northeast-2.amazonaws.com"


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


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
    return y_pred.tolist()[0]


@app.route('/survey/<data>', methods=['GET', 'POST'])
def submit_survey(data):
    answer = []
    for i in data[:8]:
        if i in ["1", "2", "3", "4", "5"]:  # answer선택지 검증 (1 ~ 5)
            answer.append(i)
    answer.append(data[8:])
    # try SQL Insert
    try:
        dbConnector.insertData(answer)
    except Exception as e:
        print(f'INSERT FAIL: {e}')

    # MBTI 예측
    try:
        mbti = predict_mbti(data[:8])
        print(f'mbti: {mbti}, type({type(mbti)})')
    except Exception as e:
        print(f'PREDICT FAIL: {e}')

    if mbti == 0:
        return redirect(f"{url}/0.html", code=301)
    elif mbti == 1:
        return redirect(f"{url}/1.html", code=301)
    elif mbti == 2:
        return redirect(f"{url}/2.html", code=301)
    elif mbti == 3:
        return redirect(f"{url}/3.html", code=301)
    else:
        return "TRY LATER", 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
