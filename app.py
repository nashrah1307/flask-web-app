from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Data storage file
DATA_FILE = 'tasks.json'

def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    """Home page"""
    tasks = load_tasks()
    completed = sum(1 for task in tasks if task['completed'])
    pending = len(tasks) - completed
    return render_template('index.html', 
                         tasks=tasks, 
                         total=len(tasks),
                         completed=completed,
                         pending=pending)

@app.route('/add', methods=['POST'])
def add_task():
    """Add a new task"""
    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'title': request.form.get('title'),
        'description': request.form.get('description'),
        'priority': request.form.get('priority', 'medium'),
        'completed': False,
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    tasks.append(task)
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/toggle/<int:task_id>')
def toggle_task(task_id):
    """Toggle task completion status"""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed']
            break
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.route('/api/tasks')
def api_tasks():
    """API endpoint to get all tasks"""
    tasks = load_tasks()
    return jsonify(tasks)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
