import streamlit as st
import pandas as pd
import re
from collections import Counter
import os
from datetime import datetime

st.set_page_config(page_title="GuardianIQ SOC", layout="wide")

# ---------------- THEME ----------------
st.markdown("""
<style>
body {
    background-color: #0b0b0b;
    color: #ff2b2b;
}
.stApp {
    background-color: #0b0b0b;
    color: #ff2b2b;
}
h1, h2, h3 {
    color: #ff2b2b;
}
.sidebar .sidebar-content {
    background-color: #111;
}
</style>
""", unsafe_allow_html=True)

LOG_FILE = "/var/log/suricata/fast.log"

# ---------------- READ REAL BACKEND LOGS ----------------
def read_logs():
    logs = []
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            for line in f:
                if "GuardianIQ" in line:
                    logs.append(line.strip())
    return logs

logs = read_logs()

# ---------------- EXTRACT IPS ----------------
def extract_ips(text):
    return re.findall(r"\b\d{1,3}(?:\.\d{1,3}){3}\b", text)

ips = extract_ips(" ".join(logs))
ip_count = Counter(ips)

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "🛡️ GuardianIQ SOC Panel",
    ["🏠 Overview", "📡 Attack Logs", "🧠 Threat Analytics"]
)

# ---------------- PAGE 1 ----------------
if menu == "🏠 Overview":
    st.title("🛡️ GuardianIQ SOC Dashboard")

    st.metric("🔥 Total Alerts", len(logs))

    st.subheader("🕒 Last 10 Security Events")
    for log in logs[-10:]:
        st.code(log)

# ---------------- PAGE 2 ----------------
elif menu == "📡 Attack Logs":
    st.title("📡 Live Attack Logs (Backend Connected)")

    if logs:
        for log in reversed(logs[-50:]):
            st.write(log)
    else:
        st.warning("No GuardianIQ alerts found in fast.log yet.")

# ---------------- PAGE 3 ----------------
elif menu == "🧠 Threat Analytics":
    st.title("🧠 Threat Intelligence Analytics")

    if ip_count:
        st.subheader("Top Source IPs (Live)")
        st.bar_chart(ip_count)
    else:
        st.info("No IP data available yet from logs.")