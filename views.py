from app import app
from flask import render_template, url_for
import os

audience_q_idx = 1
tiebreaker_q_idx = 1
round_3_disable = set()

def generic_read_question(file_path, index):
    f = open(file_path, 'r')
    for idx, line in enumerate(f):
        x = line.strip()
        if index == idx+1:
            f.close()
            return eval(x)

def generic_read_question_all(file_path):
    question_list = []
    for i in range(5):
        question_list.append(generic_read_question(file_path, i+1))
    return question_list

@app.route("/")
def homepage():
    return render_template("first_page.html")

@app.route("/a")
def all_rounds():
    return render_template("all_rounds.html")

@app.route("/a_e")
def all_rounds_e():
    return render_template("all_rounds_e.html")

@app.route("/audience")
def audience():
    global audience_q_idx
    file_path = url_for('static', filename='questions/audience/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    d_next, d_prev = url_for('all_rounds')
    if audience_q_idx > 6:
        return render_template('first_page.html')
    token = generic_read_question(file_path, audience_q_idx)
    #################################################
    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': audience_q_idx,
    'question':token[0],
    'option1':token[1],
    'option2':token[2],
    'option3':token[3],
    'option4':token[4],
    'answer':token[5]
    }
    audience_q_idx += 1
    return render_template("round_2.html", data=data)

@app.route("/tiebreaker")
def tiebreaker():
    global tiebreaker_q_idx
    file_path = url_for('static', filename='questions/tiebreaker/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    d_next, d_prev = url_for('all_rounds')
    if tiebreaker_q_idx > 12:
        return render_template('first_page.html')
    token = generic_read_question(file_path, tiebreaker_q_idx)
    #################################################
    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': tiebreaker_q_idx,
    'question':token[0],
    'option1':token[1],
    'option2':token[2],
    'option3':token[3],
    'option4':token[4],
    'answer':token[5]
    }
    tiebreaker_q_idx += 1
    return render_template("round_2.html", data=data)

@app.route("/1/<q_idx>")
def round_1(q_idx):
    q_idx = int(q_idx)
    file_path = url_for('static', filename='questions/1/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_next, d_prev = None, None
    token = generic_read_question(file_path, q_idx)
    if q_idx == 1:
        d_prev = url_for('all_rounds')
        d_next = url_for('round_1', q_idx=q_idx+1)
    elif q_idx == 8:
        d_prev = url_for('round_1', q_idx=q_idx-1)
        d_next = url_for('all_rounds')
    elif 1 < q_idx < 8:
        d_prev = url_for('round_1', q_idx=q_idx-1)
        d_next = url_for('round_1', q_idx=q_idx+1)
    #################################################

    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token[0],
    'answer':token[1]
    }
    return render_template("round_1.html", data=data)

@app.route("/2/<q_idx>")
def round_2(q_idx):
    q_idx = int(q_idx)
    file_path = url_for('static', filename='questions/2/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_next, d_prev = None, None
    token = generic_read_question(file_path, q_idx)
    if q_idx == 1:
        d_prev = url_for('all_rounds')
        d_next = url_for('round_2', q_idx=q_idx+1)
    elif q_idx == 8:
        d_prev = url_for('round_2', q_idx=q_idx-1)
        d_next = url_for('all_rounds')
    elif 1 < q_idx < 8:
        d_prev = url_for('round_2', q_idx=q_idx-1)
        d_next = url_for('round_2', q_idx=q_idx+1)
    #################################################
    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token[0],
    'option1':token[1],
    'option2':token[2],
    'option3':token[3],
    'option4':token[4],
    'answer':token[5]
    }
    return render_template("round_2.html", data=data)

@app.route("/3")
def round_3():
    d_prev = d_next = url_for('all_rounds')
    data = {
    'prev':d_prev,
    'next':d_next,
    'cleared':round_3_disable
    }
    return render_template('round_3.html', data=data)

