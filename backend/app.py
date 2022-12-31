from flask import Flask, request
import dbConnector
import ml

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pass
    return 'hello'


@app.route('/survey/<data>', methods=['GET', 'POST'])
def submit_survey(data):
    answer = []
    for i in data[:8]:
        if i in ["1", "2", "3", "4", "5"]:
            answer.append(i)
    answer.append(data[8:])
    try:
        dbConnector.insertData(answer)
    except Exception as e:
        print(f'INSERT FAIL: {e}')
    return answer


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
