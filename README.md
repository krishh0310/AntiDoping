# 🛡️ Anti-Doping Awareness Platform

A comprehensive, web-based educational platform built with **Django 6.0** and **AI (Groq LLaMA 3.1)** to promote anti-doping awareness among students, athletes, coaches, and sports professionals. The platform delivers a structured learning path with interactive modules, per-module quizzes, a final assessment, AI-powered Q&A, live updates, and certificate generation — all wrapped in a clean, responsive, modern UI.

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Django](https://img.shields.io/badge/Django-6.0-green?logo=django)
![AI](https://img.shields.io/badge/AI-Groq%20LLaMA%203.1-orange?logo=meta)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots & Pages](#-screenshots--pages)
- [Tech Stack](#-tech-stack)
- [Architecture & Project Structure](#-architecture--project-structure)
- [Data Models](#-data-models)
- [URL Routes & API Endpoints](#-url-routes--api-endpoints)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Admin Panel Setup](#-admin-panel-setup)
- [How the Learning Path Works](#-how-the-learning-path-works)
- [AI Chatbot](#-ai-chatbot)
- [Security Features](#-security-features)
- [Responsive Design](#-responsive-design)
- [Dependencies](#-dependencies)
- [Configuration Reference](#-configuration-reference)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)
- [Contact](#-contact)

---

## 🌍 Overview

Doping in sports is a global issue that undermines fair play, endangers athlete health, and erodes public trust. This platform was created to educate users — especially young athletes and students — about:

- **What doping is** and the categories of prohibited substances
- **Health risks** associated with performance-enhancing drugs
- **The role of WADA** (World Anti-Doping Agency) and national anti-doping organizations
- **Doping control procedures** — from sample collection to laboratory analysis
- **Fair play and ethics** — why clean sport matters

Users progress through a **sequential, guided learning path**: read each module (broken into digestible parts), pass the module quiz (≥60%), unlock the next module, and finally take a comprehensive final assessment to earn a **downloadable certificate of completion**.

---

## ✨ Features

### 📚 Structured Learning Modules
- Multi-part educational modules on anti-doping topics
- Each module is divided into **ordered parts** (e.g., Part 1, Part 2, Part 3) for digestible reading
- **Sequential access control** — modules are locked until the previous module's quiz is passed
- Visual **progress tracking** with progress bars and step indicators on every page
- **Breadcrumb navigation** for easy orientation within the course
- Previous/Next navigation between parts with a clear step indicator (Part 1 → Part 2 → Part 3 → Quiz)

### 📝 Module Quizzes
- Each module has its own set of **multiple-choice questions** (4 options: A, B, C, D)
- **60% passing score** required to unlock the next module
- Instant results with score, percentage, and pass/fail feedback
- Clear call-to-action: proceed to the next module (if passed) or review and retry (if failed)
- Student name input for personalized result tracking

### 🏆 Final Quiz & Certificate
- Comprehensive **final assessment** with standalone questions (not tied to any single module)
- Real-time **progress bar** that fills as questions are answered
- Beautiful, **print-ready certificate** generated upon passing (≥60%)
- Certificate includes: student name, score, percentage, year, certificate ID, and signature lines
- **Print / Save as PDF** button with print-optimized CSS (hides navbar, footer, and action buttons)
- Certificate access is restricted — only passing results can generate a certificate

### 🤖 AI Chatbot (Groq LLaMA 3.1)
- Powered by the **Groq API** using the `llama-3.1-8b-instant` model
- System prompt tuned for anti-doping awareness: _"You are an anti-doping awareness assistant. Keep answers clear and student-friendly."_
- Chat-style UI with user/bot message bubbles, avatars, and a typing animation
- **Copy-to-clipboard** button on every bot response
- **Rate limiting**: max 20 messages per minute per session
- Input validation: messages capped at 1,000 characters, empty messages rejected
- Secure: CSRF-protected POST endpoint, no internal error details exposed to client
- Temperature set to `0.4` for factual, consistent responses with max `400` tokens

### 📢 Updates Feed
- Admin-managed news and updates displayed in reverse chronological order
- **Pinned banner** reminding users that WADA updates the Prohibited List annually
- **Live badge** with a pulsing red dot indicator
- Color-coded update icons (red, blue, green, gold) rotating per update
- Relative timestamps ("3 hours ago", "2 days ago")
- **Auto-refresh** every 30 seconds with a visible countdown timer

### 📱 Responsive Design
- Fully mobile-friendly with responsive breakpoints at `768px` and `600px`
- **Hamburger menu** for mobile navigation with smooth toggle animation
- Fluid typography using `clamp()` for headings
- Grid layouts that gracefully collapse on smaller screens
- Touch-friendly tap targets and input fields

### 🔒 Security
- **CSRF protection** on all POST endpoints (quiz submissions, chat API)
- **Content Security Policy (CSP)** headers preventing XSS attacks
- **Strict Referrer Policy** (`strict-origin-when-cross-origin`)
- **Input validation & sanitization** — student names are regex-validated, stripped, and capped at 100 characters
- **Rate limiting** on the chatbot API (20 requests/minute per session, enforced server-side)
- **Session security** — 1-hour session expiry, `HttpOnly` cookies, `SameSite=Lax`, secure cookies in production
- **HSTS** (HTTP Strict Transport Security) enabled in production with preloading
- **X-Frame-Options: DENY** to prevent clickjacking
- **XSS Filter** and **Content-Type Nosniff** headers enabled
- Environment-based configuration — secrets loaded from `.env`, never hardcoded
- `SECRET_KEY` validation — app refuses to start with the default key

---

## 🖥️ Screenshots & Pages

The platform consists of the following pages:

| Page | URL | Description |
|------|-----|-------------|
| **Home** | `/` | Hero section with course stats, module preview cards, feature highlights, and CTA banner |
| **Modules List** | `/modules/` | All modules listed with progress bar, status badges (Done / Start → / 🔒 Locked) |
| **Module Detail** | `/module/<id>/` | Module content view (redirects to first part if parts exist) |
| **Module Part** | `/module/<id>/part/<order>/` | Individual part content with step progress indicator |
| **Module Quiz** | `/module/<id>/quiz/` | Per-module quiz with name input and multiple-choice questions |
| **Final Quiz** | `/quiz/` | Comprehensive final assessment with progress bar |
| **Certificate** | `/certificate/<result_id>/` | Print-ready certificate of completion |
| **AI Chatbot** | `/chatbot/` | Interactive AI-powered Q&A interface |
| **Updates** | `/updates/` | News feed with auto-refresh |
| **Error** | _(rendered on access denial)_ | Friendly error page with return-to-home link |
| **Admin** | `/admin/` | Django admin panel for managing all content |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django 6.0.3, Python 3.13 | Web framework, ORM, admin, sessions, security |
| **AI / Chatbot** | Groq API (`groq` 1.1.1), LLaMA 3.1 8B Instant | Real-time conversational AI for anti-doping Q&A |
| **Database** | SQLite 3 | Lightweight default database (easily swappable) |
| **Frontend** | HTML5, CSS3 (custom), Vanilla JavaScript | No frontend framework — clean, fast, dependency-free |
| **Fonts** | Google Fonts (Syne, DM Sans) | Modern typography — Syne for headings, DM Sans for body |
| **Icons** | Bootstrap Icons 1.11.3 (CDN) | Consistent iconography across all pages |
| **HTTP Client** | httpx 0.28.1 (via Groq SDK) | Async HTTP requests for the Groq API |
| **Validation** | Pydantic 2.12.5 (via Groq SDK) | Data validation for API responses |
| **Config** | python-dotenv 1.2.2 | Environment variable management from `.env` files |
| **Server** | WSGI (Django built-in) / ASGI (optional) | Development server; production-ready with Gunicorn/Daphne |

---

## 🏗️ Architecture & Project Structure

```
AntiDoping/                         # Root project directory
│
├── manage.py                       # Django management CLI entry point
├── requirements.txt                # Python dependencies (pinned versions)
├── db.sqlite3                      # SQLite database file (auto-generated)
├── LICENSE                         # MIT License
├── README.md                       # This file
├── .env                            # Environment variables (create manually, not committed)
│
├── AntiDoping/                     # Django project configuration package
│   ├── __init__.py                 # Package initializer
│   ├── settings.py                 # All Django settings (security, DB, templates, static, etc.)
│   ├── urls.py                     # Root URL config — includes admin + base app URLs
│   ├── wsgi.py                     # WSGI application entry point (for production deployment)
│   └── asgi.py                     # ASGI application entry point (for async deployment)
│
└── base/                           # Main application — all features live here
    ├── __init__.py                 # Package initializer
    ├── apps.py                     # App configuration (BaseConfig)
    ├── models.py                   # Database models: Module, ModulePart, QuizQuestion, QuizResult, Update
    ├── views.py                    # All view functions + AI chatbot API endpoint
    ├── urls.py                     # URL routing — 10 routes including API
    ├── admin.py                    # Admin panel customization with inline editing
    ├── tests.py                    # Test file (extendable)
    │
    ├── templates/                  # Django HTML templates
    │   ├── base.html               # Base layout — navbar, footer, CSS variables, mobile menu
    │   ├── home.html               # Landing page — hero, module cards, features, CTA
    │   ├── modules.html            # Module listing — progress bar, locked/unlocked/done states
    │   ├── module_detail.html      # Single module view — breadcrumbs, content card, navigation
    │   ├── module_part.html        # Part-by-part view — step indicators, prev/next navigation
    │   ├── module_quiz.html        # Per-module quiz — question cards, result banner
    │   ├── final_quiz.html         # Final assessment — progress bar, result banner, cert link
    │   ├── certificate.html        # Print-ready certificate — scores, stamps, signatures
    │   ├── chatbot.html            # AI chat interface — message bubbles, typing animation
    │   ├── updates.html            # News feed — pinned banner, live badge, auto-refresh
    │   └── error.html              # Error page — friendly message with return link
    │
    ├── static/
    │   └── css/
    │       └── style.css           # Additional static CSS
    │
    └── migrations/                 # Django database migrations (auto-generated)
        ├── __init__.py
        ├── 0001_initial.py
        ├── 0002_remove_quizresult_name_quizresult_student_name.py
        ├── 0003_alter_quizresult_student_name.py
        ├── 0004_alter_module_options_rename_body_update_...py
        └── 0005_alter_module_content_modulepart.py
```

---

## 🗄️ Data Models

### `Module`
The core learning unit. Each module represents a topic (e.g., "What is Doping?").

| Field | Type | Description |
|-------|------|-------------|
| `title` | `CharField(200)` | Module title |
| `content` | `TextField` | Module content (used when no parts exist; blank allowed) |
| `order` | `IntegerField` | Display & access order (ascending) |

- **Ordering**: by `order` field (ascending)
- **Relation**: Has many `ModulePart` objects (via `parts` related name)
- **Relation**: Has many `QuizQuestion` objects (via `questions` related name)

### `ModulePart`
Breaks a module into smaller, sequential reading sections.

| Field | Type | Description |
|-------|------|-------------|
| `module` | `ForeignKey(Module)` | Parent module (CASCADE delete) |
| `title` | `CharField(200)` | Part title (e.g., "Types of Banned Substances") |
| `content` | `TextField` | Part content body |
| `order` | `IntegerField` | Part order within the module |

- **Ordering**: by `order` field (ascending)
- If a module has parts, visiting the module auto-redirects to the first part

### `QuizQuestion`
Multiple-choice questions for module quizzes or the final assessment.

| Field | Type | Description |
|-------|------|-------------|
| `module` | `ForeignKey(Module)` | Associated module (`null` = final quiz question) |
| `question` | `CharField(255)` | The question text |
| `option_a` | `CharField(200)` | Option A |
| `option_b` | `CharField(200)` | Option B |
| `option_c` | `CharField(200)` | Option C |
| `option_d` | `CharField(200)` | Option D |
| `correct_option` | `CharField(1)` | Correct answer: `A`, `B`, `C`, or `D` |

- Questions with `module=None` appear in the **Final Quiz**
- Questions with a module assigned appear in that **Module's Quiz**

### `QuizResult`
Stores every quiz attempt (both module quizzes and final quiz).

| Field | Type | Description |
|-------|------|-------------|
| `student_name` | `CharField(100)` | Participant's name (default: "Participant") |
| `score` | `IntegerField` | Number of correct answers |
| `total` | `IntegerField` | Total number of questions |
| `module` | `ForeignKey(Module)` | Associated module (`null` = final quiz result) |
| `created_at` | `DateTimeField` | Auto-set timestamp |

- Final quiz results (`module=None`) are used for **certificate generation**
- Certificate access requires a passing score (≥60%)

### `Update`
Admin-managed news/announcements for the updates feed.

| Field | Type | Description |
|-------|------|-------------|
| `title` | `CharField(200)` | Update headline |
| `message` | `TextField` | Update body content |
| `created_at` | `DateTimeField` | Auto-set timestamp |

---

## 🔗 URL Routes & API Endpoints

### Page Routes

| Method | URL Pattern | View Function | Description |
|--------|-------------|---------------|-------------|
| `GET` | `/` | `home` | Landing page with hero, stats, module previews |
| `GET` | `/modules/` | `modules_list` | List all modules with progress & lock status |
| `GET` | `/module/<int:module_id>/` | `module_detail` | Module content (redirects to first part if parts exist) |
| `GET` | `/module/<id>/part/<order>/` | `module_part` | Individual part within a module |
| `GET/POST` | `/module/<id>/quiz/` | `module_quiz` | Per-module quiz (GET: form, POST: submit & grade) |
| `GET/POST` | `/quiz/` | `final_quiz` | Final assessment (GET: form, POST: submit & grade) |
| `GET` | `/chatbot/` | `chatbot` | AI chatbot interface |
| `GET` | `/updates/` | `updates` | News & updates feed |
| `GET` | `/certificate/<result_id>/` | `certificate` | Certificate (only for passing final quiz results) |
| `GET` | `/admin/` | _(Django admin)_ | Admin panel for managing all content |

### API Endpoints

| Method | URL | View Function | Description |
|--------|-----|---------------|-------------|
| `POST` | `/api/chat/` | `chat_api` | AI chatbot — accepts `{ "message": "..." }`, returns `{ "reply": "..." }` |

**Chat API Details:**
- **Request**: `POST /api/chat/` with `Content-Type: application/json` and `X-CSRFToken` header
- **Request Body**: `{ "message": "What is EPO?" }` (max 1,000 characters)
- **Success Response**: `200 OK` — `{ "reply": "EPO stands for..." }`
- **Error Responses**:
  - `400` — Invalid JSON or empty message
  - `429` — Rate limit exceeded (20 req/min)
  - `500` — API not configured or processing error

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.10+** (developed with Python 3.13)
- **pip** (Python package manager)
- A **[Groq API key](https://console.groq.com/)** (free tier available — required for the chatbot)

### Step-by-Step Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/krishh0310/AntiDoping.git
cd AntiDoping
```

#### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Set Up Environment Variables

Create a `.env` file in the project root (`AntiDoping/.env`):

```env
# Required — Django will refuse to start without a proper secret key
SECRET_KEY=your-unique-random-secret-key-here

# Required — Get your free key at https://console.groq.com/
GROQ_API_KEY=gsk_your_groq_api_key_here

# Optional — Set to 'true' for development (enables debug mode)
DEBUG=true

# Optional — Comma-separated allowed hosts (defaults to localhost,127.0.0.1)
ALLOWED_HOSTS=localhost,127.0.0.1
```

> **💡 Tip:** Generate a strong secret key with:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

#### 5. Run Database Migrations

```bash
python manage.py migrate
```

This creates the SQLite database and all required tables.

#### 6. Create a Superuser (Admin Account)

```bash
python manage.py createsuperuser
```

You'll be prompted for a username, email, and password. This account is used to manage content via the admin panel.

#### 7. Start the Development Server

```bash
python manage.py runserver
```

#### 8. Open in Browser

- **Platform**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔑 Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `SECRET_KEY` | ✅ Yes | `CHANGE-ME-IN-PRODUCTION` (raises error) | Django secret key for cryptographic signing |
| `GROQ_API_KEY` | ✅ Yes (for chatbot) | `""` (empty) | Groq API key for the AI chatbot |
| `DEBUG` | ❌ No | `False` | Set to `true` for development mode |
| `ALLOWED_HOSTS` | ❌ No | `localhost,127.0.0.1` | Comma-separated list of allowed hostnames |

> ⚠️ **Important**: The application will **raise a `ValueError`** on startup if `SECRET_KEY` is not set. This is intentional to prevent running with insecure defaults.

---

## ⚙️ Admin Panel Setup

After creating a superuser, visit `/admin/` to manage all content.

### Adding Modules

1. Go to **Admin → Modules → Add Module**
2. Set the **title**, **order** (determines sequence), and optionally **content** (for single-page modules)
3. Add **Module Parts** inline — set order, title, and content for each part
4. Save. Parts with `order = 1, 2, 3` will display as "Part 1 → Part 2 → Part 3 → Quiz"

### Adding Quiz Questions

1. Go to **Admin → Quiz Questions → Add Quiz Question**
2. Write the question, fill in options A–D, and set the **correct option** (`A`, `B`, `C`, or `D`)
3. **Assign to a module** → the question appears in that module's quiz
4. **Leave module blank** → the question appears in the **Final Quiz**

### Admin Panel Features

| Model | Admin Features |
|-------|---------------|
| **Module** | List display: order & title. Inline editing of ModuleParts (3 extra blank rows). Ordered by `order`. |
| **QuizQuestion** | List display: question, module, correct_option. Filterable by module. |
| **QuizResult** | Default list view. Records all quiz attempts with scores. |
| **Update** | Default list view. Add news/updates that appear on the Updates page. |

---

## 📖 How the Learning Path Works

The platform enforces a **strict sequential progression**:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Module 1   │ ──▶ │  Module 2   │ ──▶ │  Module 3   │ ──▶ │  Module N   │
│  (3 Parts)  │     │  (3 Parts)  │     │  (3 Parts)  │     │  (3 Parts)  │
│   + Quiz    │     │   + Quiz    │     │   + Quiz    │     │   + Quiz    │
│  Pass ≥60%  │     │  Pass ≥60%  │     │  Pass ≥60%  │     │  Pass ≥60%  │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                    │
                                                                    ▼
                                                            ┌───────────────┐
                                                            │  Final Quiz   │
                                                            │  Pass ≥60%    │
                                                            └───────┬───────┘
                                                                    │
                                                                    ▼
                                                            ┌───────────────┐
                                                            │ 🏆 Certificate │
                                                            └───────────────┘
```

### Detailed Flow

1. **Module 1** is always accessible (no prerequisites)
2. Within a module, users read **Part 1 → Part 2 → Part 3** sequentially using Previous/Next buttons
3. After reading all parts, users click **"Take Quiz"** to access the module quiz
4. Quiz requires a **student name** and answering all multiple-choice questions
5. Upon submission, the system calculates the score and shows:
   - **≥60%**: ✅ Passed — next module is unlocked, "Next Module" button appears
   - **<60%**: ❌ Not passed — "Re-read Module" and "Try Again" buttons appear
6. Progress is tracked via **Django sessions** (`passed_modules` list)
7. After all modules are passed, users take the **Final Quiz**
8. Passing the final quiz (≥60%) generates a **certificate** accessible via `/certificate/<id>/`
9. The certificate can be **printed or saved as PDF** using the browser's print functionality

### Access Control Logic

The `_verify_module_access()` function enforces sequential access:
- Checks the user's `passed_modules` session data
- Module 1 (index 0) is always accessible
- Module N requires Module N-1 to be in `passed_modules`
- Unauthorized access returns a **403 error page** with a friendly message

### Student Name Validation

The `_validate_student_name()` function sanitizes all name inputs:
- Strips whitespace and caps at 100 characters
- Only allows: letters, numbers, spaces, hyphens, and apostrophes
- Invalid names default to `"Participant"`

---

## 🤖 AI Chatbot

### How It Works

The chatbot uses the **Groq API** with the `llama-3.1-8b-instant` model to provide instant answers about anti-doping topics.

### Technical Details

| Setting | Value |
|---------|-------|
| **Model** | `llama-3.1-8b-instant` |
| **Temperature** | `0.4` (factual, low creativity) |
| **Max Tokens** | `400` |
| **System Prompt** | "You are an anti-doping awareness assistant. Keep answers clear and student-friendly." |
| **Rate Limit** | 20 messages/minute per session |
| **Max Input Length** | 1,000 characters |

### Frontend Features

- **Chat-style UI** with distinct user (🧑) and bot (🤖) avatars
- **Typing indicator** with animated bouncing dots while waiting for a response
- **Copy button** on every bot message for easy text copying
- **Enter key** sends messages (no need to click the button)
- **XSS protection** — all user input is HTML-escaped before rendering; bot responses are sanitized with bold/italic markdown support
- **Error handling** — network errors and API failures show friendly warning messages

### Getting a Groq API Key

1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Sign up or log in with your account
3. Navigate to **API Keys** and create a new key
4. Copy the key (starts with `gsk_`) and add it to your `.env` file
5. Groq offers a generous **free tier** — no credit card required

---

## 🔐 Security Features

### Server-Side Security

| Feature | Implementation |
|---------|---------------|
| **CSRF Protection** | Django's built-in `CsrfViewMiddleware` + `@csrf_protect` on API endpoints |
| **Secret Key Validation** | App refuses to start if `SECRET_KEY` is not configured |
| **Input Sanitization** | Regex validation on student names; message length limits on chat API |
| **Rate Limiting** | Session-based rate limiter on `/api/chat/` (20 req/min, sliding window) |
| **Error Concealment** | Internal errors return generic messages; no stack traces exposed to users |
| **Session Security** | 1-hour expiry, `HttpOnly` flag, `SameSite=Lax`, browser-close expiry |

### HTTP Security Headers

| Header | Value | Purpose |
|--------|-------|---------|
| **Content-Security-Policy** | Restricts sources for scripts, styles, fonts, images, connections | Prevents XSS, data injection |
| **Referrer-Policy** | `strict-origin-when-cross-origin` | Limits referrer data leakage |
| **X-Frame-Options** | `DENY` | Prevents clickjacking |
| **X-Content-Type-Options** | `nosniff` | Prevents MIME type sniffing |
| **X-XSS-Protection** | `1; mode=block` | Legacy XSS filter |
| **Strict-Transport-Security** | `max-age=31536000; includeSubDomains; preload` (production only) | Forces HTTPS |

### Production vs Development

| Setting | `DEBUG=true` | `DEBUG=false` (Production) |
|---------|-------------|---------------------------|
| SSL Redirect | ❌ Off | ✅ Enabled |
| Secure Cookies | ❌ Off | ✅ Enabled |
| HSTS | ❌ Off | ✅ 1 year with preload |
| CSRF Secure Cookie | ❌ Off | ✅ Enabled |

---

## 📱 Responsive Design

The UI is built with a **mobile-first philosophy** using CSS custom properties and responsive breakpoints:

### CSS Design System

```
Fonts:     Syne (headings) + DM Sans (body)
Colors:    --ink (#0f2b26), --gold (#d4890e), --green (#0dab76), --red (#cf3a3a)
Radii:     8px (sm) → 14px → 22px (lg) → 32px (xl)
Shadows:   3-tier system (sm, default, lg)
```

### Breakpoints

| Breakpoint | Changes |
|------------|---------|
| `≤ 1024px` | Feature grid reduces columns |
| `≤ 768px` | Hamburger menu activates; padding reduces; hero compresses; single-column layouts |
| `≤ 600px` | Quiz options switch to single column; certificate body padding reduces |

### Key Responsive Features

- **Sticky navbar** with hamburger toggle for mobile
- **`clamp()`-based headings** that scale fluidly from mobile to desktop
- **CSS Grid** with `auto-fill` / `auto-fit` for automatic column adjustment
- **Flex-wrap** on all multi-item layouts for graceful degradation
- **Print stylesheet** (`@media print`) on the certificate page hides navigation elements

---

## 📦 Dependencies

All dependencies are pinned in `requirements.txt`:

| Package | Version | Purpose |
|---------|---------|---------|
| `Django` | 6.0.3 | Web framework |
| `groq` | 1.1.1 | Groq API client for LLaMA 3.1 |
| `python-dotenv` | 1.2.2 | `.env` file loader |
| `httpx` | 0.28.1 | Modern HTTP client (used by Groq SDK) |
| `pydantic` | 2.12.5 | Data validation (used by Groq SDK) |
| `sqlparse` | 0.5.5 | SQL parsing (Django dependency) |
| `asgiref` | 3.11.1 | ASGI utilities (Django dependency) |
| `certifi` | 2026.2.25 | SSL certificates |
| `idna` | 3.11 | Internationalized domain names |
| `sniffio` | 1.3.1 | Async library detection |
| `anyio` | 4.12.1 | Async compatibility layer |
| `h11` | 0.16.0 | HTTP/1.1 protocol implementation |
| `httpcore` | 1.0.9 | HTTP transport library |
| `distro` | 1.9.0 | OS distribution detection |
| `annotated-types` | 0.7.0 | Type annotation extensions |
| `typing-inspection` | 0.4.2 | Typing introspection utilities |
| `typing_extensions` | 4.15.0 | Backported typing features |
| `pydantic_core` | 2.41.5 | Pydantic core validation engine |

---

## ⚙️ Configuration Reference

Key settings in `AntiDoping/settings.py`:

| Setting | Value | Description |
|---------|-------|-------------|
| `DEBUG` | Env-based (`False` default) | Enables debug mode when `true` |
| `ALLOWED_HOSTS` | Env-based (`localhost,127.0.0.1`) | Hosts allowed to serve the app |
| `DATABASES` | SQLite (`db.sqlite3`) | Default file-based database |
| `SESSION_COOKIE_AGE` | `3600` (1 hour) | Session timeout duration |
| `SESSION_EXPIRE_AT_BROWSER_CLOSE` | `True` | Sessions expire when browser closes |
| `STATIC_URL` | `static/` | URL prefix for static files |
| `STATICFILES_DIRS` | `base/static/` | Additional static file directories |
| `TEMPLATES.DIRS` | `base/templates/` | Template search directory |

---

## 🔧 Troubleshooting

### Common Issues

| Problem | Solution |
|---------|----------|
| `ValueError: SECRET_KEY environment variable is not set` | Create a `.env` file with `SECRET_KEY=your-key-here` |
| Chatbot returns "API not configured" | Ensure `GROQ_API_KEY` is set in `.env` and the server is restarted |
| Chatbot returns "Too many requests" | Wait 60 seconds — rate limit is 20 messages/minute |
| Module shows "Access denied" | Complete and pass the previous module's quiz first |
| Certificate page shows "Access denied" | Only passing final quiz results (≥60%) can access certificates |
| "No questions added for this module yet" | Go to Admin → Quiz Questions → add questions and assign them to the module |
| "No final quiz questions have been added yet" | Go to Admin → Quiz Questions → add questions **without** assigning a module |
| Database errors after model changes | Run `python manage.py makemigrations` then `python manage.py migrate` |
| Static files not loading | Ensure `DEBUG=true` for development, or configure `collectstatic` for production |
| Module progress resets | Progress is session-based — clearing cookies/sessions resets progress |

### Resetting the Database

```bash
rm db.sqlite3
python manage.py migrate
python manage.py createsuperuser
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/AntiDoping.git
   cd AntiDoping
   ```
3. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make** your changes and test thoroughly
5. **Commit** with a clear message:
   ```bash
   git commit -m "Add: brief description of your change"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. **Open** a Pull Request on the main repository

### Ideas for Contributions

- 🌐 **Internationalization (i18n)** — Translate the platform to other languages
- 📊 **Analytics Dashboard** — Track user progress, quiz scores, completion rates
- 🔐 **User Authentication** — Add login/registration for persistent progress tracking
- 📧 **Email Certificates** — Send certificates via email upon completion
- 🎨 **Dark Mode** — Add a dark theme toggle
- 📱 **PWA Support** — Make the platform installable as a Progressive Web App
- 🧪 **Unit Tests** — Add comprehensive test coverage for views and models
- 🗃️ **PostgreSQL Support** — Production-grade database configuration
- 🐳 **Docker Support** — Add Dockerfile and docker-compose for easy deployment

---

## 📄 License

This project is licensed under the **MIT License**.

Copyright © 2026 **Kadempally Sai Krish Karthik**

See the [LICENSE](LICENSE) file for full details.

---

## 📬 Contact

Built with ❤️ by **[@krishh0310](https://github.com/krishh0310)**

- 🐙 GitHub: [github.com/krishh0310](https://github.com/krishh0310)
- 📂 Repository: [github.com/krishh0310/AntiDoping](https://github.com/krishh0310/AntiDoping)

---

<div align="center">

**⭐ If you found this project useful, please give it a star on GitHub! ⭐**

</div>
