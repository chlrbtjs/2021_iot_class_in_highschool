from flask import Flask

app = Flask(__name__) #__name__ == 현재 파일 명

@app.route("/") #라우팅, ?
def hello():
    return '''
        <p>Hello, Flask!</p>
        <a href="/first">Go first</a>
        <a href="/second">Go second</a>
    '''
#html 코드로 반환, p는 문단의 약자, 문단을 나눌 때 사용 <p> 는 여는 태그 </p>는 닫는 태그
#<a>는 하이퍼링크

@app.route("/first")
def first():
    return '''
        <p>First Page</p>
        <a href="/">Go Home</a>
    '''
@app.route("/second")
def second():
    return '''
        <p>Second Page</p>
        <a href="/">Go Home</a>
    '''

if __name__ == "__main__": #터미널에서 실행된 경우
    app.run(host="0.0.0.0")
