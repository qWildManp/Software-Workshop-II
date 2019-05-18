from wtforms import Form, StringField, validators, RadioField
from flask import Flask, render_template, request, redirect, url_for,session
from DatabaseOperation import DatabaseOperations

app = Flask(__name__)
app.config['SECRET_KEY'] = "next_round_member"




class EventForm(Form):
    game_type = RadioField('game_type', [validators.data_required])
    game_limit = RadioField('game_limit',[validators.data_required])
    match_name = StringField('match_name', [validators.data_required])



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ScheduleManagement')
def schedule_mange():
    return render_template('ScheduleManagement.html')


@app.route('/CreateSchedule', methods=['GET', 'POST'])
def schedule():
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
    return redirect(url_for('find_event'))


@app.route('/editTime/<int:game_id>', methods=['GET', 'POST'])
def time_change(game_id):
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
                               count= count,
                               match_team_pair=team_pair,
                               view=sql.view_arrange(game_id)
                               , view_bye=sql.view_bye(game_id),
                               champion_contender=champion_contender,
                               second_runner_contender=second_runner_contender)


@app.route('/editScore/<string:back>')
def score_back(back):
    return redirect(url_for('find_event'))


@app.route('/editScore/<int:game_id>', methods=['GET', 'POST'])
def score_index(game_id):
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
                               view_score=sql.view_score(game_id),match_id=match_id,alert=alert)
    else:
        return render_template('editScore.html', event_name=sql.find_event_name(game_id),
                               match_team_pair=sql.view_arrange(game_id),
                               view_score=sql.view_score(game_id),alert=alert)






@app.route('/editKnock/<string:back>')
def knock_back(back):
    return redirect(url_for('find_event'))


@app.route('/editKnock/<int:game_id>',methods=['GET','POST'])
def knock_index(game_id):
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
    return redirect(url_for('find_event'))


@app.route('/uploadResult/<int:game_id>',methods=['POST','GET'])
def upload_index(game_id):
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

@app.route('/viewPage/<string:back>')
def view_back(back):
    return redirect(url_for('find_event'))


@app.route('/viewPage/<int:game_id>')
def view_index(game_id):
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
    sql = DatabaseOperations()
    game_id = game_id_change[5:]
    game_change_condition = game_id_change[0:5]
    if (game_change_condition == 'start' or game_change_condition == 'endit' or game_change_condition == 'reset'):
        game_id = int(game_id)
        sql.change_condition(game_change_condition, game_id)
        return redirect(url_for('find_event'))
    else:
        return redirect(url_for('find_event'))




def table_attribute(table, num):
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
            sql = 'update user set PERMISSION =' + table_name + ' where student_id = ' + request.form.get('studentId')
            DatabaseOperations().admin_requirement(sql, 'update')
            result = 'success'
            table = ''

        return render_template('AdministratorInformationEditingPage.html', result=result, table=table)

    else:
        return render_template('AdministratorInformationEditingPage.html')