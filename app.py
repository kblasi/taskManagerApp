#import flask and request
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

#create empty list for tasks to be added to
tasks = []


@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

# route to POST ("add") task to the list
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect('/')

# route to DELETE task from list
@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect('/')

# route to edit task in List
@app.route('/edit/<int:task_id>')
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        task_to_edit = tasks[task_id]
        return render_template('edit.html', task_id=task_id, task=task_to_edit)
    else:
        return redirect('/')

@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if 0 <= task_id < len(tasks):
        updated_task = request.form.get('updated_task')
        tasks[task_id] = updated_task
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
