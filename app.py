from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# Data storage files
TASKS_FILE = 'tasks.json'
EXPENSES_FILE = 'expenses.json'
NOTES_FILE = 'notes.json'

# ==================== TASKS FUNCTIONS ====================
def load_tasks():
    """Load tasks from JSON file"""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    """Save tasks to JSON file"""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# ==================== EXPENSES FUNCTIONS ====================
def load_expenses():
    """Load expenses from JSON file"""
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    """Save expenses to JSON file"""
    with open(EXPENSES_FILE, 'w') as f:
        json.dump(expenses, f, indent=2)

# ==================== NOTES FUNCTIONS ====================
def load_notes():
    """Load notes from JSON file"""
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, 'r') as f:
            return json.load(f)
    return []

def save_notes(notes):
    """Save notes to JSON file"""
    with open(NOTES_FILE, 'w') as f:
        json.dump(notes, f, indent=2)

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

# ==================== EXPENSE TRACKER ROUTES ====================
@app.route('/expenses')
def expenses():
    """Expense tracker page"""
    expenses = load_expenses()
    
    # Calculate statistics
    total_expenses = sum(float(exp['amount']) for exp in expenses)
    monthly_expenses = {}
    category_expenses = {}
    
    for exp in expenses:
        # Monthly totals
        month = exp['date'][:7]  # YYYY-MM
        monthly_expenses[month] = monthly_expenses.get(month, 0) + float(exp['amount'])
        
        # Category totals
        category = exp['category']
        category_expenses[category] = category_expenses.get(category, 0) + float(exp['amount'])
    
    return render_template('expenses.html', 
                         expenses=expenses,
                         total_expenses=total_expenses,
                         count=len(expenses),
                         monthly_expenses=monthly_expenses,
                         category_expenses=category_expenses)

@app.route('/expenses/add', methods=['POST'])
def add_expense():
    """Add a new expense"""
    expenses = load_expenses()
    expense = {
        'id': len(expenses) + 1,
        'title': request.form.get('title'),
        'amount': request.form.get('amount'),
        'category': request.form.get('category'),
        'date': request.form.get('date'),
        'description': request.form.get('description', ''),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    save_expenses(expenses)
    return redirect(url_for('expenses'))

@app.route('/expenses/delete/<int:expense_id>')
def delete_expense(expense_id):
    """Delete an expense"""
    expenses = load_expenses()
    expenses = [exp for exp in expenses if exp['id'] != expense_id]
    save_expenses(expenses)
    return redirect(url_for('expenses'))

# ==================== NOTES MANAGER ROUTES ====================
@app.route('/notes')
def notes():
    """Notes manager page"""
    notes = load_notes()
    return render_template('notes.html', 
                         notes=notes,
                         total=len(notes))

@app.route('/notes/add', methods=['POST'])
def add_note():
    """Add a new note"""
    notes = load_notes()
    note = {
        'id': len(notes) + 1,
        'title': request.form.get('title'),
        'content': request.form.get('content'),
        'color': request.form.get('color', 'yellow'),
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    notes.append(note)
    save_notes(notes)
    return redirect(url_for('notes'))

@app.route('/notes/edit/<int:note_id>', methods=['POST'])
def edit_note(note_id):
    """Edit a note"""
    notes = load_notes()
    for note in notes:
        if note['id'] == note_id:
            note['title'] = request.form.get('title')
            note['content'] = request.form.get('content')
            note['color'] = request.form.get('color', 'yellow')
            note['updated_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    save_notes(notes)
    return redirect(url_for('notes'))

@app.route('/notes/delete/<int:note_id>')
def delete_note(note_id):
    """Delete a note"""
    notes = load_notes()
    notes = [note for note in notes if note['id'] != note_id]
    save_notes(notes)
    return redirect(url_for('notes'))

@app.route('/api/tasks')
def api_tasks():
    """API endpoint to get all tasks"""
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/api/expenses')
def api_expenses():
    """API endpoint to get all expenses"""
    expenses = load_expenses()
    return jsonify(expenses)

@app.route('/api/notes')
def api_notes():
    """API endpoint to get all notes"""
    notes = load_notes()
    return jsonify(notes)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
