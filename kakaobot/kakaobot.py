from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route("/animal")
def hello():
    return "Hello goorm!"

@application.route("/animal",methods=['POST'])
def animal():
    req = request.get_json()
    #조도 값이 200 이상이면 
    isOpen = "열렸습니다"
    #조도 값이 200 이하면
    isClose = "닫혔습니다"
    
    light = 100
    if light>=200:
        answer = isOpen
    else:
        answer = isClose
    # 답변 텍스트 설정
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer
                    }
                }
            ]
        }
    }

    # 답변 전송
    return jsonify(res)

if __name__ == "__main__":
    application.run(host='191.168.50.74', port=8520, threaded=True)