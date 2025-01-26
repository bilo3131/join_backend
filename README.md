# Join

## Description
Join is a Kanban board that allows users to efficiently organize their tasks. It provides registration and login functionality, as well as the ability to create tasks and contacts. The key features of the project include:

- **Tasks:**
  - Fields: Title, Description, Category (business-oriented), Due Date (future only), Priority (Low, Medium, Urgent), and optional Subtasks.
  - Tasks can be assigned to contacts.
  - Drag-and-drop functionality for process management on the board.

- **Contacts:**
  - Add contacts with phone numbers and email addresses.
  - Link contacts to tasks.

- **Main Pages:**
  - **Summary:** Overview of all tasks, including:
    - Number of todos, in progress, awaiting feedback, and completed tasks.
    - Count of "Urgent" tasks and the next due date.
  - **Board:** Manage tasks using drag-and-drop functionality.
  - **Add Task:** Create new tasks.
  - **Contacts:** Add and manage contacts.

Additional Pages:
- Login, Registration, Help, Privacy Policy, and Imprint.

All data is stored and retrieved from an SQLite database.

---

## Technologies
- **Frontend:** JavaScript
- **Backend:** Python (Django)
- **Database:** SQLite

---

## Repositories
This project is split into two repositories on GitHub:
- **Frontend Repository:** [join_frontend](https://github.com/bilo3131/join_frontend)
- **Backend Repository:** [join_backend](https://github.com/bilo3131/join_backend)

---

## Installation
### Prerequisites
- **Python 3.x** installed
- **Node.js** (if additional frontend tools are required)

### Steps
1. **Clone the repositories:**
   ```bash
   git clone https://github.com/bilo3131/join_frontend.git
   git clone https://github.com/bilo3131/join_backend.git
   ```

2. **Install backend dependencies:**
   ```bash
   cd join-backend
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies:**
   (If necessary, e.g., when using a build system)
   ```bash
   cd join-frontend
   npm install
   ```

---

## Usage
### Start the backend
```bash
cd join-backend
python manage.py runserver
```
The backend will be available at `http://127.0.0.1:8000`.

### Start the frontend
If no build system is used, open the HTML files directly in the browser or use a local server tool.

---

## Features
- Registration and login.
- Create and manage tasks with drag-and-drop functionality.
- Add and assign contacts.
- Task summary with statistics.

---

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Make your changes and commit them:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push your changes:
   ```bash
   git push origin feature-name
   ```
5. Create a pull request.

---

## License
This project is proprietary. You are permitted to clone, run, and modify the project for personal use only. Redistribution or any form of public use, including commercial purposes, is strictly prohibited without explicit permission from the author.

