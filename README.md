# 🚀 DevOps & Automation Portfolio

Practical automation tools built with Python, focused on solving real-world business problems.
Built as part of my preparation for a career in DevOps / Cloud Engineering.

---

## 🎯 Goal

To demonstrate hands-on skills for DevOps and Cloud roles by building tools that automate repetitive tasks — from data processing to log monitoring.

---

## 🛠️ Projects

### 1. 📊 Excel Cleaner & Merger

Automatically cleans and merges multiple Excel files into one structured report.

**Use case:** Many businesses manually combine Excel files (timesheets, financial data, exports). This tool automates that process and eliminates human error.

**Features:**
- Upload multiple `.xlsx` / `.xls` files via a web interface
- Automatically cleans data: removes empty rows, duplicates, and normalizes column names
- Detects and warns about column mismatches between files
- Previews each file before merging
- Exports a clean, ready-to-use Excel report

**Tech:** Python · Pandas · Streamlit · OpenPyXL

**Run locally:**
```bash
pip install -r requirements.txt
streamlit run excel_cleaner.py
```

---

### 2. 📄 Word naar Excel Converter

Extracts tables from Word documents and exports them to a structured Excel file.

**Use case:** Teams that store data in Word tables (reports, forms, meeting notes) can export it to Excel in one click — no manual copy-pasting.

**Features:**
- Upload any `.docx` file via a web interface
- Extracts all tables automatically, one sheet per table
- Handles duplicate column names and empty rows
- Previews extracted data before downloading
- Auto-adjusts column widths in the output Excel

**Tech:** Python · python-docx · Pandas · Streamlit · OpenPyXL

**Run locally:**
```bash
pip install -r requirements.txt
streamlit run word_to_excel.py
```

---

### 3. 🔍 Log Analyzer

Parses log files and generates a summary of errors, warnings, and info messages.

**Use case:** Quickly scan large log files without reading them line by line — useful for incident triage or daily health checks.

**Features:**
- Parses standard log files
- Counts and categorizes ERROR, WARNING, and INFO messages
- Outputs a clean summary report

**Tech:** Python · CLI

**Run locally:**
```bash
python3 log_analyzer.py --file app.log
```

---

### 4. 📂 Multi-Log Analyzer (CLI)

Extends the Log Analyzer to process multiple log files in one command.

**Features:**
- Processes an entire folder of log files
- Combines results into one summary
- CLI-based for easy scripting and automation

**Tech:** Python · CLI · argparse

**Run locally:**
```bash
python3 multi_log_analyzer.py --folder logs/
```

---

### 5. 👁️ Real-Time Log Watcher

Monitors a log file continuously and alerts on new errors or warnings as they appear.

**Use case:** Keep an eye on a running application without tailing logs manually — useful during deployments or debugging sessions.

**Features:**
- Watches a log file in real time (similar to `tail -f`)
- Instantly flags new ERROR and WARNING entries
- Lightweight and runs in the background

**Tech:** Python · CLI

**Run locally:**
```bash
python3 log_watcher.py --file app.log
```

---

### 6. 🐳 Docker Integration

All tools are containerized for consistent, reproducible environments across machines.

**Features:**
- Dockerfile per tool
- No local Python setup required — just Docker
- Works on any OS (Windows, Mac, Linux)

**Run with Docker:**
```bash
docker build -t excel-cleaner .
docker run -p 8501:8501 excel-cleaner
```

**Tech:** Docker · Linux · CLI

---

## 🧠 Skills Demonstrated

| Skill | Tools / Tech |
|---|---|
| Python automation | Pandas, python-docx, OpenPyXL |
| Web UI development | Streamlit |
| Data processing & cleaning | Pandas |
| CLI tooling | argparse, subprocess |
| Containerization | Docker |
| Version control | Git, GitHub |
| DevOps mindset | Automation, error handling, logging |

---

## 📌 About Me

I'm Efra — an aspiring Cloud / DevOps Engineer building practical tools to develop real-world experience. I'm focused on Azure Cloud and automation, and I'm continuously learning and expanding this portfolio.

> 💡 Open to traineeships and junior roles in DevOps / Cloud Engineering.

---

## 📬 Contact

- GitHub: [@Efra-ClouDev](https://github.com/Efra-ClouDev)
