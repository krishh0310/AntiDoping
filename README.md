# 🛡️ Anti-Doping Awareness Platform

A web-based educational platform built with **Django** and **AI** to promote anti-doping awareness among students and athletes. The platform features interactive learning modules, quizzes, an AI-powered chatbot, and certificate generation.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?logo=django)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

- **📚 Learning Modules** — Structured, multi-part educational modules on anti-doping topics with sequential access control
- **📝 Module Quizzes** — Quiz after each module to test understanding (60% passing score required to unlock the next module)
- **🏆 Final Quiz & Certificate** — Comprehensive final quiz with a downloadable certificate upon passing
- **🤖 AI Chatbot** — Powered by Groq (LLaMA 3.1) for instant anti-doping Q&A
- **📢 Updates Feed** — Latest news and updates on anti-doping regulations
- **📱 Responsive Design** — Fully mobile-friendly with a clean, modern UI
- **🔒 Security** — CSRF protection, Content Security Policy, input validation, and rate limiting

---

## 🛠️ Tech Stack

| Layer      | Technology                          |
|------------|-------------------------------------|
| Backend    | Django 6.0, Python 3.13             |
| Frontend   | HTML, CSS, JavaScript               |
| AI/Chatbot | Groq API (LLaMA 3.1 8B Instant)    |
| Database   | SQLite (default)                    |
| Fonts      | Google Fonts (Syne, DM Sans)        |
| Icons      | Bootstrap Icons                     |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- A [Groq API key](https://console.groq.com/) (for the chatbot feature)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/krishh0310/AntiDoping.git
   cd AntiDoping
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate        # macOS/Linux
   venv\Scripts\activate           # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   DJANGO_SECRET_KEY=your_secret_key_here
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser** (to add modules & questions via admin)
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 📁 Project Structure

```
AntiDoping/
├── AntiDoping/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── base/                # Main app
│   ├── models.py        # Module, ModulePart, QuizQuestion, QuizResult, Update
│   ├── views.py         # All view logic including AI chatbot
│   ├── urls.py          # URL routing
│   ├── admin.py         # Admin panel configuration
│   ├── templates/       # HTML templates
│   │   ├── base.html          # Base layout with navbar & footer
│   │   ├── home.html          # Landing page
│   │   ├── modules.html       # Module listing
│   │   ├── module_detail.html # Module content
│   │   ├── module_part.html   # Multi-part module view
│   │   ├── module_quiz.html   # Per-module quiz
│   │   ├── final_quiz.html    # Final assessment
│   │   ├── certificate.html   # Certificate generation
│   │   ├── chatbot.html       # AI chatbot interface
│   │   ├── updates.html       # News & updates
│   │   └── error.html         # Error page
│   └── static/
│       └── css/style.css
├── manage.py
├── requirements.txt
└── db.sqlite3
```

---

## 🔐 Security Features

- **CSRF Protection** on all POST endpoints
- **Content Security Policy (CSP)** headers to prevent XSS
- **Input Validation & Sanitization** for user inputs
- **Rate Limiting** on chatbot API (20 requests/minute per session)
- **Strict Referrer Policy** for privacy

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📬 Contact

Built by [@krishh0310](https://github.com/krishh0310)
