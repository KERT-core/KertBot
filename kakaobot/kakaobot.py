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
    
    speakerON = "스피커 ON!"
    ls = "열어주세요"
    
    #입력받은걸 문자열로
    speaker = req["action"]["detailParams"]["IsOpen"]["origin"]
    if speaker == "열어주세요":
        answer = "열었습니다"
    else:
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
    application.run(host='0.0.0.0', port=5000, threaded=True)