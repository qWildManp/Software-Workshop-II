import pymysql
from datetime import datetime
class DatabaseOperations():
    # Fill in the information of your database server.
    __db_url = 'localhost'
    __db_username = 'root'
    __db_password = ''
    __db_name = 'uccg'
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
            self.__db.close()
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


# --------------------------------------------------------------------


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
            self.__db.close()


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
            if(result):
                sql_check_condition = """SELECT GAME_CONDITION FROM GAME WHERE GAME_NAME = '%s'""" % (game_name)
                try:
                    cursor.execute(sql_check_condition)
                    condition_result = cursor.fetchall()
                    condition = (condition_result[0])[0]
                    if(condition != 'onMatching'):
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
                                    except :
                                        pass
                                if check_par:
                                    sql_delete_participate = """DELETE FROM PARTICIPATE WHERE GAME_ID = %d""" %(game_id)
                                    try:
                                        cursor.execute(sql_delete_participate)
                                        self.__db.commit()
                                    except:
                                        pass
                            elif game_limit == 2:
                                if check_sco :
                                    sql_delete_score_team = """DELETE FROM MATCH_SCORE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_score_team)
                                        self.__db.commit()
                                    except :
                                        pass
                                if check_arr:
                                    sql_delete_arr_team = """DELETE FROM MATCH_ARRANGE WHERE GAME_ID = %d""" % (game_id)
                                    try:
                                        cursor.execute(sql_delete_arr_team)
                                        self.__db.commit()
                                    except :
                                        pass
                                if check_par:
                                    sql_delete_participate = """DELETE FROM PARTICIPATE_INDIVIDUAL WHERE GAME_ID = %d""" % (game_id)
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
                except :
                    pass
            else:
                return "notfound"
        except:
            pass

# --------------------------------------------------------------------


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
            self.__db.close()

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
            self.__db.close()


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
            sql_player = """SELECT PARTICIPATE_INDIVIDUAL.STUDENT_ID,USER.USER_NAME,PARTICIPATE_INDIVIDUAL.GAME_ID 
            FROM PARTICIPATE_INDIVIDUAL NATURAL JOIN PLAYER NATURAL JOIN USER 
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
            sql_view = """SELECT T1.STUDENT_ID, T1.USER_NAME ,T2.STUDENT_ID,T2.USER_NAME ,ARR_TIME 
            FROM  USER  AS T1 ,USER AS T2, MATCH_ARRANGE_INDIVIDUAL
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
            sql_view = """SELECT T1.STUDENT_ID,T1.USER_NAME,MATCH_ARRANGE_INDIVIDUAL.GAME_ID
                        FROM  USER  AS T1 , MATCH_ARRANGE_INDIVIDUAL
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
            sql_view = """SELECT T1.STUDENT_ID,T1.USER_NAME,T2.STUDENT_ID,T2.USER_NAME,PLAYER_ONE_SCORE,PLAYER_TWO_SCORE,ARR_TIME
                        FROM MATCH_ARRANGE_INDIVIDUAL, USER as T1 ,USER as T2 ,MATCH_SCORE_INDIVIDUAL
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
                return 0
            elif arr_num-bye_num == actual_num:
                return 1
            else:
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
            sql_winner_left = """SELECT T1.STUDENT_ID,T1.USER_NAME,MATCH_SCORE_INDIVIDUAL.GAME_ID
                                    FROM MATCH_ARRANGE_INDIVIDUAL, USER as T1 ,USER as T2 ,MATCH_SCORE_INDIVIDUAL
                                    WHERE T1.STUDENT_ID = STUDENT_ID_ONE 
                                    AND T2.STUDENT_ID =STUDENT_ID_TWO 
                                    AND MATCH_ARRANGE_INDIVIDUAL.MATCH_ID = MATCH_SCORE_INDIVIDUAL.MATCH_ID 
                                    AND PLAYER_ONE_SCORE > PLAYER_TWO_SCORE 
                                    AND MATCH_SCORE_INDIVIDUAL.GAME_ID= %d""" % (game_id)
            sql_winner_right = """SELECT T2.STUDENT_ID,T2.USER_NAME,MATCH_SCORE_INDIVIDUAL.GAME_ID
                                            FROM MATCH_ARRANGE_INDIVIDUAL, USER as T1 ,USER as T2 ,MATCH_SCORE_INDIVIDUAL
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
            sql_pick = """ SELECT STUDENT_ID,USER_NAME,GAME_ID FROM PARTICIPATE_INDIVIDUAL NATURAL JOIN USER 
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