from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de tarefas com campo de conclusão
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form.get('task')
    if task_name:
        tasks.append({'name': task_name, 'completed': False})  # Adiciona uma nova tarefa como não concluída
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['completed'] = True  # Marca a tarefa como concluída
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

'''

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)


@app.route('/add' , methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        task.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        task.pop(task_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

'''