# TaskMaster Pro - Complete Productivity Suite

A comprehensive productivity web application built with Flask featuring **Task Management**, **Expense Tracking**, and **Note Taking** all in one place.

![TaskMaster Pro](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Version](https://img.shields.io/badge/Version-2.0-purple)

## 🌟 Features

### 📋 Task Manager
- ✅ Create and manage tasks with titles and descriptions
- 🎯 Set task priorities (Low, Medium, High)
- ✔️ Mark tasks as completed
- 📊 Track statistics (Total, Completed, Pending)
- 🗑️ Delete tasks when done

### 💰 Expense Tracker
- 💵 Track all your expenses
- 🏷️ Categorize expenses (Food, Transportation, Shopping, Entertainment, Bills, Healthcare, Education, Other)
- 📊 View spending statistics and category breakdown
- 📅 Date-based expense tracking
- 💳 See total spending at a glance

### 📝 Notes Manager
- 📒 Create colorful sticky notes
- 🎨 Choose from 5 color themes (Yellow, Blue, Green, Pink, Purple)
- ✏️ Edit notes anytime
- 🗂️ Organize your thoughts and ideas
- 🕐 Track creation and update times

### 🎨 General Features
- 📱 Fully responsive design for all devices
- 🚀 Fast and lightweight
- 💾 JSON-based data persistence
- 🔌 RESTful API endpoints for all modules
- 🎭 Modern, intuitive user interface
- ⚡ Smooth animations and transitions

## 🛠️ Technologies Used

- **Backend**: Python 3.11, Flask 3.0.0
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: JSON
- **Icons**: Font Awesome 6.4.0
- **Server**: Gunicorn (for production)
- **Deployment**: Render/Vercel/Railway

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 Local Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/flask-web-app.git
cd flask-web-app
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment Instructions

### Option 1: Deploy on Render (Recommended - FREE)

1. **Create a Render Account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub

2. **Push Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/flask-web-app.git
   git push -u origin main
   ```

3. **Create New Web Service on Render**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: `taskmaster-pro`
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

4. **Deploy**
   - Click "Create Web Service"
   - Wait 2-3 minutes
   - Your app will be live at: `https://taskmaster-pro.onrender.com`

See `DEPLOYMENT_GUIDE.md` for detailed deployment instructions.

## 📁 Project Structure

```
flask-web-app/
│
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── Procfile                 # Deployment configuration
├── runtime.txt              # Python version
├── .gitignore               # Git ignore rules
│
├── templates/               # HTML templates
│   ├── base.html           # Base template
│   ├── index.html          # Task Manager page
│   ├── expenses.html       # Expense Tracker page
│   ├── notes.html          # Notes Manager page
│   └── about.html          # About page
│
├── static/                 # Static assets
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       └── script.js      # JavaScript
│
├── tasks.json              # Task data (auto-created)
├── expenses.json           # Expense data (auto-created)
├── notes.json              # Notes data (auto-created)
│
└── README.md               # This file
```

## 🎯 Usage Guide

### Task Manager
1. Navigate to **Tasks** page
2. Click "Add New Task"
3. Fill in title, description, and priority
4. Click circle icon to mark complete
5. Click trash icon to delete

### Expense Tracker
1. Navigate to **Expenses** page
2. Click "Add New Expense"
3. Enter title, amount, category, and date
4. View statistics and category breakdown
5. Delete expenses as needed

### Notes Manager
1. Navigate to **Notes** page
2. Click "Add New Note"
3. Enter title and content
4. Choose a color theme
5. Edit or delete notes using icons

## 🔌 API Endpoints

### Tasks API
- `GET /api/tasks` - Get all tasks

### Expenses API
- `GET /api/expenses` - Get all expenses

### Notes API
- `GET /api/notes` - Get all notes

Example usage:
```bash
curl https://your-app.onrender.com/api/tasks
```

## 🎨 Customization

### Change Colors
Edit `static/css/style.css`:
```css
:root {
    --primary-color: #your-color;
    --secondary-color: #your-color;
}
```

### Add New Categories (Expenses)
Edit `templates/expenses.html` in the category select dropdown.

### Add New Colors (Notes)
Edit `templates/notes.html` and add color options in the color picker.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit (`git commit -am 'Add new feature'`)
5. Push (`git push origin feature/improvement`)
6. Create a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com

## 🙏 Acknowledgments

- Flask Documentation
- Font Awesome for icons
- Render for free hosting
- All contributors

## 📸 Screenshots

### Task Manager
Organize your daily tasks with priorities and completion tracking.

### Expense Tracker
Track spending across multiple categories with visual breakdowns.

### Notes Manager
Capture ideas with colorful, editable sticky notes.

## 🐛 Known Issues

- Data stored in JSON files (consider database for production)
- Single-user application (no authentication)
- Free hosting has cold starts (30-60 second wake-up)

## 🔮 Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Export data to CSV/PDF
- [ ] Charts and visualizations for expenses
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Dark mode toggle
- [ ] Mobile app version
- [ ] Email notifications
- [ ] Recurring expenses

## 💡 For Students

This is a complete project that demonstrates:
- Full-stack web development
- Database operations (CRUD)
- RESTful API design
- Responsive UI/UX design
- Cloud deployment
- Version control with Git

Perfect for:
- Academic projects
- Portfolio piece
- Learning Flask framework
- Understanding web development

## 📞 Support

For issues or questions:
- Open an issue on GitHub
- Check the documentation
- Review Flask guides

---

**Built with ❤️ using Flask**

TaskMaster Pro - Your All-in-One Productivity Suite

Version 2.0 | January 2026
