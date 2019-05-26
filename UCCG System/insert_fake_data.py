from faker import Factory
import pymysql
import random
class Database_insert():
    # Fill in the information of your database server.
    __db_url = 'localhost'
    __db_username = 'root'
    __db_password = ''
    __db_name = 'test'
    __db = ''

    def __init__(self):
        """Connect to database when the object is created."""
        self.__db = self.db_connect()

    def __del__(self):
        """Disconnect from database when the object is destroyed."""
        self.__db.close()

    def db_connect(self):
        self.__db = pymysql.connect(self.__db_url, self.__db_username,
                                    self.__db_password, self.__db_name)
        return self.__db

    def insert_fake_user(self):
        cursor = self.__db.cursor()
        fake = Factory.create()
        stu_id = "1"+str(fake.pyint(min=0,max=8))+"300"+str(fake.pyint(min=10,max=99))+str(fake.pyint(min=100,max=999))
        email = fake.safe_email()
        phone_no = fake.phone_number()
        name = fake.name()
        password = fake.pystr(min_chars=3, max_chars=10)
        sql = """INSERT INTO USER(STUDENT_ID,EMAIL,PHONE_NO,USER_NAME,
        PASSWORD,SECURITY_QUESTION_1,SECURITY_ANSWER_1,
        SECURITY_QUESTION_2,SECURITY_ANSWER_2,AUTHORITY)
        VALUE(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s')""" % (int(stu_id),email,phone_no, name,password, "Q1", "A1",  "Q2", "A2", "0")
        try:
            cursor.execute(sql)
            print("user_insert_success")
            self.__db.commit()
        except:
            print("fail")
            self.__db.rollback()

    def insert_fake_player(self):
        cursor = self.__db.cursor()
        fake = Factory.create()
        stu_id = "1" + str(fake.pyint(min=0, max=8)) + "300" + str(fake.pyint(min=10, max=99)) + str(
            fake.pyint(min=100, max=999))
        name = fake.name()
        status = ['on Match' , 'free']
        player_status = random.choice(status)
        forbidden = [0,1]
        player_forbidden= random.choice(forbidden)
        sql="""INSERT INTO PLAYER(STUDENT_ID,PLAYER_NAME,STATUS,FORBIDDEN) VALUE (%d,'%s','%s',%d)""" % (int(stu_id),name,player_status,player_forbidden)
        try:
            cursor.execute(sql)
            print("player_insert_success")
            self.__db.commit()
        except:
            print("fail")
            self.__db.rollback()

    def insert_fake_team(self):
        cursor = self.__db.cursor()
        fake = Factory.create()
        team_name = fake.name_male()
        stu_id = "1" + str(fake.pyint(min=0, max=8)) + "300" + str(fake.pyint(min=10, max=99)) + str(
            fake.pyint(min=100, max=999))
        sql="""INSERT INTO TEAM(TEAM_NAME,CAPTAIN_ACCOUNT) VALUE('%s',%d)""" % (team_name,int(stu_id))
        try:
            cursor.execute(sql)
            print("team_insert_success")
            self.__db.commit()
        except:
            print("fail")
            self.__db.rollback()

    def insert_fake_belong(self):
        cursor = self.__db.cursor()
        fake = Factory.create()
        team_name = fake.name_male()
        stu_id = "1" + str(fake.pyint(min=0, max=8)) + "300" + str(fake.pyint(min=10, max=99)) + str(
            fake.pyint(min=100, max=999))
        team_id = str(fake.pyint(min=10, max=99))
        sql = """INSERT INTO belong(STUDENT_ID, TEAM_ID, POSITION) VALUE(%d, %d, '%s')""" % (int(stu_id), int(team_id), 'member' )
        try:
            cursor.execute(sql)
            print("team_insert_success")
            self.__db.commit()
        except:
            print("fail")
            self.__db.rollback()
sql =  Database_insert()
# h = 0
# while h < 50:
#     sql.insert_fake_belong()
#     h += 1
#
# sql =  Database_insert()
# i = 0
# while i < 8000:
#     sql.insert_fake_user()
#     i += 1
# j =0
# while j < 2000:
#     sql.insert_fake_player()
#     j+=1

k = 0
while k < 30000:
    sql.insert_fake_team()
    k+=1