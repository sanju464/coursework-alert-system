coursework-alert-system

Never miss a deadline again.

An automated tool that monitors ETLab for new assignments and tutorials, detects updates using hashing, and instantly notifies students via email or Google Calendar.

🚀 Features

🔍 Smart change detection — monitors ETLab assignment/tutorial pages using hashing, only triggers when something actually changes
📧 Instant email alerts — sends notifications to individual students or group emails
📅 Google Calendar integration — adds deadlines directly to your calendar automatically
⏰ Never miss a deadline — runs in the background and catches updates as soon as they're posted
👥 Group support — notify an entire class or group at once


🎯 Who is this for?
Students at colleges using ETLab (common in Kerala engineering colleges) who want to stop manually checking for new assignments every day.

🛠️ How it Works

The tool periodically fetches your ETLab assignment/tutorial page
It computes a hash of the page content
If the hash changes (new assignment posted), it triggers an alert
You get an email or Google Calendar notification instantly


⚙️ Setup
Requirements

Python 3.x
Google account (for Calendar integration)
ETLab account

Installation
bash# Clone the repo
git clone https://github.com/sanju464/coursework-alert-system.git
cd coursework-alert-system

# Install dependencies
pip install -r requirements.txt
Configuration

Add your ETLab credentials and email in the config section of hash checker.py
Set up Google Calendar API credentials (see Google Calendar Python Quickstart)
Run the script:

bashpython "hash checker.py"
Or open and run the Jupyter notebook:
bashjupyter notebook Url_phising3.ipynb

📸 Screenshots

Add screenshots here


📄 License
MIT License — free to use, modify, and distribute.

👨‍💻 Author
sanju464 — github.com/sanju464

Built for Kerala engineering students 🌴
