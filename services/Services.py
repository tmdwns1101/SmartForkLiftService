from maincontainer.MainContainerDAO import *
from maincontainer.MainContainerVO import *
from cashcontainer.CashContainerDAO import *
from cashcontainer.CashContainerVO import *
from datetime import datetime
from totalInfo.TotalInfoVO import *
from totalInfo.TotalInfoDAO import *

def initService():
    #현재 날짜에 맞게 메인 컨테이너 수량 초기화
    now = datetime.now()

    todayTotal = TotalInfoDAO().getAllTodayInfo(now.year, now.month, now.day)

    for i in range(0, len(todayTotal)):
        MainContainerDAO().UpdateQuantity(todayTotal[i].getQuantity(), todayTotal[i].getContainerID())





    cashContainerDAO = CashContainerDAO()
    result = cashContainerDAO.getAllContainerInfo()


    for i in range(0, len(result)):
        if result[i].getQuantity() == 0:
            updateZeroService(result[i].getContainerID())



#Cash컨테이너의 갯수가 0 개 일 때 호출 되는 함수
def updateZeroService(containerID):
    mainContainerDAO = MainContainerDAO()
    curID_total = mainContainerDAO.getContainerInfo(containerID).getQuantity()

    if curID_total > 3:
        CashContainerDAO().UpdateQuantity(3, containerID)
        mainContainerDAO.UpdateQuantity(curID_total - 3, containerID)
        return True
    else:
        CashContainerDAO().UpdateQuantity(curID_total, containerID)
        mainContainerDAO.UpdateQuantity(0, containerID)
        return False



#컨테이너가 모두 비였는지 체크
def isContainerEmpty():
    check1 = MainContainerDAO().getEmptyContainer()
    check2 = CashContainerDAO().getEmptyContainer()


    print("zero Main count :", check1)
    print("zero Cash count :", check2)



    if check1 == 3 and check2 == 3:
        return True
    else:
        return False

