import pymysql
from util.DataBaseConn import DBAccessMerial
from totalInfo.TotalInfoVO import *

class TotalInfoDAO():
    name = "TotalInfoDAO"
    a = list()

    def __init__(self):
        self

    def getAllTodayInfo(self, year, month, day):
        sql = "select * from totalInfo where year = %s and month =%s and day = %s"
        host, user, password, db = DBAccessMerial()
        conn = pymysql.connect(host=host, user=user, password=password, db=db, charset='utf8')
        try:
            curs = conn.cursor()
            curs.execute(sql, (year, month, day))

            row = curs.fetchall()
            print("getAllTodayInfo", row)

            for i in range(0, len(row)):
                totalInfoVO = TotalInfoVO(row[i][0], row[i][1], row[i][2], row[i][3], row[i][4], row[i][5])
                self.a.append(totalInfoVO)

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
