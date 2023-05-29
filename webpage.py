from flask import Flask
from predictNumber import predict
from flask import request
app = Flask(__name__)

@app.route('/predictNumber/', methods=['POST'])
def predict_number():
    image = request.form["image"]  # 非必须，本案例使用
    result = predict(image)
    return {
        "result": result
    }

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=5000)
