As-salamu alaykum 
Now I am telling you about this browser
🛡️ Pentest Browser
Pentest Browser is a hacker-style, GUI-based web browser built using Python and PyQt5. It's designed for penetration testing, input fuzzing, and form brute-force attacks on websites. It includes built-in tools like a repeater, input field detector, attack logger, request interceptor, and a system resource monitor.

🧩 Features
🌐 Browser Features
Tabbed web browsing (based on QWebEngineView)

URL navigation bar with quick buttons:

🔙 Back, 🔜 Forward, 🏠 Home, ➕ New Tab

Predefined test target: http://testasp.vulnweb.com

🧪 Pentesting Tools
🕵️‍♂️ Detect Inputs: Auto-detects all <input name=""> fields from the current web page

🚀 Start Attack: Launches input-based attacks (fuzzing or brute-force) using wordlists

⛔ Stop Attack: Stops an active attack session

📜 Attack Log: Displays all attempted payloads and attack results

Repeater: Send custom GET or POST HTTP requests with headers and body

Delay Control: Adjust time interval between payload submissions (1–10 seconds)

🖥️ System Monitor
Displays CPU %, memory usage, and GPU temperature (if supported)

📦 Request Interceptor
Logs every outgoing HTTP request in requests_log.txt (includes domain and URL)

🔧 Requirements
Python 3.6+

PyQt5

PyQtWebEngine

psutil

requests

Install dependencies using:

pip install PyQt5 PyQtWebEngine psutil requests
🚀 Running the Application

cd bruteforcr-browser,
cd __pycache__,
python3 browser2.0.py


📂 Project Structure

pentest_browser.pyc      # Main PyQt5 GUI browser
requests_log.txt        # Automatically generated log of outgoing HTTP requests
wordlists/              # (Optional) Directory to store your wordlist text files
⚙️ How the Attack Works
Input Detection:
It scans the current webpage for <input> elements with a name attribute and supported type.

Wordlist Assignment:
A GUI lets you assign a wordlist file to each detected input field.

Payload Execution:
The tool auto-fills the fields with values from the wordlist(s) and submits the form with delay control.

Logging:
Every attempted payload is shown in the attack log panel.

🛡️ Legal Disclaimer
This tool is provided for educational and ethical penetration testing purposes only.
⚠️ Do NOT use this tool on websites or systems without proper authorization. Unauthorized use is illegal.

