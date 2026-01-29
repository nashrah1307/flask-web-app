# TaskMaster Pro - Flask Web Application

A modern, intuitive task management web application built with Flask. Organize your daily tasks, set priorities, and track your progress efficiently.

![TaskMaster Pro](https://img.shields.io/badge/Flask-3.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

- ✅ Create and manage tasks easily
- 🎯 Set task priorities (Low, Medium, High)
- ✔️ Mark tasks as completed
- 📊 Track statistics (Total, Completed, Pending)
- 🎨 Clean and modern user interface
- 📱 Responsive design for all devices
- 💾 JSON-based data persistence

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Data Storage**: JSON
- **Icons**: Font Awesome
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
     - **Name**: `taskmaster-pro` (or your choice)
     - **Environment**: `Python 3`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`
     - **Plan**: Free

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (2-3 minutes)
   - Your app will be live at: `https://taskmaster-pro.onrender.com`

### Option 2: Deploy on Vercel (FREE)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Create vercel.json**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "app.py"
       }
     ]
   }
   ```

3. **Deploy**
   ```bash
   vercel
   ```

### Option 3: Deploy on Railway (FREE)

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository
   - Railway will auto-detect Flask and deploy

3. **Generate Domain**
   - Go to Settings → Generate Domain
   - Your app will be live!

### Option 4: Deploy on PythonAnywhere (FREE)

1. **Create Account** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload Code**
   - Use Git or upload files directly

3. **Configure Web App**
   - Go to Web tab → Add a new web app
   - Choose Flask
   - Configure WSGI file

## 📁 Project Structure

```
flask-web-app/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
│
├── templates/            # HTML templates
│   ├── base.html        # Base template
│   ├── index.html       # Home page
│   └── about.html       # About page
│
├── static/              # Static files
│   ├── css/
│   │   └── style.css   # Styles
│   └── js/
│       └── script.js   # JavaScript
│
└── tasks.json          # Data storage (auto-created)
```

## 🎯 Usage

1. **Add Task**: Click "Add New Task" button, fill in details, and save
2. **Complete Task**: Click the circle icon next to a task to mark it complete
3. **Delete Task**: Click the trash icon to remove a task
4. **View Statistics**: Dashboard shows total, completed, and pending tasks
5. **Priority Levels**: Assign Low, Medium, or High priority to tasks

## 🔧 Configuration

### Environment Variables (Optional)

Create a `.env` file for production settings:

```env
FLASK_ENV=production
SECRET_KEY=your-secret-key-here
```

### Modify Port (if needed)

In `app.py`, change the port:

```python
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
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
- All contributors and testers

## 📸 Screenshots

### Home Page
![Home Page](screenshots/home.png)

### Task Management
![Task Management](screenshots/tasks.png)

### About Page
![About Page](screenshots/about.png)

## 🐛 Known Issues

- Data persists in JSON file (consider database for production)
- No user authentication (single-user application)

## 🔮 Future Enhancements

- [ ] User authentication and multi-user support
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Task categories and tags
- [ ] Due dates and reminders
- [ ] Export tasks to CSV/PDF
- [ ] Dark mode toggle
- [ ] Mobile app version

## 💡 Tips for Students

**For your teacher submission:**

1. Create a GitHub repository
2. Push all code to GitHub
3. Deploy on Render (easiest and free)
4. Submit the live URL: `https://your-app-name.onrender.com`
5. Also submit GitHub repository link

**What to include in submission:**
- Live deployment URL
- GitHub repository link
- Screenshots of the application
- Brief description of features

## 📞 Support

If you have any questions or need help with deployment, please:
- Open an issue on GitHub
- Check the Flask documentation
- Review Render's deployment guides

---

**Happy Coding! 🚀**

Made with ❤️ using Flask
