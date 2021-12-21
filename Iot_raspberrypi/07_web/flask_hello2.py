from flask import Flask, render_template

app = Flask(__name__) #__name__ == 현재 파일 명

@app.route("/") #라우팅, ?
def hello():
    return render_template("hello.html", title = "Hello, Flask") #불러올 문서 이름, 경로는 templates로 고정
#html 코드로 반환, p는 문단의 약자, 문단을 나눌 때 사용 <p> 는 여는 태그 </p>는 닫는 태그
#<a>는 하이퍼링크


@app.route("/first")
def first():
    # return render_template("first.html")

    return render_template(
        "first.html",)#html에 넘겨줄때 인자를 더 줄 수 있음, 


@app.route("/second")
def second():
    return render_template("second.html")


if __name__ == "__main__": #터미널에서 실행된 경우
    app.run(host="0.0.0.0")
