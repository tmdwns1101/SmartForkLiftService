from services.Services import *
import time
import serial

ser = serial.Serial(port="COM12", baudrate=9600)
def main():

    print("초기화 실행")

    containerID = 1  #init 아이디 설정
    initService()

    ser.write("Init".encode())

    while True:
        if ser.readable():
            state = ser.readline()
            print(state.decode()[:len(state) - 1])
            if "Ready\r" == state.decode()[:len(state) - 1]:
                if isContainerEmpty()  == False :
                    curInfo = CashContainerDAO().getContainerInfo(containerID)  # 현재 컨테이너 정보
                    #컨테이너 아이디와 수량 데이터 전송(블루투스 연동)
                    curID = str(curInfo.getContainerID())
                    curQuantity = str(curInfo.getQuantity())
                    print("현재 ID", curInfo.getContainerID())
                    print("현재 수량", curInfo.getQuantity())

                    data = curID + '/' + curQuantity + '\n'
                    ser.write(data.encode())

                    nextQuantity = curInfo.getQuantity() - 1
                    time.sleep(1)

                    if nextQuantity == 0:
                        rs = updateZeroService(containerID)
                        if rs == False and CashContainerDAO().getContainerInfo(containerID).getQuantity() == 0:
                            containerID += 1
                    else:
                        CashContainerDAO().UpdateQuantity(nextQuantity, containerID)

                    #요청 신호 올때까지 대기
                    #input()
                else:
                    # 종료 메시지 전송
                    print("오늘 물량을 모두 처리하였습니다")
                    ser.write("end".encode())
                    ser.close()
                    break





if __name__ == "__main__":
    main()