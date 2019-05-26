from flask import Flask, render_template,request, session, redirect, url_for, flash
from wtforms import Form,StringField,PasswordField,validators, SelectField, RadioField, TextField, SubmitField
import pymysql
from datetime import timedelta
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY']= "boy_next_door"
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(minutes=30)


# -------------------------------------------------------------------------------------------------------------------------------------------
# By Yu Jiahui and Li Donghua

class individualForm(Form):
    leader_id = TextField('Team Leader_id:', validators=[validators.required()])
    mail = TextField('E-mail:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    submit1 = SubmitField('submit',validators=[validators.required()])

class TeamForm5(Form):
    leader_id = TextField('Team Leader_id:', validators=[validators.required()])
    mail = TextField('E-mail:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    member1 = TextField('Student_id:', validators=[validators.required()])
    position1 = TextField('Position',validators=[validators.required()])
    member2 = TextField('Student_id:', validators=[validators.required()])
    position2 = TextField('Position',validators=[validators.required()])
    member3 = TextField('Student_id:', validators=[validators.required()])
    position3 = TextField('Position', validators=[validators.required()])
    member4 = TextField('Student_id:', validators=[validators.required()])
    position4 = TextField('Position', validators=[validators.required()])
    submit5 = SubmitField('submit',validators=[validators.required()])


class TeamForm6(Form):
    leader_id = TextField('Team Leader_id:', validators=[validators.required()])
    mail = TextField('E-mail:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    member1 = TextField('Student_id:', validators=[validators.required()])
    position1 = TextField('Position',validators=[validators.required()])
    member2 = TextField('Student_id:', validators=[validators.required()])
    position2 = TextField('Position',validators=[validators.required()])
    member3 = TextField('Student_id:', validators=[validators.required()])
    position3 = TextField('Position', validators=[validators.required()])
    member4 = TextField('Student_id:', validators=[validators.required()])
    position4 = TextField('Position', validators=[validators.required()])
    member5 = TextField('Student_id:', validators=[validators.required()])
    position5 = TextField('Position', validators=[validators.required()])
    submit6 = SubmitField('submit',validators=[validators.required()])


class TeamForm7(Form):
    leader_id = TextField('Team Leader_id:', validators=[validators.required()])
    mail = TextField('E-mail:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    member1 = TextField('Student_id:', validators=[validators.required()])
    position1 = TextField('Position',validators=[validators.required()])
    member2 = TextField('Student_id:', validators=[validators.required()])
    position2 = TextField('Position',validators=[validators.required()])
    member3 = TextField('Student_id:', validators=[validators.required()])
    position3 = TextField('Position', validators=[validators.required()])
    member4 = TextField('Student_id:', validators=[validators.required()])
    position4 = TextField('Position', validators=[validators.required()])
    member5 = TextField('Student_id:', validators=[validators.required()])
    position5 = TextField('Position', validators=[validators.required()])
    member6 = TextField('Student_id:', validators=[validators.required()])
    position6 = TextField('Position', validators=[validators.required()])
    submit7 = SubmitField('submit',validators=[validators.required()])


class TeamForm8(Form):
    leader_id = TextField('Team Leader_id:', validators=[validators.required()])
    mail = TextField('E-mail:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    member1 = TextField('Student_id:', validators=[validators.required()])
    position1 = TextField('Position',validators=[validators.required()])
    member2 = TextField('Student_id:', validators=[validators.required()])
    position2 = TextField('Position',validators=[validators.required()])
    member3 = TextField('Student_id:', validators=[validators.required()])
    position3 = TextField('Position', validators=[validators.required()])
    member4 = TextField('Student_id:', validators=[validators.required()])
    position4 = TextField('Position', validators=[validators.required()])
    member5 = TextField('Student_id:', validators=[validators.required()])
    position5 = TextField('Position', validators=[validators.required()])
    member6 = TextField('Student_id:', validators=[validators.required()])
    position6 = TextField('Position', validators=[validators.required()])
    member7 = TextField('Student_id:', validators=[validators.required()])
    position7 = TextField('Position', validators=[validators.required()])
    submit8 = SubmitField('submit',validators=[validators.required()])


class registerForm(Form):
    student_id = TextField('Student_id:', validators=[validators.required()])
    mail = TextField('Email:', validators=[validators.required(),validators.Length(min=6, max=35), validators.Regexp('^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', message = "Email form invalid")])
    username = TextField('Username', validators=[validators.required(), validators.Length(min=3, max=20)])
    password = TextField('Your Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    confirm = TextField('Confirm your Password:', validators=[validators.required(), validators.Length(min=3, max=35),validators.EqualTo("password")])
    questionL = [('1','Q1'),('2','Q2'),('3','Q3'),('4','Q4'),('5','Q5')]
    security1 = SelectField('Set your Security Question1:', choices=questionL, validators=[validators.required()],coerce=str)
    answer1 = StringField('Answer1:', validators=[validators.required()])
    security2 = SelectField('Set your Security Question2:', choices=questionL, validators=[validators.required()],coerce=str)
    answer2 = TextField('Answer2:', validators=[validators.required()])
    pnumber = TextField('Your Phone Number:', validators=[validators.required()])


class LostAccountForm(Form):
    student_id = TextField('Student_id:', validators=[validators.required()])
    sanswer1 = TextField('Answer1:', validators=[validators.required()])
    sanswer2 = TextField('Answer2:', validators=[validators.required()])
    phone = TextField('Your Phone number:', validators=[validators.required()])


class ResetForm(Form):
    password = TextField('Your Password:',validators=[validators.required(), validators.Length(min=3, max=35)])
    confirm = TextField('Confirm your Password:', validators=[validators.required(),validators.EqualTo("password")])

# ----------------------------------------------------------------------------------------------------------------------------------------------
# By He Langxuan and Li Junjiang


class DatabaseOperations:
    # Fill in the information of your database server.
    __db_url = '172.16.199.106'
    __db_username = '1730026028'
    __db_password = '88888888'
    __db_name = '1730026028'
    __db = ''
    # __db_url = 'localhost'
    # __db_username = 'root'
    # __db_password = ''
    # __db_name = 'test'
    # __db = ''

    def __init__(self):
        """Connect to database when the object is created."""
        self.__db = self.db_connect()

    def __del__(self):
        """Disconnect from database when the object is destroyed."""
        self.__db.close()

    def db_connect(self):
        self.__db = pymysql.connect(self.__db_url, self.__db_username, self.__db_password, self.__db_name)
        return self.__db

    def find_event(self):
        cursor = self.__db.cursor()
        sql_find = """SELECT DISTINCT GAME_ID ,GAME_NAME,GAME_TYPE,GAME_CONDITION,MAX_NUM,GAME_LIMIT 
                        FROM GAME 
                        ORDER BY GAME_CONDITION"""
        try:
            cursor.execute(sql_find)
            result = cursor.fetchall()
            return result
        except:
            pass

    def check_condition(self, game_id):
        cursor = self.__db.cursor()
        sql_check = """SELECT GAME_CONDITION FROM GAME WHERE GAME_ID = %d""" % (game_id)
        try:
            cursor.execute(sql_check)
            result = cursor.fetchone()
            for row in result:
                game_condition = row
            if (game_condition == 'onMatching'):
                return 1
            else:
                return 0
        except:
            self.__db.close()


    def change_condition(self, game_condition, game_id):
        cursor = self.__db.cursor()
        if (game_condition == 'start'):
            count_participate = self.count_participant(game_id)
            count = (count_participate[0])[1]
            can_start = False
            if self.check_game_type(game_id) == 1:
                if count <= 5:
                    sql_check_history = """SELECT * FROM HISTORY WHERE GAME_ID = %d""" %(game_id)
                    try:
                        cursor.execute(sql_check_history)
                        history = cursor.fetchall()
                        if history:
                            can_start = True
                    except:
                        pass
                elif count > 5:
                    can_start = True
            elif self.check_game_type(game_id) == 2:
                if count > 1:
                    can_start = True
            if can_start:
                sql_change = """UPDATE GAME SET GAME_CONDITION = 'onMatching' 
                WHERE GAME_ID = %d AND (GAME_CONDITION = 'Available')""" % (game_id)
                try:
                    cursor.execute(sql_change)
                    self.__db.commit()
                except:
                    self.__db.rollback()

            else:
                return "fail"
        elif (game_condition == 'endit'):
            sql_change = """UPDATE GAME SET GAME_CONDITION = 'Stopped' 
            WHERE GAME_ID = %d AND (GAME_CONDITION = 'onMatching' OR GAME_CONDITION = 'Available' )""" % (game_id)
            try:
                cursor.execute(sql_change)
                self.__db.commit()
            except:
                self.__db.rollback()

        elif (game_condition == 'reset'):
            sql_change = """UPDATE GAME SET GAME_CONDITION = 'Available' 
            WHERE GAME_ID = %d """ % (game_id)
            try:
                cursor.execute(sql_change)
                self.__db.commit()
            except:
                self.__db.rollback()


    def check_participate(self,game_id):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        if game_limit == 1:
            sql_check = """SELECT TEAM_ID FROM PARTICIPATE WHERE GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                return result
            except:
                pass

        elif game_limit == 2:
            sql_check = """SELECT STUDENT_ID FROM PARTICIPATE_INDIVIDUAL WHERE GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                return result
            except:
                pass

    def delete_event(self, game_name):
        cursor = self.__db.cursor()
        sql_exist = """SELECT GAME_ID FROM GAME WHERE GAME_NAME = '%s'""" % (game_name)
        try:
            cursor.execute(sql_exist)
            result = cursor.fetchall()
            if (result):
                sql_check_condition = """SELECT GAME_CONDITION FROM GAME WHERE GAME_NAME = '%s'""" % (game_name)
                try:
                    cursor.execute(sql_check_condition)
                    condition_result = cursor.fetchall()
                    condition = (condition_result[0])[0]
                    if (condition != 'onMatching'):
                        game_id = (result[0])[0]
                        game_limit = self.check_game_limit(game_id)
                        try:
                            check_arr = self.view_arrange(game_id)
                            check_sco = self.view_score(game_id)
                            check_par = self.check_participate(game_id)
                            if game_limit == 1:
                                if check_sco:
                                    sql_delete_score_team = """DELETE FROM MATCH_SCORE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_score_team)
                                        self.__db.commit()
                                    except:
                                        pass
                                if check_arr:
                                    sql_delete_arr_team = """DELETE FROM MATCH_ARRANGE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_arr_team)
                                        self.__db.commit()
                                    except:
                                        pass
                                if check_par:
                                    sql_delete_participate = """DELETE FROM PARTICIPATE WHERE GAME_ID = %d""" % (
                                        game_id)
                                    try:
                                        cursor.execute(sql_delete_participate)
                                        self.__db.commit()
                                    except:
                                        pass
                            elif game_limit == 2:
                                if check_sco:
                                    sql_delete_score_team = """DELETE FROM MATCH_SCORE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_score_team)
                                        self.__db.commit()
                                    except:
                                        pass
                                if check_arr:
                                    sql_delete_arr_team = """DELETE FROM MATCH_ARRANGE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_arr_team)
                                        self.__db.commit()
                                    except:
                                        pass
                                if check_par:
                                    sql_delete_participate = """DELETE FROM PARTICIPATE_INDIVIDUAL WHERE GAME_ID = %d""" % (
                                        game_id)
                                    try:
                                        cursor.execute(sql_delete_participate)
                                        self.__db.commit()
                                    except:
                                        pass
                            sql_delete_game = """DELETE FROM GAME WHERE GAME_NAME= '%s'""" % (game_name)
                            cursor.execute(sql_delete_game)
                            self.__db.commit()
                            return "success"
                        except:
                            self.__db.rollback()
                    else:
                        return "fail"
                except:
                    pass
            else:
                return "notfound"
        except:
            pass


    def find_event_name(self, game_id):
        cursor = self.__db.cursor()
        sql_find = """SELECT GAME_NAME FROM GAME WHERE GAME_ID = %d""" % (game_id)
        try:
            cursor.execute(sql_find)
            result = cursor.fetchall()
            for row in result:
                game_name = row[0]
            return game_name
        except:
            pass


    def find_event_game_round(self,game_id):
        cursor = self.__db.cursor()
        sql_find = """SELECT GAME_ROUND FROM GAME WHERE GAME_ID = %d""" % (game_id)
        try:
            cursor.execute(sql_find)
            result = cursor.fetchall()
            for row in result:
                game_round = row[0]
            return game_round
        except:
            pass


    def count_participant(self, game_id):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        if (game_limit == 1):
            sql_count = """SELECT GAME_ID ,COUNT(TEAM_ID) FROM PARTICIPATE WHERE GAME_ID = %d
    GROUP BY GAME_ID """ % (game_id)
        elif (game_limit == 2):
            sql_count = """SELECT GAME_ID,COUNT(STUDENT_ID) FROM PARTICIPATE_INDIVIDUAL WHERE GAME_ID = %d 
            GROUP BY GAME_ID""" % (game_id)
        try:
            cursor.execute(sql_count)
            result = cursor.fetchall()
            if (result):
                return result
            else:
                return ((game_id, 0),)
        except:
            pass


    def check_game_limit(self,game_id):
        cursor = self.__db.cursor()
        sql_check = """SELECT GAME_LIMIT FROM GAME WHERE GAME_ID = %d"""  % (game_id)
        try:
            cursor.execute(sql_check)
            result = cursor.fetchall()
            if((result[0])[0]=='team'):
                return 1
            else:
                return 2
        except:
            pass


    def check_game_type(self, game_id):
        cursor = self.__db.cursor()
        sql_check = """SELECT GAME_TYPE FROM GAME WHERE GAME_ID = %d""" % (game_id)
        try:
            cursor.execute(sql_check)
            result = cursor.fetchall()
            if((result[0])[0] == 'knock'):
                return 1
            else:
                return 2
        except:
            pass


    def knock_method(self, result):
        i = 0
        match_team_pair_knock = []
        if (len(result) % 2 == 0):
            while i < len(result):
                row_one = result[i]
                row_two = result[i + 1]
                match_team_pair_knock.append([row_one[0], row_one[1], row_two[0], row_two[1], row_one[2]])
                i += 2
            return match_team_pair_knock
        else:
            while i < (len(result) - 1):
                row_one = result[i]
                row_two = result[i + 1]
                match_team_pair_knock.append([row_one[0], row_one[1], row_two[0], row_two[1], row_one[2]])
                i += 2
            match_team_pair_knock.append([(result[len(result) - 1])[0], (result[len(result) - 1])[1], None, None,
                                          (result[len(result) - 1])[2]])
            return match_team_pair_knock

    def round_method(self, result):
        j = 0
        match_team_pair_round = []
        while j < len(result):
            row = result[j]
            k = j + 1
            while k < len(result):
                each = result[k]
                match_team_pair_round.append([row[0], row[1], each[0], each[1], row[2]])
                k += 1
            j += 1

        return match_team_pair_round

    def get_team_pair(self, game_id):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        game_type = self.check_game_type(game_id)
        if(game_limit == 1):
            sql_team = """SELECT PARTICIPATE.TEAM_ID, TEAM.TEAM_NAME, PARTICIPATE.GAME_ID FROM PARTICIPATE NATURAL JOIN TEAM 
                WHERE PARTICIPATE.GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_team)
                result = cursor.fetchall()
                if(game_type == 1):
                    result_arr_knock = self.knock_method(result)
                    return result_arr_knock
                elif(game_type == 2):
                    result_arr_round = self.round_method(result)
                    return result_arr_round
            except:
                pass


        elif(game_limit == 2):
            sql_player = """SELECT PARTICIPATE_INDIVIDUAL.STUDENT_ID,PLAYER.PLAYER_NAME,PARTICIPATE_INDIVIDUAL.GAME_ID 
            FROM PARTICIPATE_INDIVIDUAL NATURAL JOIN PLAYER
            WHERE GAME_ID = %d"""%(game_id)
            try:
                cursor.execute(sql_player)
                result = cursor.fetchall()
                if (game_type == 1):
                    result_arr_knock = self.knock_method(result)
                    return result_arr_knock
                elif (game_type == 2):
                    result_arr_round = self.round_method(result)
                    return result_arr_round
            except:
                pass


    def upload_arrange(self, id_one, id_two, game_id, date):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if(game_limit == 1):
            sql_check = """SELECT * FROM MATCH_ARRANGE 
                WHERE TEAM_ID_ONE = %d AND TEAM_ID_TWO = %d AND GAME_ID = %d""" % (id_one, id_two, game_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                if (result):
                    sql_update = """UPDATE MATCH_ARRANGE SET ARR_TIME = '%s' 
                        WHERE TEAM_ID_ONE = %d AND TEAM_ID_TWO = %d AND GAME_ID = %d""" % (
                        date, id_one, id_two, game_id)
                    try:
                        cursor.execute(sql_update)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
                else:
                    sql_insert = """INSERT INTO MATCH_ARRANGE(TEAM_ID_ONE,TEAM_ID_TWO,GAME_ID, ARR_TIME) 
                        VALUE(%d,%d,%d,'%s') """ % (id_one, id_two, game_id, date)
                    try:
                        cursor.execute(sql_insert)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
            except:
                pass

        elif(game_limit == 2):
            sql_check = """SELECT * FROM MATCH_ARRANGE_INDIVIDUAL 
            WHERE STUDENT_ID_ONE = %d AND STUDENT_ID_TWO = %d AND GAME_ID = %d
                        """ % (id_one, id_two, game_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                if (result):
                    sql_update = """UPDATE MATCH_ARRANGE_INDIVIDUAL SET ARR_TIME = '%s' 
                        WHERE STUDENT_ID_ONE = %d AND STUDENT_ID_TWO = %d AND GAME_ID = %d""" % (
                        date, id_one, id_two, game_id)
                    try:
                        cursor.execute(sql_update)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
                else:
                    sql_insert = """INSERT INTO MATCH_ARRANGE_INDIVIDUAL(STUDENT_ID_ONE,STUDENT_ID_TWO,GAME_ID, ARR_TIME)
                        VALUE(%d,%d,%d,'%s') """ % (id_one, id_two, game_id, date)
                    try:
                        cursor.execute(sql_insert)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
            except:
                pass


    def view_arrange(self, game_id):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if(game_limit == 1):
            sql_view = """SELECT T1.TEAM_ID, T1.TEAM_NAME,T2.TEAM_ID,T2.TEAM_NAME,ARR_TIME
            FROM MATCH_ARRANGE, TEAM as T1 ,TEAM as T2 
            WHERE T1.TEAM_ID = TEAM_ID_ONE AND T2.TEAM_ID =TEAM_ID_TWO AND GAME_ID= %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass

        elif(game_limit == 2):
            sql_view = """SELECT T1.STUDENT_ID,T1.PLAYER_NAME,T2.STUDENT_ID,T2.PLAYER_NAME,ARR_TIME
            FROM  PLAYER  AS T1 ,PLAYER AS T2, MATCH_ARRANGE_INDIVIDUAL
            WHERE T1.STUDENT_ID = STUDENT_ID_ONE AND T2.STUDENT_ID = STUDENT_ID_TWO AND GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass


    def view_bye(self, game_id):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if (game_limit == 1):
            sql_view = """SELECT DISTINCT T1.TEAM_ID, T1.TEAM_NAME,MATCH_ARRANGE.GAME_ID
                    FROM MATCH_ARRANGE, TEAM as T1
                    WHERE T1.TEAM_ID = TEAM_ID_ONE AND TEAM_ID_TWO = 0 AND ARR_TIME = 0 AND GAME_ID= %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass

        elif(game_limit == 2):
            sql_view = """SELECT T1.STUDENT_ID,T1.PLAYER_NAME,MATCH_ARRANGE_INDIVIDUAL.GAME_ID
                        FROM  PLAYER  AS T1 , MATCH_ARRANGE_INDIVIDUAL
                        WHERE T1.STUDENT_ID = STUDENT_ID_ONE AND STUDENT_ID_TWO =0 AND ARR_TIME =0 AND GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass


    def find_match_id(self, team_one_id, team_two_id, game_id):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if(game_limit == 1):
            sql_find = """SELECT MATCH_ID FROM MATCH_ARRANGE 
            WHERE TEAM_ID_ONE = %d AND TEAM_ID_TWO = %d AND GAME_ID = %d""" % (team_one_id, team_two_id, game_id)
            try:
                cursor.execute(sql_find)
                result = cursor.fetchall()
                match_id = (result[0])[0]
                return match_id
            except:
                pass

        elif(game_limit == 2):
            sql_find = """SELECT MATCH_ID FROM MATCH_ARRANGE_INDIVIDUAL 
                       WHERE STUDENT_ID_ONE = %d AND STUDENT_ID_TWO = %d AND GAME_ID = %d""" % (
                team_one_id, team_two_id, game_id)
            try:
                cursor.execute(sql_find)
                result = cursor.fetchall()
                match_id = (result[0])[0]
                return match_id
            except:
                pass


    def upload_score(self, match_id, game_id, one_score, two_score):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if(game_limit == 1):
            sql_check = """SELECT * FROM MATCH_SCORE WHERE MATCH_ID = %d""" % (match_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                if (result):
                    sql_update = """UPDATE MATCH_SCORE SET TEAM_ONE_SCORE = %d, TEAM_TWO_SCORE = %d
                                    WHERE MATCH_ID= %d """ % (one_score,two_score,match_id)
                    try:
                        cursor.execute(sql_update)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
                else:
                    sql_insert = """INSERT INTO MATCH_SCORE(MATCH_ID,GAME_ID,TEAM_ONE_SCORE,TEAM_TWO_SCORE) 
                    VALUE(%d,%d,%d,%d)""" % (match_id,game_id,one_score,two_score)
                    try:
                        cursor.execute(sql_insert)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
            except:
                pass

        elif(game_limit ==2):
            sql_check = """SELECT * FROM MATCH_SCORE_INDIVIDUAL WHERE MATCH_ID = %d""" % (match_id)
            try:
                cursor.execute(sql_check)
                result = cursor.fetchall()
                if (result):
                    sql_update = """UPDATE MATCH_SCORE_INDIVIDUAL SET PLAYER_ONE_SCORE = %d, PLAYER_TWO_SCORE = %d
                                                WHERE MATCH_ID= %d """ % (one_score, two_score, match_id)
                    try:
                        cursor.execute(sql_update)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
                else:
                    sql_insert = """INSERT INTO MATCH_SCORE_INDIVIDUAL(MATCH_ID,GAME_ID,PLAYER_ONE_SCORE,PLAYER_TWO_SCORE) 
                                VALUE(%d,%d,%d,%d)""" % (match_id, game_id, one_score, two_score)
                    try:
                        cursor.execute(sql_insert)
                        self.__db.commit()
                    except:
                        self.__db.rollback()
            except:
                pass


    def view_score(self, game_id):
        game_limit = self.check_game_limit(game_id)
        cursor = self.__db.cursor()
        if(game_limit == 1):
            sql_view = """SELECT T1.TEAM_ID, T1.TEAM_NAME,T2.TEAM_ID,T2.TEAM_NAME,TEAM_ONE_SCORE,TEAM_TWO_SCORE,ARR_TIME
            FROM MATCH_ARRANGE, TEAM as T1 ,TEAM as T2 ,MATCH_SCORE
            WHERE T1.TEAM_ID = TEAM_ID_ONE 
            AND T2.TEAM_ID =TEAM_ID_TWO 
            AND MATCH_ARRANGE.MATCH_ID = MATCH_SCORE.MATCH_ID AND MATCH_SCORE.GAME_ID= %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass

        elif(game_limit == 2):
            sql_view = """SELECT T1.STUDENT_ID, T1.PLAYER_NAME,T2.STUDENT_ID,T2.PLAYER_NAME,PLAYER_ONE_SCORE,PLAYER_TWO_SCORE,ARR_TIME
                        FROM MATCH_ARRANGE_INDIVIDUAL, PLAYER as T1 ,PLAYER as T2 ,MATCH_SCORE_INDIVIDUAL
                        WHERE T1.STUDENT_ID = STUDENT_ID_ONE 
                        AND T2.STUDENT_ID =STUDENT_ID_TWO AND MATCH_ARRANGE_INDIVIDUAL.MATCH_ID = MATCH_SCORE_INDIVIDUAL.MATCH_ID 
                        AND MATCH_SCORE_INDIVIDUAL.GAME_ID= %d""" % (game_id)
            try:
                cursor.execute(sql_view)
                result = cursor.fetchall()
                return result
            except:
                pass


    def if_match_isdone(self,game_id):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        if game_limit == 1:
            sql_bye = """SELECT * FROM MATCH_ARRANGE WHERE GAME_ID = %d AND TEAM_ID_TWO = 0 AND ARR_TIME = 0""" % (game_id)
            sql_count_arr = """SELECT GAME_ID,COUNT(GAME_ID) 
            FROM MATCH_ARRANGE 
            WHERE GAME_ID = %d GROUP BY GAME_ID""" % (game_id)
            sql_count_sco = """SELECT GAME_ID,COUNT(GAME_ID) 
            FROM MATCH_SCORE 
            WHERE GAME_ID = %d GROUP BY GAME_ID""" % (game_id)
        elif game_limit == 2:
            sql_bye = """SELECT * FROM MATCH_ARRANGE_INDIVIDUAL WHERE GAME_ID = %d AND STUDENT_ID_TWO = 0 AND ARR_TIME = 0""" % (
                game_id)
            sql_count_arr = """SELECT GAME_ID,COUNT(GAME_ID) 
                        FROM MATCH_ARRANGE_INDIVIDUAL 
                        WHERE GAME_ID = %d GROUP BY GAME_ID""" % (game_id)
            sql_count_sco = """SELECT GAME_ID,COUNT(GAME_ID) 
                        FROM MATCH_SCORE_INDIVIDUAL 
                        WHERE GAME_ID = %d GROUP BY GAME_ID""" % (game_id)
        try:
            cursor.execute(sql_bye)
            result = cursor.fetchall()
            if result:
                bye_num = 1
            else :
                bye_num = 0
            cursor.execute(sql_count_arr)
            result_arr = cursor.fetchall()
            if result_arr:
                arr_num = (result_arr[0])[1]
            else:
                arr_num = 0
            cursor.execute(sql_count_sco)
            result_sco = cursor.fetchall()
            if result_sco:
                actual_num = (result_sco[0])[1]
            else:
                actual_num = 0
            if arr_num-bye_num > actual_num:
                self.__db.close()
                return 0
            elif arr_num-bye_num == actual_num:
                self.__db.close()
                return 1
            else:
                self.__db.close()
                return -1
        except:
            pass


    def pick_next_round(self,game_id):
        winner = []
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        if game_limit == 1:
            sql_winner_left = """SELECT T1.TEAM_ID,T1.TEAM_NAME,MATCH_SCORE.GAME_ID
                        FROM MATCH_ARRANGE, TEAM as T1 ,TEAM as T2 ,MATCH_SCORE
                        WHERE T1.TEAM_ID = TEAM_ID_ONE 
                        AND T2.TEAM_ID =TEAM_ID_TWO 
                        AND MATCH_ARRANGE.MATCH_ID = MATCH_SCORE.MATCH_ID 
                        AND TEAM_ONE_SCORE > TEAM_TWO_SCORE 
                        AND MATCH_SCORE.GAME_ID= %d""" % (game_id)
            sql_winner_right = """SELECT T2.TEAM_ID,T2.TEAM_NAME,MATCH_SCORE.GAME_ID
                                FROM MATCH_ARRANGE, TEAM as T1 ,TEAM as T2 ,MATCH_SCORE
                                WHERE T1.TEAM_ID = TEAM_ID_ONE 
                                AND T2.TEAM_ID =TEAM_ID_TWO 
                                AND MATCH_ARRANGE.MATCH_ID = MATCH_SCORE.MATCH_ID 
                                AND TEAM_ONE_SCORE < TEAM_TWO_SCORE 
                                AND MATCH_SCORE.GAME_ID= %d""" % (game_id)
        elif game_limit == 2:
            sql_winner_left = """SELECT T1.STUDENT_ID,T1.PLAYER_NAME,MATCH_SCORE_INDIVIDUAL.GAME_ID
                                    FROM MATCH_ARRANGE_INDIVIDUAL, PLAYER as T1 ,PLAYER as T2 ,MATCH_SCORE_INDIVIDUAL
                                    WHERE T1.STUDENT_ID = STUDENT_ID_ONE 
                                    AND T2.STUDENT_ID =STUDENT_ID_TWO 
                                    AND MATCH_ARRANGE_INDIVIDUAL.MATCH_ID = MATCH_SCORE_INDIVIDUAL.MATCH_ID 
                                    AND PLAYER_ONE_SCORE > PLAYER_TWO_SCORE 
                                    AND MATCH_SCORE_INDIVIDUAL.GAME_ID= %d""" % (game_id)
            sql_winner_right = """SELECT T2.STUDENT_ID,T2.PLAYER_NAME,MATCH_SCORE_INDIVIDUAL.GAME_ID
                                            FROM MATCH_ARRANGE_INDIVIDUAL, PLAYER as T1 ,PLAYER as T2 ,MATCH_SCORE_INDIVIDUAL
                                            WHERE T1.STUDENT_ID = STUDENT_ID_ONE 
                                            AND T2.STUDENT_ID =STUDENT_ID_TWO 
                                            AND MATCH_ARRANGE_INDIVIDUAL.MATCH_ID = MATCH_SCORE_INDIVIDUAL.MATCH_ID 
                                            AND PLAYER_ONE_SCORE < PLAYER_TWO_SCORE 
                                            AND MATCH_SCORE_INDIVIDUAL.GAME_ID= %d""" % (game_id)
        try:
            cursor.execute(sql_winner_left)
            result_left = cursor.fetchall()
            for each in result_left:
                winner.append(each)
            cursor.execute(sql_winner_right)
            result_right = cursor.fetchall()
            for each in result_right:
                winner.append(each)
            bye = self.view_bye(game_id)
            if bye:
                winner.append(bye[0])
            return winner
        except:
            pass


    def upload_history(self,game_id):
        cursor = self.__db.cursor()
        round_num = self.find_event_game_round(game_id)
        sql_get_scores = self.view_score(game_id)
        data = []
        for each in sql_get_scores:
            data.append((game_id, round_num, each[0], each[2], each[4], each[5]))
        sql_check_exist = """SELECT * FROM HISTORY 
        WHERE GAME_ID = %d AND GAME_ROUND= %d 
        AND PARTICIPANT_ONE_ID = %d AND PARTICIPANT_TWO_ID= %d 
        AND PARTICIPANT_ONE_SCORE = %d AND PARTICIPANT_TWO_SCORE = %d"""
        try:
            for each in data:
                cursor.execute(sql_check_exist % each)
                if cursor.fetchall():
                    return "fail"
        except:
            pass
        sql_insert = """INSERT INTO HISTORY(GAME_ID,GAME_ROUND,PARTICIPANT_ONE_ID,PARTICIPANT_TWO_ID,PARTICIPANT_ONE_SCORE,PARTICIPANT_TWO_SCORE)
        VALUES(%d,%d,%d,%d,%d,%d)"""
        try:
            for each in data:
                cursor.execute(sql_insert % each)
            self.__db.commit()
            return "success"
        except:
            self.__db.rollback()


    def upload_event(self, type, game_name,max_num,limit):
        date = datetime.now()
        date_str = date.strftime("%Y-%m-%d")
        cursor = self.__db.cursor()
        sql_find = """SELECT GAME_NAME FROM GAME WHERE GAME_NAME = '%s'""" % (game_name)
        try:
            cursor.execute(sql_find)
            result = cursor.fetchall()
            if (result):
                return 0
        except:
            pass
        if type == 'knock':
            round_num = 1
        elif type == 'round':
            round_num = -1
        sql = """INSERT INTO GAME (GAME_NAME,GAME_TYPE,GAME_DATE,GAME_CONDITION,MAX_NUM,GAME_LIMIT,GAME_ROUND) VALUE('%s','%s','%s','%s',%d,'%s',%d)""" % (
            game_name, type, date_str, 'Available', max_num, limit, round_num)
        try:
            cursor.execute(sql)
            self.__db.commit()
            return 1
        except:
            self.__db.rollback()
            return 0


    def generate_next_round(self,game_id):
        cursor = self.__db.cursor()
        upload_result = self.upload_history(game_id)
        if upload_result == "success":
            sql_next = """UPDATE GAME SET GAME_ROUND = GAME_ROUND+1 WHERE GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_next)
                self.__db.commit()
                next_round_team_pair = self.next_round_team_pair(game_id)
                return next_round_team_pair
            except:
                pass

        else:
            return "Fail"

    def pick_participants(self,game_id):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        if game_limit == 1:
            sql_pick = """SELECT TEAM_ID,TEAM_NAME,GAME_ID FROM PARTICIPATE NATURAL JOIN TEAM 
            WHERE GAME_ID = %d""" % (game_id)
        elif game_limit == 2:
            sql_pick = """ SELECT STUDENT_ID,PLAYER_NAME,GAME_ID FROM PARTICIPATE_INDIVIDUAL NATURAL JOIN PLAYER
            WHERE GAME_ID = %d""" % (game_id)
        try :
            cursor.execute(sql_pick)
            result = cursor.fetchall()
            return result
        except:
            pass


    def clear_the_old_record(self,game_id,looser):
        cursor = self.__db.cursor()
        game_limit = self.check_game_limit(game_id)
        team_ids = []
        if game_limit == 1:
            sql_delete_score ="""DELETE FROM MATCH_SCORE WHERE GAME_ID = %d""" %(game_id)
            try:
                cursor.execute(sql_delete_score)
                self.__db.commit()
            except:
                self.__db.rollback()
            sql_delete_time = """DELETE FROM MATCH_ARRANGE WHERE GAME_ID = %d""" %(game_id)
            try:
                cursor.execute(sql_delete_time)
                self.__db.commit()
            except:
                self.__db.rollback()
            sql_delete_team = """DELETE FROM PARTICIPATE WHERE TEAM_ID = %d"""
            for each in looser:
                team_ids.append(each[0])
            for each in team_ids:
                try:
                    cursor.execute(sql_delete_team % each)
                    self.__db.commit()
                except:
                    self.__db.rollback()
            self.__db.close()
        elif game_limit == 2:
            sql_delete_score = """DELETE FROM MATCH_SCORE_INDIVIDUAL WHERE GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_delete_score)
                self.__db.commit()
            except:
                self.__db.rollback()
            sql_delete_time = """DELETE FROM MATCH_ARRANGE_INDIVIDUAL WHERE GAME_ID = %d""" % (game_id)
            try:
                cursor.execute(sql_delete_time)
                self.__db.commit()
            except:
                self.__db.rollback()
            sql_delete_team = """DELETE FROM PARTICIPATE_INDIVIDUAL WHERE STUDENT_ID = %d"""
            for each in looser:
                team_ids.append(each[0])
            for each in team_ids:
                try:
                    cursor.execute(sql_delete_team % each)
                    self.__db.commit()
                except:
                    self.__db.rollback()

            self.__db.close()

    def next_round_team_pair(self,game_id):
        next_round_member = self.pick_next_round(game_id)
        last_round_member = self.pick_participants(game_id)
        looser = list(set(last_round_member) - set(next_round_member))
        match_team_pair = []
        if len(next_round_member) == 2:
            match_team_pair = next_round_member
            for each in looser:
                match_team_pair.append(each)
            match_team_pair = self.knock_method(match_team_pair)
            match_team_pair.append('final_round')
        elif len(next_round_member) == 3:
            j = 0
            while j < len(next_round_member):
                row = next_round_member[j]
                k = j + 1
                while k < len(next_round_member):
                    each = next_round_member[k]
                    match_team_pair.append([row[0], row[1], each[0], each[1], row[2]])
                    k += 1
                j += 1
        else:
            match_team_pair = self.knock_method(next_round_member)
        return match_team_pair

    def admin_requirement(self, sql, type):
        cursor = self.__db.cursor()
        try:
            cursor.execute(sql)
            if type == 'update':
                self.__db.commit()
            else:
                return cursor.fetchall()
        except:
            self.__db.rollback()


# ------------------------------------------------------------------------------------------------------------------------------------
# By Li Donghua


class EventForm(Form):
    game_type = RadioField('game_type', [validators.data_required])
    game_limit = RadioField('game_limit',[validators.data_required])
    match_name = StringField('match_name', [validators.data_required])


class LoginForm(Form):
    username = StringField('username', [validators.DataRequired("Username is empty")])
    password = PasswordField('password', [validators.DataRequired("Password is empty")])


class newLeaderForm(Form):
    newLeader = StringField('newLeader', [validators.Length(min=10, max=10), validators.DataRequired()])
    newLeader = StringField('curTeam', [validators.DataRequired()])
    currentPassword = StringField('currentPassword', [validators.DataRequired()])

class individualRegisterFrom(Form):
    individualID = StringField('studentID', [validators.Length(min=10, max=10), validators.DataRequired()])
    individualPassword = PasswordField('user_password', [validators.DataRequired()])

class teamRegisterForm(Form):
    teamName = StringField('team_name', [validators.DataRequired()])
    leaderID = StringField('leader_id', [validators.DataRequired()])
    leaderPassword = PasswordField('leader_pwd', [validators.DataRequired()])
    member1 = StringField('team_member0', [validators.DataRequired()])
    signas1 = SelectField('signas0', choices=[('member', 'member'), ('alternative', 'alternative')])
    member2 = StringField('team_member1', [validators.DataRequired()])
    signas2 = SelectField('signas1', choices=[('member', 'member'), ('alternative', 'alternative')])
    member3 = StringField('team_member2', [validators.DataRequired()])
    signas3 = SelectField('signas2', choices=[('member', 'member'), ('alternative', 'alternative')])
    member4 = StringField('team_member3', [validators.DataRequired()])
    signas4 = SelectField('signas3', choices=[('member', 'member'), ('alternative', 'alternative')])
    member5 = StringField('team_member4', [validators.DataRequired()])
    signas5 = SelectField('signas4', choices=[('member', 'member'), ('alternative', 'alternative')])
    member6 = StringField('team_member5', [validators.DataRequired()])
    signas6 = SelectField('signas5', choices=[('member', 'member'), ('alternative', 'alternative')])
    member7 = StringField('team_member6', [validators.DataRequired()])
    signas7 = SelectField('signas6', choices=[('member', 'member'), ('alternative', 'alternative')])

# -------------------------------------------------------------------------------------------------------------------------------------
# By Li Donghua


class Model:
    def __init__(self):
        pass

    def checkUserDB(self, username, password):
        var1 = "SET @checkUser = '%s'" % (username)
        var2 = "SET @checkPassword = '%s'" % (password)
        connectDb = DatabaseOperations()
        db = connectDb.db_connect()
        cursor = db.cursor()
        sql = "SELECT * FROM user WHERE STUDENT_ID = @checkUser AND PASSWORD = @checkPassword"
        try:
            cursor.execute(var1)
            cursor.execute(var2)
            cursor.execute(sql)
            results = cursor.fetchall()
            foundUser = []
            for row in results:
                for col in row:
                    foundUser.append(col)
            if len(foundUser)!=0:
                return foundUser
            else:
                return 0
        except:
            return 0


    def printTeammatesInfo(self):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        cursor.execute("SELECT COUNT(*) FROM (SELECT STUDENT_ID, PLAYER_NAME, TEAM_NAME, STATUS, FORBIDDEN, POSITION FROM player NATURAL JOIN belong NATURAL JOIN team WHERE team.CAPTAIN_ACCOUNT= %d) AS c" % int(session.get('ID') ))
        session['tableColumn']=cursor.fetchone()[0]
        try:
            cursor.execute("SELECT STUDENT_ID, PLAYER_NAME, TEAM_NAME, STATUS, FORBIDDEN, POSITION FROM player NATURAL JOIN belong NATURAL JOIN team WHERE team.CAPTAIN_ACCOUNT= %d AND belong.POSITION != 'Team Leader'" % int(session.get('ID')))
            tableData = cursor.fetchall()
            return tableData
        except:
            print("query fail")
            return 3


    def updatePersonalInfo(self, newValue, flag):
        var1 = "SET @newInfo = '%s'" % (newValue)
        var2 = "SET @flag = '%s'" % (flag)
        ID = "SET @ID = %s " % (session['ID'])
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        # update new personal info
        if flag == 'USER_NAME':
            sql = "UPDATE user SET USER_NAME = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'PHONE_NO':
            sql = "UPDATE user SET PHONE_NO = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'EMAIL':
            sql = "UPDATE user SET EMAIL = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'SECURITY_QUESTION_1':
            sql = "UPDATE user SET SECURITY_QUESTION_1 = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'SECURITY_ANSWER_1':
            sql = "UPDATE user SET SECURITY_ANSWER_1 = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'SECURITY_QUESTION_2':
            sql = "UPDATE user SET SECURITY_QUESTION_2 = @newInfo WHERE STUDENT_ID = @ID"
        if flag == 'SECURITY_ANSWER_2':
            sql = "UPDATE user SET SECURITY_ANSWER_2 = @newInfo WHERE STUDENT_ID = @ID"
        try:
            cursor.execute(var1)
            cursor.execute(var2)
            cursor.execute(ID)
            cursor.execute(sql)
            db.commit()
            return 1
        except:
            # query fail error indicating code, if raised, rollback the database
            print("query fail")
            db.rollback()
            return "query fail"


    def transformLeader(self, cur, new, password, curTeam):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        curID = "SET @curID = '%s'" % (cur)
        newID = "SET @newID = '%s'" % (new)
        try:
            cursor.execute(curID)
            cursor.execute(newID)
            getPass = session.get('password')
            if getPass == password:
                try:
                    cursor.execute("SELECT AUTHORITY FORM user WHERE STUDENT_ID = @curID")
                    curAuthority = cursor.fetchone()[0]
                    cursor.execute("SELECT AUTHORITY FORM user WHERE STUDENT_ID = @newID")
                    newAuthority = cursor.fetchone()[0]
                    cursor.execute("SELECT COUNT(*) FROM (SELECT TEAM_ID FROM team WHERE CAPTAIN_ACCOUNT = @curID) AS a")
                    countCur = cursor.fetchone()[0]
                    if newAuthority in range(0,2):
                        try:
                            cursor.execute("UPDATE user SET AUTHORITY = 2 WHERE STUDENT_ID = @newID")
                            db.commit()
                        except:
                            db.rollback()
                            return "Update leader fail"
                    if countCur == 1:
                        try:
                            cursor.execute("UPDTAE user SET AUTHORITY = 1 WHERE SYTUDENT_ID = @curID")
                            db.commit()
                        except:
                            db.rollback()
                            return "Transform authority fail!"
                    try:
                        cursor.execute("UPDATE team SET CAPTAIN_ACCOUNT = @newID WHERE TEAM_ID = %d" % curTeam)
                        cursor.execute("UPDATE belong SET POSITION = 'Member' WHERE TEAM_ID = %d and STUDENT_ID = @curID" % curTeam)
                        cursor.execute("UPDATE belong SET POSITION = 'Team Leader' WHERE TEAM_ID = %d and STUDENT_ID = @newID" % curTeam)
                        db.commit()
                    except:
                        db.rollback()
                        return "Update new leader fail!"
                except:
                    db.rollback()
                    return 0
            else:
                return "Password incorrect!"
        except:
            return "Compare password fail"


    def getMax_Num(self, gameID):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT MAX_NUM FROM game WHERE GAME_ID = %d" %(gameID)
        try:
            cursor.execute(sql)
            return  cursor.fetchone()[0]
        except:
            print("Get max numbe of game fail!")
            return  -1


    def signupCompetition(self, signas, teamID, leaderPassword, chosenEvent):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sign = "SET @signas = '%s'" % (signas)
        ID = "SET @ID = '%s'" % (teamID)
        chosen = "SET @chosenEvent = '%d'" % (chosenEvent)
        if signas == "team":
            if Model().getParticipateNum(chosenEvent, signas)== Model().getMax_Num(chosenEvent):
                return "This event has been full!"

            sql1 = "SELECT CAPTAIN_ACCOUNT FROM team WHERE TEAM_ID = @ID"
            try:
                cursor.execute(sign)
                cursor.execute(ID)
                cursor.execute(chosen)
                cursor.execute(sql1)
                captainID = cursor.fetchone()
                sql3 = "SELECT PASSWORD FROM user WHERE STUDENT_ID = '%s'" % (captainID[0])
                cursor.execute(sql3)
                truePassword = cursor.fetchone()
                if leaderPassword == truePassword[0]:
                    sql2 = "INSERT INTO `PARTICIPATE` (`TEAM_ID`, `GAME_ID`) VALUES(@ID,@chosenEvent)"
                    try:
                        cursor.execute(sql2)
                        db.commit()
                        return 2
                    except:
                        db.rollback()
                        return "Insert fail!"
                else:
                        return "Password incorrect!"
            except:
                return "Fetch password fail!"




        else:
            try:
                cursor.execute(sign)
                cursor.execute(ID)
                cursor.execute(chosen)
                sql1 = "SELECT PASSWORD FROM user WHERE STUDENT_ID = @ID"
                cursor.execute(sql1)
                truePassword = cursor.fetchone()
                print(truePassword)
                if leaderPassword == truePassword[0]:
                    sql2 = "INSERT INTO `PARTICIPATE_INDIVIDUAL` (`STUDENT_ID`, `GAME_ID`) VALUES(@ID,@chosenEvent)"
                    try:
                        cursor.execute(sql2)
                        db.commit()
                        return 2
                    except:
                        db.rollback()
                        return "Insert fail!"
                else:
                    return "Password incorrect!"
            except:
                return "Fetch password fail!"


    def manageTeam(self, newPosition, newID, teamName):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql1 = "SELECT TEAM_ID FROM team WHERE TEAM_NAME = '%s'" % (teamName)
        try:
            cursor.execute(sql1)
            result = cursor.fetchone()
        except:
            print("Get team ID fail!")
            return 0
        sql = "UPDATE belong SET POSITION = '%s' WHERE STUDENT_ID = %d and TEAM_ID = %d" % (newPosition, int(newID), result[0])
        try:
            cursor.execute(sql)
            db.commit()
            return 1
        except:
            print("Update position fail")
            db.rollback()
            return 0


    def checkSession(self):
        # checking session
        if 'username' and 'ID' not in session:
            message = 'Login is overdue'
            return render_template('Login.html', message=message)

    def checkHighAuthority(self):
        if 'Authority' not in session or session.get('Authority') < 3:
            message = 'Your are not allowed to assess this page'
            return render_template('Login.html', message=message)

    def getTeamCompetition(self):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT GAME_ID, GAME_NAME FROM game WHERE GAME_LIMIT = 'team'"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except:
            return "Find team games fail!"


    def getIndividualCompetition(self):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT GAME_ID, GAME_NAME FROM game WHERE GAME_LIMIT = 'individual'"
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except:
            print("Find individual games fail!")
            return 0


    def getParticipateNum(self, gameID, type):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        if type == "team":
            sql = "select COUNT(TEAM_ID) FROM participate WHERE GAME_ID = %d GROUP BY GAME_ID " %(gameID)
        else:
            sql = "select COUNT(STUDENT_ID) FROM participate_individual WHERE GAME_ID = %d GROUP BY GAME_ID " %(gameID)
        try:
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            return result
        except:
            print("Find games participatant amount fail!")
            return 0


    def individualasPlayer(self, ID, password):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT PASSWORD, USER_NAME FROM user WHERE STUDENT_ID = %d" % int(ID)
        updateA = Model().updateAuthority(int(ID), 1)
        if  updateA == -1:
            return "This account has been banned!"
        elif updateA == 0:
            return "Update Authority fail!"
        else:
            try:
                cursor.execute(sql)
                result = cursor.fetchone()
                rightPwd = result[0]
                rightName = result[1]
                if password == rightPwd:
                    sql1 = "INSERT INTO `player` (`STUDENT_ID`, `PLAYER_NAME`, `STATUS`, `FORBIDDEN`) VALUES(%d, '%s', 'free', 0)" % (int(ID), rightName)
                    try:
                        cursor.execute(sql1)
                        db.commit()
                        return "Register successfully!"
                    except:
                        db.rollback()
                        return "This player has already been register!"
                else:
                    return "Password incorrect!"
            except:
                return "Can not find user " + ID + " please try again!"


    def teamasPlayer(self, leaderID, leaderPwd, teamName, teamMember, teamPositions):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        try:
            cursor.execute("SELECT * FROM team WHERE TEAM_NAME = '%s'" % teamName)
            result = cursor.fetchall()
            if result:
                return "Team name has been registered!"
        except:
            return "Check Team Name existent fail!"

        sql = "SELECT PASSWORD, USER_NAME FROM user WHERE STUDENT_ID = %d" % int(leaderID)
        try:
            cursor.execute(sql)
            result1 = cursor.fetchone()
            rightPwd = result1[0]
            rightName = result1[1]
            if leaderPwd == rightPwd:
                for a in teamMember:
                    if Model().updateAuthority(int(a), 1) == -1:
                        return 'The account of ' + a + 'has been banned!'
                if Model().updateAuthority(int(leaderID), 2) and Model().updateAuthority(int(leaderID), 2) != -1:
                    sql1 = "INSERT INTO `player` (`STUDENT_ID`, `PLAYER_NAME`, `STATUS`, `FORBIDDEN`) VALUES(%d, '%s', 'free', 0)" % (int(leaderID), rightName)
                    sql4 = "INSERT INTO `team` (`TEAM_NAME`, `CAPTAIN_ACCOUNT`) VALUES ('%s', %d)" %(teamName, int(leaderID))
                    try:
                        cursor.execute(sql1)
                        db.commit()
                    except:
                        db.rollback()
                    try:
                        cursor.execute(sql4)
                        db.commit()
                    except:
                        db.rollback()
                    try:
                        cursor.execute("SELECT `TEAM_ID` FROM `team` WHERE `TEAM_NAME` = '%s'" % teamName)
                        teamID = cursor.fetchone()[0]
                    except:
                        return "Get new generated team ID fail"
                    memberName = []
                    for h in teamMember:
                        try:
                            sql2 = "SELECT USER_NAME FORM user WHERE STUDENT_ID = %d" % int(h)
                            cursor.execute(sql2)
                            result = cursor.fetchone()[0]
                            memberName.append(result)
                        except:
                            db.rollback()
                    for i, l in zip(teamMember, memberName):
                        try:
                            sql3= "INSERT INTO `player` (`STUDENT_ID`, `PLAYER_NAME`, `STATUS`, `FORBIDDEN`) VALUES(%d, '%s', 'free', 0)" % (int(i), l)
                            cursor.execute(sql3)
                            db.commit()
                        except:
                            db.rollback()
                    try:
                        sql6 = "INSERT INTO `belong` (`STUDENT_ID`, `TEAM_ID`, POSITION ) VALUES(%d, %d, '%s')" % (int(leaderID), int(teamID), "Team Leader")
                        cursor.execute(sql6)
                        db.commit()
                    except:
                        db.rollback()
                    for j,k in zip(teamMember, teamPositions):
                        try:
                            sql5 = "INSERT INTO `belong` (`STUDENT_ID`, `TEAM_ID`, POSITION ) VALUES(%d, %d, '%s')" % (int(j), int(teamID), k)
                            cursor.execute(sql5)
                            db.commit()
                        except:
                            db.rollback()
                else:
                    return "This leader account " + leaderID + " is banned!"
            else:
                return "Password incorrect!"
        except:
            return "This user does not exist"
        return "Register successfully!"

    def updateAuthority(self, ID, level):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT AUTHORITY FROM user WHERE STUDENT_ID = %d" % ID
        try:
            cursor.execute(sql)
            result = cursor.fetchone()[0]
            if int(result) == -1:
                return -1
            elif level > int(result):
                sql1 = "UPDATE user SET AUTHORITY = %d WHERE STUDENT_ID = %d" %(level, ID)
                cursor.execute(sql1)
                db.commit()
                return 1
            return 1
        except:
            print("Update authority fail!")
            db.rollback()
            return 0

    def getLeaderTeam(self, ID):
        connectDB = DatabaseOperations()
        db = connectDB.db_connect()
        cursor = db.cursor()
        sql = "SELECT TEAM_ID, TEAM_NAME FROM team WHERE CAPTAIN_ACCOUNT = %d" % ID
        try:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        except:
            print("Get team names fail!")
            return 0





# ---------------------------------------------------------------------------------------------------------------------------------------
# By Li Donghua


@app.route('/')
def hello_world():
    session.clear()
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    return render_template('Login.html')


@app.route('/logout')
def logout():
    session.clear()
    return render_template('Login.html')


@app.route('/Login', methods=['GET', 'POST'])
def login_check():
    session.clear()
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.username.data and form.password.data:
            result = Model().checkUserDB(form.username.data, form.password.data)
            if result:
                # store all the info in session to promise refreshing no changing the info in the personal information page
                session.permanent = True
                session['ID'] = result[0]
                session['username'] = form.username.data
                session['password'] = form.password.data
                session['Email'] = result[1]
                session['Phone'] = result[2]
                session['Q1'] = result[5]
                session['A1'] = result[6]
                session['Q2'] = result[7]
                session['A2'] = result[8]
                session['Authority'] = int(result[9])
                teamTable = Model().printTeammatesInfo()
                if int(result[9]) == -1:
                    session.clear()
                    return render_template('Login.html', message="This account has been banned!")
                if teamTable:
                    if Model().getLeaderTeam((result[0])):
                        session['teamName'] = Model().getLeaderTeam(result[0])
                    session['teamTable'] = teamTable
                    return render_template('Personal Information.html', Name=form.username.data, ID=result[0], Email=result[1], Phone=result[2], Q1=result[5], A1=result[6], Q2=result[7], A2=result[8], tableDatas=teamTable, Authority=int(result[9]))
                elif not teamTable:
                    return render_template('Personal Information.html', Name=form.username.data, ID=result[0], Email=result[1], Phone=result[2], Q1=result[5], A1=result[6], Q2=result[7], A2=result[8], tableDatas=teamTable, Authority=int(result[9]))
                else:
                    message = "Team Table Error!"
                    return render_template('Login.html', message=message)
            else:
                message = "Username or Password incorrect"
                return render_template('Login.html', message=message)
        else:
            message = "Username or Password incorrect"
            return render_template('Login.html', message=message)
    else:
        message = "Username or Password cannot be empty"
        return render_template('Login.html', message=message)


@app.route('/Personal Information', methods=['GET', 'POST'])
def infoEdit():
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    form1 = newLeaderForm(request.form)
    # get the updated info from the front table
    newname = request.form.get("newname")
    newaddress = request.form.get("newaddress")
    newnumber = request.form.get("newnumber")
    newQ1 = request.form.get("newQ1")
    newA1 = request.form.get("newA1")
    newQ2 = request.form.get("newQ2")
    newA2 = request.form.get("newA2")


    if request.method == 'POST':
        i = 1
        newPositions = []
        members = []
        teamNames = []
        flag = False
        while True:
            position = 'newPosition' + str(i)
            memberID = 'memberID' + str(i)
            teamName = 'teamBelong' + str(i)
            if not request.form.get(memberID):
                break
            else:
                newPositions.append(request.form.get(position))
                members.append(request.form.get(memberID))
                teamNames.append(request.form.get(teamName))
                flag = True
            i += 1
        if flag:
            result1 = 0
            print(members)
            print(newPositions)
            print(teamNames)
            for i,j,k in zip (members,newPositions, teamNames):
                result1 = Model().manageTeam(j, i, k)
            if result1:
                # update successfully, clear the current session and require login again
                message = "User Updated, please login again"
                session.clear()
                return render_template('Login.html', message=message)
        # updating the new personal info
        elif newname or newaddress or newnumber or newQ1 or newA1 or newQ2 or newA2:
            result = 0
            if newname:
                result = Model().updatePersonalInfo(newname, "USER_NAME")
            if newnumber:
                result = Model().updatePersonalInfo(newnumber, "PHONE_NO")
            if newaddress:
                result = Model().updatePersonalInfo(newaddress, "EMAIL")
            if newQ1:
                result = Model().updatePersonalInfo(newQ1, "SECURITY_QUESTION_1")
            if newA1:
                result = Model().updatePersonalInfo(newA1, "SECURITY_ANSWER_1")
            if newQ2:
                result = Model().updatePersonalInfo(newQ2, "SECURITY_QUESTION_2")
            if newA2:
                result = Model().updatePersonalInfo(newA2, "SECURITY_ANSWER_2")
            if result:
                # update successfully, clear the current session and require login again
                message = "User Updated, please login again"
                session.clear()
                return render_template('Login.html', message=message)
            else:
                # updating error indicating code
                message = "Error occur at update New Info!"
                return render_template('Login.html', message=message)
        elif form1.validate():
            result1 = Model().transformLeader(session['ID'], form1.newLeader.data, form1.currentPassword.data, form1.curTeam.data)
            if result1 == 1:
                message = "User status update, please login again"
                session.clear()
                return render_template('Login.html', message=message)
            elif result1 == 'Password incorrect!':
                message = 'Password incorrect!'
                return render_template('Personal Information.html', message=message, Name=session.get('username'), ID=session.get('ID'), Email=session.get('Email'), Phone=session.get('Phone'), Q1=session.get('Q1'), A1=session.get('A1'), Q2=session.get('Q2'),A2=session.get('A2'), tableDatas=session.get('teamTable'), Authority=session.get('Authority'))
            else:
                message = 'Compare password fail'
                return render_template('Login.html', message=message)
        else:
            # validator error indicating code
            message = "Error occur at validator!"
            return render_template('Login.html', message=message)
    else:
        message = "Welcome back!"
        teamTable = Model().printTeammatesInfo()
        return render_template('Personal Information.html', message=message, Name=session.get('username'), ID=session.get('ID'), Email=session.get('Email'), Phone=session.get('Phone'), Q1=session.get('Q1'), A1=session.get('A1'), Q2=session.get('Q2'),A2=session.get('A2'), tableDatas=teamTable, Authority=session.get('Authority'))


@app.route('/CompitionSignup', methods=['GET', 'POST'])
def signupCompition():
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    signas = request.form.get('gridRadios')
    teamID = request.form.get('teamID')
    leaderPassword = request.form.get('leaderPass')
    chosenEvent = request.form.get('chosenEvent')
    teamGame = Model().getTeamCompetition()
    individualGame = Model().getIndividualCompetition()


    if request.method == 'POST':
        if signas and teamID and leaderPassword and chosenEvent:
            result = Model().signupCompetition(signas, teamID, leaderPassword, int(chosenEvent))
            if result == 2:
                message = "Sign up successfully!"
                return  render_template('CompetitionSignUpPage.html', message=message)
            else:
                message = result
                return  render_template('CompetitionSignUpPage.html', message=message)
        else:
            if not teamID:
                message = "Please input your team ID!"
            elif not leaderPassword:
                message = "Please input the leader's password!"
            elif not chosenEvent:
                message = "Please select an event!"
            else:
                message = "Something unexpected happens"
            return render_template("CompetitionSignUpPage.html", message=message)
    else:
        return render_template("CompetitionSignUpPage.html", teamGame = teamGame, individualGame = individualGame)

# --------------------------------------------------------------------------------------------------------------------------------
# By He Langxuan


@app.route('/ScheduleManagement')
def schedule_mange():
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return render_template('ScheduleManagement.html')


@app.route('/CreateSchedule', methods=['GET', 'POST'])
def schedule():
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    form = EventForm(request.form)
    if request.method == 'POST':
        max = int(request.form.get('max_num'))
        insert_result = DatabaseOperations().upload_event(form.game_type.data, form.match_name.data,max,form.game_limit.data)
        if (insert_result == 1):
            message = "Insert Success!!"
            alert = "alert-success"
            location = "ScheduleManagement"
            return render_template('Result.html', message=message, alert=alert, location=location)
        elif (insert_result == 0):
            message = "Fail to insert (match ahs already exist)!!"
            alert = "alert-danger"
            location = "ScheduleManagement"
            return render_template('Result.html', message=message, alert=alert, location=location)

        return render_template('CreateSchedule.html', max=form.game_limit.data)
    else:
        return render_template('CreateSchedule.html')


@app.route('/editTime/<string:back>')
def time_back(back):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return redirect(url_for('find_event'))


@app.route('/editTime/<int:game_id>', methods=['GET', 'POST'])
def time_change(game_id):
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    if (sql.check_condition(int(game_id)) == 0):
        message = "Fail to edit (event only can be edited when it is on matching)!!"
        alert = "alert-danger"
        location = "EditSchedule"
        return render_template('Result.html', message=message, alert=alert, location=location)
    round_num = sql.find_event_game_round(game_id)
    count = (sql.count_participant(game_id)[0])[1]
    champion_contender = False
    second_runner_contender = False
    is_final = False
    if round_num <= 1:
        team_pair = sql.get_team_pair(game_id)
    elif round_num > 1:
        team_pair =[]
        match_team_pair = session.get('next_round_member'+str(game_id))
        for each in match_team_pair:
            if each == 'final_round':
                is_final = True
                session.permanent = True
                session['final_round'+str(game_id)] = "Yes"
                break
            team_pair.append(each)
        if len(team_pair) != 3:
            count = 2*len(team_pair)
        else:
            count = len(team_pair)
        if is_final:
            champion_contender =True
            second_runner_contender =True
    is_bye = request.form.get('bye')
    infor = request.form.get('infor')
    date = str(request.form.get('date'))
    date_ymd = date[0:10]
    date_clock = date[11:]
    date_str = date_ymd + " " + date_clock
    if request.method == 'POST':
        if (is_bye == None):
            infor = infor.split('/')
            one_id = int(infor[0])
            two_id = int(infor[1])
            sql.upload_arrange(one_id, two_id, game_id, date_str)
        elif (infor == None):
            id = int(is_bye)
            nullvalue = 0
            sql.upload_arrange(id, nullvalue, game_id, nullvalue)
        return render_template('editTime.html', event_name=sql.find_event_name(game_id),
                               count= count,
                               match_team_pair=team_pair,
                               view=sql.view_arrange(game_id),
                               view_bye=sql.view_bye(game_id),
                               champion_contender=champion_contender,
                               second_runner_contender=second_runner_contender)
    else:
        return render_template('editTime.html', event_name=sql.find_event_name(game_id),
                               count=count,
                               match_team_pair=team_pair,
                               view=sql.view_arrange(game_id)
                               , view_bye=sql.view_bye(game_id),
                               champion_contender=champion_contender,
                               second_runner_contender=second_runner_contender)


@app.route('/editScore/<string:back>')
def score_back(back):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return redirect(url_for('find_event'))


@app.route('/editScore/<int:game_id>', methods=['GET', 'POST'])
def score_index(game_id):
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    if sql.check_condition(int(game_id)) == 0:
        message = "Fail to edit (event only can be edited when it is on matching)!!"
        alert = "alert-danger"
        location = "EditSchedule"
        return render_template('Result.html', message=message, alert=alert, location=location)
    alert = False
    if request.method == 'POST':
        one_score = int(request.form.get('team_one_score'))
        two_score = int(request.form.get('team_two_score'))
        infor = request.form.get('infor').split('/')
        one_id = int(infor[0])
        two_id = int(infor[1])
        match_id = int(sql.find_match_id(one_id, two_id, game_id))
        if one_score == two_score:
            alert = True
            return render_template('editScore.html', event_name=sql.find_event_name(game_id),
                                   match_team_pair=sql.view_arrange(game_id),
                                   view_score=sql.view_score(game_id), match_id=match_id, alert=alert)
        else:
            sql.upload_score(match_id, game_id, one_score, two_score)
            return render_template('editScore.html', event_name=sql.find_event_name(game_id),
                               match_team_pair=sql.view_arrange(game_id),
                               view_score=sql.view_score(game_id),match_id=match_id)
    else:
        return render_template('editScore.html', event_name=sql.find_event_name(game_id),
                               match_team_pair=sql.view_arrange(game_id),
                               view_score=sql.view_score(game_id),alert=alert)


@app.route('/editKnock/<string:back>')
def knock_back(back):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return redirect(url_for('find_event'))


@app.route('/editKnock/<int:game_id>',methods=['GET','POST'])
def knock_index(game_id):
    # checking session
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    message = ""
    show_upload_history = False
    show_button = True
    next_round_memeber = set(sql.pick_next_round(game_id))
    last_round_memeber = set(sql.pick_participants(game_id))
    if len(next_round_memeber) < len(last_round_memeber)/2:
        show_button = False
    elif len(next_round_memeber) == len(last_round_memeber):
        show_button = True
    elif len(last_round_memeber) - len(next_round_memeber) == 1:
        show_upload_history = True
        message = "All match is over"
        show_button = False
    if session.get('final_round'+str(game_id)) == 'Yes':
        show_button = False
        if len(next_round_memeber) < len(last_round_memeber) / 2:
            show_upload_history = False
        else:
            message = "All match is over"
            show_upload_history = True
    if request.method == 'POST':
        upload_request = request.form.get('upload')
        if upload_request == "upload_history":
            upload_result = sql.upload_history(game_id)
            if upload_result == "success":
                message = "Upload Success!!"
                alert = "alert-success"
                location = "ScheduleManagement"
                return render_template('Result.html', message=message, alert=alert, location=location)
            elif upload_result == "fail":
                message = "Upload Fail!! You have already upload the history"
                alert = "alert-danger"
                location = "ScheduleManagement"
                return render_template('Result.html', message=message, alert=alert, location=location)
        else:
            looser = list(set(last_round_memeber) - next_round_memeber)
            if sql.if_match_isdone(game_id) == 1:
                update_result = sql.generate_next_round(game_id)
                if update_result:
                    session.permanent = True
                    session['next_round_member'+str(game_id)] = update_result
                    sql.clear_the_old_record(game_id, looser)
                    message = "Generate Success!!"
                    alert = "alert-success"
                    location = "ScheduleManagement"
                    return render_template('Result.html', message=message, alert=alert, location=location)
                else:
                    message = "Fail !!"
                    alert = "alert-danger"
                    location = "ScheduleManagement"
                    return render_template('Result.html', message=message, alert=alert, location=location)
            else:
                message = "Unknown failure!!"
                alert = "alert-danger"
                location = "EditSchedule"
                return render_template('Result.html', message=message, alert=alert, location=location)
    else:
        return render_template('editKnock.html', event_name=sql.find_event_name(game_id),
                               current_round=sql.view_score(game_id),
                               current_bye =sql.view_bye(game_id),
                               game_round=sql.find_event_game_round(game_id),
                               show_button=show_button,
                               show_upload_history=show_upload_history,
                               message=message)


@app.route('/uploadResult/<string:back>')
def upload_back(back):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return redirect(url_for('find_event'))


@app.route('/viewPage/<string:back>')
def view_back(back):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    return redirect(url_for('find_event'))


@app.route('/uploadResult/<int:game_id>',methods=['POST','GET'])
def upload_index(game_id):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    message = ""
    show_upload_history = True
    next_round_memeber = set(sql.pick_next_round(game_id))
    last_round_memeber = set(sql.pick_participants(game_id))
    if len(next_round_memeber) < len(last_round_memeber) / 2:
        show_upload_history = False
    else:
        message = "All match is over"
    if request.method == 'POST':
        upload_result = sql.upload_history(game_id)
        if upload_result == "success":
            message = "Upload Success!!"
            alert = "alert-success"
            location = "ScheduleManagement"
            return render_template('Result.html', message=message, alert=alert, location=location)
        elif upload_result == "fail":
            message = "Upload Fail!! You have already upload the history"
            alert = "alert-danger"
            location = "ScheduleManagement"
            return render_template('Result.html', message=message, alert=alert, location=location)
    else:
        return render_template('uploadResult.html', event_name=sql.find_event_name(game_id),
                               current_round=sql.view_score(game_id),
                               show_upload_history=show_upload_history,
                               message=message)


@app.route('/viewPage/<int:game_id>')
def view_index(game_id):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    condition = sql.check_condition(game_id)
    event_name = sql.find_event_name(game_id)
    if condition == 1:
        title = "Team/Player(s) in the next round"
    else:
        title = "Participants"
    participants = sql.pick_participants(game_id)
    count = sql.count_participant(game_id)
    return render_template('viewPage.html',participants=participants,count=count,title=title,event_name =event_name)


@app.route('/EditSchedule', methods=['GET', 'POST'])
def find_event():
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    if request.method == 'POST':
        game_name = request.form.get('game_name')
        delete_result = sql.delete_event(game_name)
        if delete_result == "success":
            alert = "alert-success"
            return render_template('EditSchedule.html', events=sql.find_event(), alert=alert)
        elif delete_result == 'fail':
            alert = "alert-danger"
            return render_template('EditSchedule.html', events=sql.find_event(), alert=alert)
        elif delete_result == "notfound":
            alert = 'notfound'
            return render_template('EditSchedule.html', events=sql.find_event(), alert=alert)
        return render_template('EditSchedule.html', events=sql.find_event(), result=sql.delete_event(game_name))
    else:
        return render_template('EditSchedule.html', events=sql.find_event())


@app.route('/EditSchedule/<string:game_id_change>', methods=['GET', 'POST'])
def change_condition(game_id_change):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    sql = DatabaseOperations()
    game_id = game_id_change[5:]
    game_change_condition = game_id_change[0:5]
    if (game_change_condition == 'start' or game_change_condition == 'endit' or game_change_condition == 'reset'):
        game_id = int(game_id)
        sql.change_condition(game_change_condition, game_id)
        return redirect(url_for('find_event'))
    else:
        return redirect(url_for('find_event'))

# ------------------------------------------------------------------------------------------------------------
# By Li Junjiang


def table_attribute(table, num):
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    if 'Authority' not in session or session.get('Authority')<3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    if table == 'game':
        if num == 1:
            return 'GAME_ID'
        if num == 2:
            return 'GAME_NAME'
        if num == 3:
            return 'GAME_TYPE'
        if num == 4:
            return 'GAME_DATE'
        if num == 5:
            return 'GAME_CONDITION'
    elif table == 'team':
        if num == 1:
            return 'TEAM_ID'
        if num == 2:
            return 'TEAM_NAME'
        if num == 3:
            return 'CAPTAIN_ACCOUNT'
    elif table == 'user':
        if num == 1:
            return 'STUDENT_ID'
        if num == 2:
            return 'EMAIL'
        if num == 3:
            return 'PHONE_NO'
        if num == 4:
            return 'USER_NAME'
        if num == 5:
            return 'SECURITY_QUESTION_ANSWER'
        if num == 6:
            return 'PERMISSION'


@app.route('/AdministratorInformationEditingPage', methods=['GET', 'POST'])
def information_edit():
    if 'Authority' not in session or session.get('Authority') < 3:
        message = 'Your are not allowed to assess this page'
        return render_template('Login.html', message=message)
    if request.method == 'POST':
        table_name = request.form.get('tableName')
        if table_name == 'g' or table_name == 't' or table_name == 'u':
            if table_name == 'g':
                table = 'game'
            elif table_name == 't':
                table = 'team'
            else:
                table = 'user'
            sql = 'select * from ' + table + ' where 1';
            i = 0
            while True:
                attribute = table + 'Attribute' + str(i)
                if not request.form.get(attribute):
                    break
                attribute_name = table_attribute(table, int(request.form.get(attribute)))
                sql += ' and ' + attribute_name + request.form.get('signal' + str(i)) + '\'' + request.form.get(
                    'input' + str(i)) + '\''
                i += 1
            result = DatabaseOperations().admin_requirement(sql, 'query')
        else:
            sql = 'select count(*) from user where student_id = ' + request.form.get('studentId')
            result = DatabaseOperations().admin_requirement(sql, 'query')
            if(result[0][0] == 0):
                result = 'User not found!'
            else:
                sql = 'update user set AUTHORITY =' + table_name + ' where student_id = ' + request.form.get('studentId')
                DatabaseOperations().admin_requirement(sql, 'update')
                result = 'Success!'
            table = ''

        return render_template('AdministratorInformationEditingPage.html', result=result, table=table)
    else:
        return render_template('AdministratorInformationEditingPage.html')

# --------------------------------------------------------------------------------------------------------------------------------
# By Yu Jiahui


@app.route('/reset/<string:lostid>',methods=['GET','POST'])
def reset(lostid):
    lostid = lostid

    form = ResetForm(request.form)

    if request.method == "POST":
        newpassword = request.form['password']
        if form.validate():
            connectDB = DatabaseOperations()
            db = connectDB.db_connect()
            cursor = db.cursor()
            cursor.execute("UPDATE user SET PASSWORD = (%s) WHERE STUDENT_ID = (%s)", (newpassword, lostid))
            db.commit()
            flash("succuss!")
            message = "Your password has been updated!"
            db.close()
            return render_template('Login.html',message = message)
        else:
            flash("data invalid")
            return render_template('ResetAccount.html',form = form,lostid=lostid)

    return render_template('ResetAccount.html',form = form,lostid=lostid)


@app.route('/lost/', methods=['GET','POST'])
def lost():

    form = LostAccountForm(request.form)

    if request.method == "POST":
        sid = request.form['student_id']
        sanswer1 = request.form['sanswer1']
        sanswer2 = request.form['sanswer2']
        phone = request.form['phone']

        if form.validate():
            connectDB = DatabaseOperations()
            db = connectDB.db_connect()
            cursor = db.cursor()
            cursor.execute("SELECT PHONE_NO,SECURITY_ANSWER_1, SECURITY_ANSWER_2 FROM user WHERE STUDENT_ID = (%s)", sid)
            results = cursor.fetchall()
            for row in results:
                phoneNo = row[0]
                answer1 = row[1]
                answer2 = row[2]
                if phoneNo == phone:
                    if sanswer1 == answer1:
                        if sanswer2 == answer2:
                            flash("confirm! waiting to reset password")
                            db.close()
                            return redirect(url_for('reset',lostid = sid))
                        else:
                            flash("answer2 is wrong.")
                            db.close()
                            return render_template('ResetYourLostAccount.html',form=form)
                    else:
                        flash("answer1 is wrong")
                        db.close()
                        return render_template('ResetYourLostAccount.html',form = form)
                else:
                    flash("phone number does not match")
                    db.close()
                    return render_template('ResetYourLostAccount.html', form=form)
    return render_template('ResetYourLostAccount.html', form = form)


@app.route("/register/", methods=['GET', 'POST'])
def register():
    form = registerForm(request.form)
    if request.method == "POST":
        sid = request.form['student_id']
        email = request.form['mail']
        password = request.form['password']
        confirmPass = request.form['confirm']
        security1 = request.form['security1']
        answer1 = request.form['answer1']
        security2 = request.form['security2']
        answer2 = request.form['answer2']
        phone = request.form['pnumber']
        username = request.form['username']

        if form.validate() and confirmPass == password:
            connectDB = DatabaseOperations()
            db = connectDB.db_connect()
            cursor = db.cursor()
            try:
                cursor.execute("SELECT * FROM user WHERE STUDENT_ID = %d" % (int(sid)))
                result = cursor.fetchone()
            except:
                result = 0

            if result:
                flash("That id has already regietered, please directly login in ")
                return render_template('RegisterPage.html', form=form)
            else:
                try:
                    cursor.execute("INSERT INTO user (STUDENT_ID, EMAIL, PHONE_NO, USER_NAME, PASSWORD, SECURITY_QUESTION_1, SECURITY_ANSWER_1,SECURITY_QUESTION_2,SECURITY_ANSWER_2, AUTHORITY) VALUES (%d, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" %(int(sid), email, phone, username, password, security1, answer1, security2, answer2, '1'))
                    db.commit()
                except:
                    db.rollback()

                session['logged_in'] = True
                session['student_id'] = sid
                message = "Register successfully"
                return render_template("Login.html", message = message)
        else:
            if not form.mail:
                flash('Error: Email form invalid!')
            if not form.username:
                flash('Error: Username is invalid!')
            if confirmPass != password:
                flash('Error: Confirm Password unmatch!')
            if not form.answer1:
                flash('Error: Need an answer for security Question 1!')
            if not form.answer2:
                flash('Error: Need an answer for security Question 2!')
            # else:
            #     flash('Error: All the form fields are required. ')

    return render_template('RegisterPage.html', form=form)

# -------------------------------------------------------------------------------------------------------------------------------------
# Structured by Yu Jiahui, Fixed and recoded by Li Donghua


@app.route('/team_register/', methods=['GET','POST'])
def TeamRegistration():
    if 'username' and 'ID' not in session:
        message = 'Login is overdue'
        return render_template('Login.html', message=message)
    alert = False
    leaderID = request.form.get('leader_id')
    leadPwd = request.form.get('leader_pwd')
    teamName = request.form.get('team_name')
    members = []
    position = []
    if request.form.get('team_member0'):
        if request.form. get('team_0') not in members:
            members.append(request.form.get('team_member0'))
            if request.form.get('signas0'):
                position.append(request.form.get('signas0'))
    if request.form.get('team_member1'):
        if request.form.get('team_1') not in members:
            members.append(request.form.get('team_member1'))
            if request.form.get('signas1'):
                position.append(request.form.get('signas1'))
    if request.form.get('team_member2'):
        if request.form.get('team_2') not in members:
            members.append(request.form.get('team_member2'))
            if request.form.get('signas2'):
                position.append(request.form.get('signas2'))
    if request.form.get('team_member3'):
        if request.form.get('team_3') not in members:
            members.append(request.form.get('team_member3'))
            if request.form.get('signas3'):
                position.append(request.form.get('signas3'))
    if request.form.get('team_member4'):
        if request.form.get('team_4') not in members:
            members.append(request.form.get('team_member4'))
            if request.form.get('signas4'):
                position.append(request.form.get('signas4'))
    if request.form.get('team_member5'):
        if request.form.get('team_5') not in members:
            members.append(request.form.get('team_member5'))
            if request.form.get('signas5'):
                position.append(request.form.get('signas5'))
    if request.form.get('team_member6'):
        if request.form.get('team_6') not in members:
            members.append(request.form.get('team_member6'))
            if request.form.get('signas6'):
                position.append(request.form.get('signas6'))


    individualID = request.form.get('studentId')
    individualPwd = request.form.get('user_password')
    if request.method == 'POST':
        if individualID and individualPwd:
            result = Model().individualasPlayer(individualID, individualPwd)
            if result == "Register successfully!":
                message = result
                return render_template('Team Registration.html', message = message)
            else:
                message = result
                return  render_template('Team Registration.html', message = message)
        elif leaderID and leadPwd and teamName and members and position:
            if leaderID in members:
                return render_template("Team Registration.html", message = "Duplicated members!")
            result1 = Model().teamasPlayer(leaderID, leadPwd, teamName,members,position)
            if result1 == "Register successfully!":
                message = "Register successfully!"
                return render_template("Team Registration.html", message = message)
            else:
                return render_template("Team Registration.html", message = result1)
        else:
            message = "Data fetching error!"
            return render_template('Team Registration.html', message=message)
    else:
        return render_template('Team Registration.html')
