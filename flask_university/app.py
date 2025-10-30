from flask import Flask, render_template, request, redirect, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'secret_key_123'

users = {'admin': 'password'}
universities = []
students = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['user'] = username
            flash('Вход выполнен успешно!')
            return redirect('/')
        else:
            flash('Неправильные данные для входа!')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Выход выполнен!')
    return redirect('/')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users:
            flash('Пользователь с таким именем уже существует!')
        else:
            users[username] = password
            flash('Пользователь создан успешно! Теперь можете войти.')
            return redirect('/login')
    
    return render_template('register.html')

@app.route('/universities')
def universities_list():
    return render_template('universities.html', universities=universities)

@app.route('/universities/create', methods=['GET', 'POST'])
def create_university():
    if 'user' not in session:
        flash('Необходимо войти в систему!')
        return redirect('/login')
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        short_name = request.form['short_name']
        creation_date = request.form['creation_date']
        
        university = {
            'id': len(universities) + 1,
            'full_name': full_name,
            'short_name': short_name,
            'creation_date': creation_date
        }
        universities.append(university)
        flash('Университет создан!')
        return redirect('/universities')
    
    return render_template('create_university.html')

@app.route('/students')
def students_list():
    return render_template('students.html', students=students, universities=universities)

@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    if 'user' not in session:
        flash('Необходимо войти в систему!')
        return redirect('/login')
    
    if request.method == 'POST':
        full_name = request.form['full_name']
        birth_date = request.form['birth_date']
        university_id = int(request.form['university_id'])
        enrollment_year = int(request.form['enrollment_year'])
        
        university = next((u for u in universities if u['id'] == university_id), None)
        
        student = {
            'id': len(students) + 1,
            'full_name': full_name,
            'birth_date': birth_date,
            'university': university,
            'enrollment_year': enrollment_year
        }
        students.append(student)
        flash('Студент создан!')
        return redirect('/students')
    
    return render_template('create_student.html', universities=universities)

if __name__ == '__main__':
    app.run(debug=True)