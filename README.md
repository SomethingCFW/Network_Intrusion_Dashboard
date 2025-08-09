# Network_Intrusion_Dashboar

# Overview
A self-hosted local web page that detects all external IPs in my local network and shares them in a log format. This was created for my Common App extracurriculars section.

# Features
- Captures live network packets using tcpdump
- Logs activity like ping requests and traffic from external IP addresses
- Stores logs in a SQLite database
- Web dashboard built with Flask showing the newest 50 intrusion events
- Deployed on a Pi 4

# Tools used
- Python
- Flask
- tcpdump 
- SQLite
- HTML/CSS

# Install
Clone the repository
   git clone https://github.com/SomethingCFW/Network_Instrusion_Dashboard.git
