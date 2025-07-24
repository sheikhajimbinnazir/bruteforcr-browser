# 🕋 As-salamu alaykum 🤲

Welcome! Now I am introducing you to a powerful pentesting browser.

---

# 🛡️ Pentest Browser

`Pentest Browser` is a **hacker-style**, **GUI-based web browser** built with **Python** and **PyQt5**.

Designed for:

- Penetration Testing 🔐  
- Input Fuzzing ⚔️  
- Form Brute-force Attacks 🔓  

It includes essential tools for ethical hacking:
- ✅ Repeater
- ✅ Input Field Detector
- ✅ Attack Logger
- ✅ Request Interceptor
- ✅ System Resource Monitor

---

## 🧩 Features

### 🌐 Browser Interface
- Tabbed Web Browsing using `QWebEngineView`
- Smart URL Navigation Bar
- Quick Buttons:
  - 🔙 Back | 🔜 Forward | 🏠 Home | ➕ New Tab
- Preloaded target site: [`http://testasp.vulnweb.com`](http://testasp.vulnweb.com)

---

### 🧪 Pentesting Tools
- 🕵️‍♂️ **Detect Inputs**  
  Auto-detects all `<input name="">` fields on the page

- 🚀 **Start Attack**  
  Launch brute-force/fuzzing with assigned wordlists

- ⛔ **Stop Attack**  
  Immediately halt ongoing attack session

- 📜 **Attack Log**  
  Shows attempted payloads and responses

- 🔁 **Repeater**  
  Send custom GET/POST requests with headers and body

- 🕰️ **Delay Control**  
  Adjust interval between payloads (1–10 seconds)

---

### 🖥️ System Monitor
- Real-time system info:
  - CPU %
  - Memory %
  - GPU Temp (if supported)

---

### 📦 Request Interceptor
- Logs every HTTP request
- Saved in: `requests_log.txt`  
  (Includes full URL and domain)

⚙️ How the Attack Works
Input Detection
→ Scans for valid <input name="..."> fields

Wordlist Assignment
→ Assigns a wordlist to each field using the GUI

Payload Execution
→ Fills inputs and submits the form automatically

Logging
→ All attempts are shown in a real-time log

🛡️ Legal Disclaimer
This tool is for educational and authorized ethical hacking only.

⚠️ Do NOT use on any website or system without explicit permission.
🚫 Unauthorized use is illegal and punishable by law.


---


## 🔧 Requirements

- Python 3.6+
- PyQt5
- PyQtWebEngine
- psutil
- requests


📥 Install with:

```bash
git clone https://github.com/sheikhajimbinnazir/bruteforcr-browser.git
pip install PyQt5 PyQtWebEngine psutil requests
cd bruteforcr-browser
cd __pycache__
python3 browser2.0.py

```

Stay with us
 ## 🔖 Tags & Topics

`PentestBrowser` &nbsp; `EthicalHacking` &nbsp; `SheikhAjimBinNazir` &nbsp; `IslamicCyberNetwork`  
`CyberSecurity` &nbsp; `PythonBrowser` &nbsp; `HackerTool` &nbsp; `PyQt5Browser`  
`OpenSourcePentest` &nbsp; `BruteForceTool` &nbsp; `WebFuzzer` &nbsp; `RepeaterTool`  
`SecurityResearch` &nbsp; `CyberUmmah` &nbsp; `InfoSecTools` &nbsp; `IslamicHackers`  
`IslamicEthicalHackers` &nbsp; `SheikhAjimTools` &nbsp; `BrowserForHackers`  
`BugBountyTools` &nbsp; `DigitalDawahSecurity` &nbsp; `HackTheHalalWay`

## 🔖 Hashtags

#PentestBrowser #EthicalHacking #SheikhAjimBinNazir #IslamicCyberNetwork  
#CyberSecurity #PythonBrowser #HackerTool #PyQt5Browser  
#OpenSourcePentest #BruteForceTool #WebFuzzer #RepeaterTool  
#SecurityResearch #CyberUmmah #InfoSecTools #IslamicHackers  
#IslamicEthicalHackers #SheikhAjimTools #BrowserForHackers  
#BugBountyTools #DigitalDawahSecurity #HackTheHalalWay
