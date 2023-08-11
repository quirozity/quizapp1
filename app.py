from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    q1_answer = request.form['q1']
    q2_answer = request.form['q2']
    q3_answer = request.form['q3']
    q4_answer = request.form['q4']
    q5_answer = request.form['q5']
    q6_answer = request.form['q6']
    q7_answer = request.form['q7']
    q8_answer = request.form['q8']
    q9_answer = request.form['q9']
    q10_answer = request.form['q10']
    
    score = 0
    wrong_questions = []

    if q1_answer == 'a':
        score += 1
    else:
        wrong_questions.append("Question 1")

    if q2_answer == 'b':
        score += 1
    else:
        wrong_questions.append("Question 2")

    if q3_answer == 'c':
        score += 1
    else:
        wrong_questions.append("Question 3")

    if q4_answer == 'a':
        score += 1
    else:
        wrong_questions.append("Question 4")

    if q5_answer == 'b':
        score += 1
    else:
        wrong_questions.append("Question 5")

    if q6_answer == 'c':
        score += 1
    else:
        wrong_questions.append("Question 6")

     if q7_answer == 'b':
        score += 1
    else:
        wrong_questions.append("Question 7")

     if q8_answer == 'a':
        score += 1
    else:
        wrong_questions.append("Question 8")

     if q9_answer == 'c':
        score += 1
    else:
        wrong_questions.append("Question 9")

     if q10_answer == 'c':
        score += 1
    else:
        wrong_questions.append("Question 10")
    
    return render_template('results.html', score=score, wrong_questions=wrong_questions)

if __name__ == '__main__':
    app.run(debug=True)
