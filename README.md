# 🐍 100 Python Projects

> A personal journey from **beginner to professional** — one project at a time.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Projects](https://img.shields.io/badge/Projects-100-green?style=flat-square)
![Level](https://img.shields.io/badge/Level-Beginner%20→%20Professional-orange?style=flat-square)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow?style=flat-square)

---

## 📖 About This Repository

This repository is my commitment to becoming a proficient Python developer through **deliberate practice**. Each project is built with the intent to **learn by doing** — not just reading or watching tutorials.

The projects are organized across four difficulty tiers, starting from CLI tools and command-line fundamentals, all the way up to production-grade applications. Every project here represents a real, working piece of software — not just toy snippets.

**What you'll find here:**
- Projects ranging from beginner to professional level
- Clean, well-commented code focused on readability
- A learning log for each project explaining what was practiced
- Progressive complexity — each tier builds on the last

---

## 🗂️ Project Tiers

### 🟢 Tier 1 — Beginner (Projects 1–25)
*Focus: Python fundamentals, CLI tools, file I/O, basic logic*

| # | Project | Key Concepts | Status |
|---|---------|--------------|--------|
| 01 | [CLI Task Manager](#) | argparse, file I/O, lists, CRUD | ✅ Done |
| 02 | Coming soon... | | 🔜 |
| ... | | | |

---

### 🟡 Tier 2 — Intermediate (Projects 26–50)
*Focus: OOP, APIs, databases, automation*

| # | Project | Key Concepts | Status |
|---|---------|--------------|--------|
| 26 | Coming soon... | | 🔜 |
| ... | | | |

---

### 🟠 Tier 3 — Advanced (Projects 51–75)
*Focus: Web development, data pipelines, concurrency, testing*

| # | Project | Key Concepts | Status |
|---|---------|--------------|--------|
| 51 | Coming soon... | | 🔜 |
| ... | | | |

---

### 🔴 Tier 4 — Professional (Projects 76–100)
*Focus: System design, deployment, ML/AI, full-stack apps*

| # | Project | Key Concepts | Status |
|---|---------|--------------|--------|
| 76 | Coming soon... | | 🔜 |
| ... | | | |

---

## 🚀 Project 01 — CLI Task Manager

> *The one that started it all.*

A command-line task manager built entirely in Python. Supports creating, listing, completing, and deleting tasks — all persisted to a local JSON file.

**What I practiced:**
- Parsing CLI arguments with `argparse`
- Reading and writing JSON files
- Structuring a small Python project cleanly
- CRUD operations without a database

**How to run:**
```bash
cd 01-cli-task-manager
python task_manager.py add "Buy groceries"
python task_manager.py list
python task_manager.py done 1
python task_manager.py delete 1
```

---

## 🛠️ How to Use This Repo

Each project lives in its own folder with the following structure:

```
project-name/
├── main.py           # Entry point
├── README.md         # Project-specific notes & what I learned
├── requirements.txt  # Dependencies (if any)
└── ...               # Other files as needed
```

**To run any project:**
```bash
# Clone the repo
git clone https://github.com/your-username/100-python-projects.git
cd 100-python-projects

# Navigate to a project
cd 01-cli-task-manager

# Install dependencies (if any)
pip install -r requirements.txt

# Run it
python main.py
```

---

## 📚 Learning Philosophy

> *"The best way to learn programming is to write programs."* — Dennis Ritchie

This repo follows a few core principles:

**Build, don't just read.** Every concept is reinforced by shipping actual working code.

**Embrace discomfort.** Projects are chosen to stretch current ability, not just confirm what's already known.

**Document the journey.** Each project folder includes notes on what was learned, what was hard, and what could be improved.

**Iterate and improve.** Early projects may be revisited and refactored as skills grow.

---

## 📈 Progress Tracker

```
Beginner    [█░░░░░░░░░░░░░░░░░░░░░░░░]  1 / 25
Intermediate [░░░░░░░░░░░░░░░░░░░░░░░░░]  0 / 25
Advanced    [░░░░░░░░░░░░░░░░░░░░░░░░░]  0 / 25
Professional [░░░░░░░░░░░░░░░░░░░░░░░░░]  0 / 25

Total: 1 / 100
```

---

## 🔧 Tech Stack

This repo spans a wide range of Python tooling as complexity grows:

- **Core:** Python 3.x, argparse, os, json, pathlib
- **Data:** pandas, SQLite, PostgreSQL, SQLAlchemy
- **Web:** Flask, FastAPI, requests, BeautifulSoup
- **Automation:** Selenium, schedule, smtplib
- **Testing:** pytest, unittest
- **ML/AI:** scikit-learn, TensorFlow / PyTorch
- **DevOps:** Docker, GitHub Actions, .env / dotenv

---

## 🤝 Connect

If you're on a similar journey, I'd love to connect. Feel free to open an issue, suggest a project idea, or just say hi.

**Star ⭐ the repo if it inspires you to start your own 100-project challenge!**

---

<p align="center">
  Built with 💻 + ☕ + persistence &nbsp;|&nbsp; Started 2024 &nbsp;|&nbsp; <em>Still going...</em>
</p>
