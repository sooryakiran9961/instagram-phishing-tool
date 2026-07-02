# Instagram Phishing Simulation Tool

> **⚠️ IMPORTANT DISCLAIMER: This tool is for EDUCATIONAL PURPOSES ONLY.**
> Unauthorized use of phishing techniques is illegal in most jurisdictions.
> Only use this on systems you own or have explicit written permission to test.

## 📋 Overview

A Python-based Instagram login page clone designed to demonstrate how credential harvesting phishing attacks work. Created as part of a cybersecurity educational project to understand social engineering attack vectors.

## 🎯 Purpose

This tool demonstrates:

- How phishing websites are created using site cloning
- How unsuspecting users can be tricked into entering credentials
- The importance of browser security indicators (HTTPS, URL inspection)
- Why Multi-Factor Authentication (MFA) is critical

## ⚙️ How It Works

1. The Python server hosts a cloned Instagram login page
2. When a user visits the page and enters credentials, they are captured
3. The user is then redirected to the real Instagram website
4. Captured credentials are logged to a text file

## 🛠️ Requirements

- **Kali Linux** (or any Linux distribution with Python 3)
- Python 3
- Network access (for serving the page)

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/sooryakiran9961/instagram-phishing-tool.git

# Navigate to the project directory
cd instagram-phishing-tool
# Make the script executable (if not already)
chmod +x phish.py

# Run with sudo  python3 phish.py

Locally: Open http://localhost:8080 in a browser
Network (same Wi-Fi): Other devices visit http://<YOUR_IP>:8080
Find your IP with: hostname -I or ip a | grep inet
Captured credentials
After someone submits the form, credentials are:

Displayed in the terminal in real-time
Saved to captured.txt in the project directory
To view saved credentials:
cat captured.txt
🧪 Testing It Yourself
Run the server
Open a browser and go to http://localhost:8080
Enter test credentials (e.g., testuser / testpass123)
Observe the credentials appear in the terminal
Check the captured.txt file
📁 Project Structure
instagram-phishing-tool/
├── phish.py          # Python HTTP server with credential harvesting
├── index.html        # Cloned Instagram login page (HTML/CSS)
├── captured.txt      # Captured credentials (auto-generated)
├── .gitignore        # Files excluded from version control
└── README.md         # This file
🔧 Customization Options
Change the port
Edit phish.py and change PORT = 8080 to any available port.

Add HTTPS (SSL)
# Generate a self-signed certificate
openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365 -nodes

# Modify phish.py to use SSL (requires additional code changes)
Use ngrok for external access
# Install ngrok (requires free account at ngrok.com)
sudo apt install ngrok

# Expose your local server
ngrok http 8080
🚫 Detection & Prevention
This tool also teaches how to detect and prevent phishing attacks:
Indicator	What to look for
URL inspection	Check for misspellings or unusual domains
HTTPS	Look for the padlock icon in the address bar
Browser warnings	Modern browsers flag suspicious pages
Password managers	Most autofill only on legitimate domains
MFA/2FA	Secondary authentication prevents harvested credentials from working