@app.route("/3/<q_idx>")
def round_3_x(q_idx):
    global round_3_disable
    q_idx = int(q_idx)
    round_3_disable.add(q_idx)
    print (round_3_disable)
    file_path = url_for('static', filename='questions/3/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_prev = d_next = url_for('round_3')
    token = generic_read_question(file_path, q_idx)
    #################################################
    data = {
    'header_hide': True,
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token[0],
    'option1':token[1],
    'option2':token[2],
    'option3':token[3],
    'option4':token[4],
    'answer':token[5],
    'style_params':token[6],
    'div_params':token[7]
    }
    return render_template("round_2.html", data=data)

@app.route("/4/<q_idx>")
def round_4(q_idx):
    q_idx = int(q_idx)
    file_path = url_for('static', filename='questions/4/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_next, d_prev = None, None
    token = generic_read_question(file_path, q_idx)
    if q_idx == 1:
        d_prev = url_for('all_rounds')
        d_next = url_for('round_4', q_idx=q_idx+1)
    elif q_idx == 5:
        d_prev = url_for('round_4', q_idx=q_idx-1)
        d_next = url_for('all_rounds_e')
    elif 1 < q_idx < 5:
        d_prev = url_for('round_4', q_idx=q_idx-1)
        d_next = url_for('round_4', q_idx=q_idx+1)
    #################################################
    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token['question'],
    'answer':token['answer'],
    'width':token['width'],
    'height':token['height'],
    'path': url_for('static', filename='questions/4/'+token['path']),
    'video':token.get('video')
    }
    return render_template("round_4.html", data=data)

@app.route("/5/<q_idx>")
def round_5(q_idx):
    q_idx = int(q_idx)
    file_path = url_for('static', filename='questions/5/{0}/que.txt'.format(q_idx))
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_next, d_prev = None, None
    if q_idx == 1:
        d_prev = url_for('all_rounds')
        d_next = url_for('round_5', q_idx=q_idx+1)
    elif q_idx == 4:
        d_prev = url_for('round_5', q_idx=q_idx-1)
        d_next = url_for('all_rounds_e')
    elif 1 < q_idx < 4:
        d_prev = url_for('round_5', q_idx=q_idx-1)
        d_next = url_for('round_5', q_idx=q_idx+1)
    #################################################
    question_list = generic_read_question_all(file_path)
    token = generic_read_question(file_path, q_idx)
    data = {
    'header_hide': True,
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token[0],
    'question_list':question_list,
    'option1':token[1],
    'option2':token[2],
    'answer':token[3]
    }
    return render_template('round_5.html', data=data)


@app.route("/6/<q_idx>")
def round_6(q_idx):
    q_idx = int(q_idx)
    file_path = url_for('static', filename='questions/6/que.txt')
    root = os.getcwd().replace("\\","/")
    if not len(root.split('/seed/application')) > 1:
        root += "/seed/application"
    file_path = root+file_path

    #################################################
    d_next, d_prev = None, None
    token = generic_read_question(file_path, q_idx)
    if q_idx == 1:
        d_prev = url_for('all_rounds')
        d_next = url_for('round_6', q_idx=q_idx+1)
    elif q_idx == 3:
        d_prev = url_for('round_6', q_idx=q_idx-1)
        d_next = url_for('all_rounds')
    elif 1 < q_idx < 3:
        d_prev = url_for('round_6', q_idx=q_idx-1)
        d_next = url_for('round_6', q_idx=q_idx+1)
    #################################################

    data = {
    'next': d_next,
    'prev': d_prev,
    'q_idx': q_idx,
    'question':token[0],
    'answer':token[1],
    'path1': url_for('static', filename='questions/6/'+token[2]) if token[2] else None,
    'path2': url_for('static', filename='questions/6/'+token[3]) if token[3] else None,
    'path3': url_for('static', filename='questions/6/'+token[4]) if token[4] else None
    }
    return render_template("round_6.html", data=data)
