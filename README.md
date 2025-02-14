# MatchMate ⚽

Welcome to **MatchMate**, your ultimate sports management platform! This web application helps sports enthusiasts, clubs, and teams manage their players, schedules, and match details efficiently.

## 🏆 Features

- **Club Management**: View featured clubs with detailed profiles.
- **Player Management**: Track player statistics and details.
- **Team Collaboration**: Connect with teams and players.
- **Responsive UI**: Built with Vue.js and Quasar for a smooth experience.
- **Backend API**: Powered by Flask, handling data efficiently.

## 🚀 Tech Stack

### Frontend:

- Vue.js (Vite)
- Quasar Framework

### Backend:

- Python (Flask)
- SQLAlchemy (Database ORM)
- SQLite (Database)

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

If cloning does not work, download the code as a ZIP file and extract it.

```sh
git clone https://github.com/yourusername/matchmate.git
cd MatchMate
```

### 2️⃣ Backend Setup (Flask)

```sh
cd matchmate/app_matchmate
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
python run.py  # or flask run
```

The backend will run on [**http://127.0.0.1:5000**](http://127.0.0.1:5000) by default.

### 3️⃣ Frontend Setup (Vue.js + Vite)

```sh
cd frontend
npm install
npm run dev
```

The frontend will run on [**http://localhost:5173**](http://localhost:5173) by default.

---

## 🛠️ Important Note

When running the application for the first time, the database will be empty. To populate it with data, use the Swagger API documentation to add clubs, players, and teams manually. Without this step, the frontend will not display any data.

---

## 📌 API Documentation

- The API documentation is available via Swagger.
- Run the backend and visit `http://127.0.0.1:5000/apidocs/#/` for API details.

---

## 📌 Deployment

- **Frontend:** Can be deployed using Netlify, Vercel, or any static hosting service.
- **Backend:** Deploy using Flask on AWS/GCP/Heroku with SQLite.

---

## 🤝 Contributing

Feel free to fork and contribute! Open a pull request with improvements.

---

## 🐟 License

This project is licensed under the MIT License.

---

🚀 **MatchMate - Connecting Players, Teams & Clubs!**

