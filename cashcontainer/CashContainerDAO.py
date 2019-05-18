import pymysql
from util.DataBaseConn import DBAccessMerial
from cashcontainer.CashContainerVO import *

class CashContainerDAO:
    name = "MainContainerDAO"
    cashContainerVO = CashContainerVO(0, 0, 0)
    a = list()
    def __init__(self):
        self

    def getAllContainerInfo(self):
        sql = "select * from cashcontainer"
        host, user, password, db = DBAccessMerial()
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')

        try:
            curs = conn.cursor()
            curs.execute(sql)

            row = curs.fetchall()
            print(row)
            print(len(row))
            for i in range(0, len(row)):
                cashContainerVO = CashContainerVO(row[i][0], row[i][1], row[i][2])
                self.a.append(cashContainerVO)

            return self.a


        except Exception as e:
            print(e)
        finally:
            try:
                if conn.open is True:
                    # Connection 닫기
                    conn.close()
            except Exception as e:
                print(e)


    def getContainerInfo(self, containerID):
        sql = "select * from cashcontainer where containerID = %s"
        host, user, password, db = DBAccessMerial()
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
        try:
            curs = conn.cursor()
            curs.execute(sql, containerID)

            row = curs.fetchone()
            self.cashContainerVO.setContainerID(row[0])
            self.cashContainerVO.setContainerName(row[1])
            self.cashContainerVO.setQuantity(row[2])
            return self.cashContainerVO


        except Exception as e:
            print(e)
        finally:
            try:
                if conn.open is True:
                    # Connection 닫기
                    conn.close()
            except Exception as e:
                print(e)



    def UpdateQuantity(self, quantity, containerID):
        sql = "update cashcontainer set  quantity = %s where containerID = %s"
        host, user, password, db = DBAccessMerial()
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')

        try:
            curs = conn.cursor()
            curs.execute(sql, (quantity, containerID))
            conn.commit()
            print("(cashContainer) updateQuantity Success!")

        except Exception as e:
            print(e)
            print("DB 오류")
            return -1
        finally:
            try:
                if conn.open is True:
                    conn.close()
            except Exception as e:
                print(e)

    def getEmptyContainer(self):
        sql = "select * from cashcontainer where quantity = 0"
        host, user, password, db = DBAccessMerial()
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')

        try:
            curs = conn.cursor()
            curs.execute(sql)
            curs.execute(sql)

            row = curs.fetchall()

            return len(row)
        except Exception as e:
            print(e)
            print("DB 오류")
            return -1
        finally:
            try:
                if conn.open is True:
                    conn.close()
            except Exception as e:
                print(e)