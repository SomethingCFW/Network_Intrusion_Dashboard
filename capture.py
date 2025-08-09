import subprocess
import sqlite3
import datetime
import re

DB_PATH = "database.db"

def log_event(source_ip, dest_ip, protocol, alert):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO logs (timestamp, source_ip, destination_ip, protocol, alert)
        VALUES (?, ?, ?, ?, ?)
    """, (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), source_ip, dest_ip, protocol, alert))
    conn.commit()
    conn.close()

# Run tcpdump to capture packets
tcpdump_cmd = ["sudo", "tcpdump", "-l", "-n", "-i", "eth0"]
process = subprocess.Popen(tcpdump_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

print("[*] Monitoring traffic... Press CTRL+C to stop.")
try:
    for line in process.stdout:
        # Fixed regex pattern
        match = re.search(r"(\d+\.\d+\.\d+\.\d+)\s+>\s+(\d+\.\d+\.\d+\.\d+):\s+(\w+)", line)
        if match:
            src, dst, proto = match.groups()

            # Alert Rules
            if proto.lower() == "icmp":
                log_event(src, dst, proto, "Ping detected")
            elif not src.startswith("192.168."):
                log_event(src, dst, proto, "External IP detected")

except KeyboardInterrupt:
    print("\n[*] Stopping monitoring...")
    process.terminate()
