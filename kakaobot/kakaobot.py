from flask import Flask, request, jsonify
import RPi.GPIO as GPIO
import time
import pygame

application = Flask(__name__)

def isopen():
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

def openplz():
    """컬방 안의 사람들이 문을 열어주도록 합니다."""
        
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
        pygame.mixer.music.play()
        return True
    else:
        return False

@application.route("/animal")
def hello():
    return "Hello goorm!"

@application.route("/animal",methods=['POST'])
def animal():
    req = request.get_json()
    usersaid = req["action"]["detailParams"]["IsOpen"]["origin"]

    if usersaid == "열렸나요":
        if isopen():
            answer = "열렸습니다"
        else:
            answer = "닫혔습니다"
    elif usersaid == "열어주세요":
        if openplz():
            answer = "컬방에 알림음을 울렸습니다."
        else:
            answer = "열어줄 사람이 없어요ㅠㅠ"

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