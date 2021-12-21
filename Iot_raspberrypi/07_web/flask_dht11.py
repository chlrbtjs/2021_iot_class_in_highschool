from flask import Flask, render_template
import Adafruit_DHT
import json

sensor = Adafruit_DHT.DHT11
PIN = 4

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)


# 라우팅을 위한 뷰 함수
@app.route("/")
def home():
    return render_template("dht11.html")


@app.route("/monitor")
def monitoring():
    try:
        h, t = Adafruit_DHT.read_retry(sensor, PIN)
        if h is not None and t is not None:
            obj = {'humidity': h, 'temperature': t} #json 형식, t : 값, t : 값 형식
            return json.dumps(obj) #객체를 문자열로 변환
        else:
            return 'Read error'
    except Exception as e:
        print(e)


# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        print("clean up")