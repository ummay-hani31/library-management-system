# 📚 Library Management System

A **Library Management System** built using **Python Flask**, **SQLite**, **SQLAlchemy**, **Bootstrap 5**, **HTML**, **CSS**, and **JavaScript**. The system provides an easy way for librarians to manage books, students, categories, and book transactions through a simple web interface.

---

## 🚀 Features

* 🔐 Admin Login Authentication
* 📖 Add, Edit, Delete, and View Books
* 👨‍🎓 Add, Edit, Delete, and View Students
* 📂 Manage Book Categories
* 📚 Issue Books to Students
* 📥 Return Issued Books
* 📊 Dashboard with Library Statistics
* 🔍 Search Books
* 📱 Responsive User Interface using Bootstrap 5

---

## 🛠️ Technologies Used

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## 📂 Project Structure

```
LibraryManagementSystem/
│
├── app.py
├── config.py
├── models.py
├── requirements.txt
│
├── routes/
│   ├── auth.py
│   ├── dashboard.py
│   ├── books.py
│   ├── students.py
│   ├── categories.py
│   ├── transactions.py
│   └── reports.py
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── books/
│   ├── students/
│   ├── categories/
│   ├── transactions/
│   └── reports/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── library.db
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/LibraryManagementSystem.git
```

### 2. Navigate to the project

```bash
cd LibraryManagementSystem
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

## 🔑 Default Admin Login

If your project creates a default admin account automatically, use:

**Username:** `admin`

**Password:** `admin123`

---

## 📸 Screenshots

You can add screenshots of:

* Login Page
* Dashboard
* Books Management
* Students Management
* Categories
* Issue Book
* Return Book

---

## 📈 Future Improvements

* Barcode/QR Code Support
* Fine Calculation for Late Returns
* Email Notifications
* Export Reports to PDF and Excel
* Student Login Portal
* Book Reservation System
* Dark Mode

---

## 👩‍💻 Author

**Sayyada Ummay Hani**

GitHub: https://github.com/ummay-hani31

---

## 📄 License

This project is developed for educational purposes.
