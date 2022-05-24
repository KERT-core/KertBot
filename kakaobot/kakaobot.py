from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time

application = Flask(__name__)

def isopen(self):
    """컬방이 열려있는지 알려줍니다."""
        
    circuit = 7
    cnt = 0
        
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(circuit, GPIO.OUT)
    GPIO.output(circuit, GPIO.LOW)
        
    time.sleep(0.1)
    GPIO.setup(circuit, GPIO.IN)
        
    while GPIO.input(circuit) == GPIO.LOW and cnt < 11000:
        cnt += 1
        
    if cnt < 10000:
        return True
    else:
        return False
            

@application.route("/animal")
def hello():
    return "Hello goorm!"

@application.route("/animal",methods=['POST'])
def animal():
    req = request.get_json()

    jodo = isopen()
    if jodo:
        answer = "열렸습니다"
    else:
        answer = "닫혔습니다"
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
    application.run(host='192.168.50.74', port=8520, threaded=True)