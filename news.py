import streamlit as st
import feedparser
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
import pytz

# 🌐 Page setup
st.set_page_config(page_title="News Hub", layout="wide")

# 🔄 Auto refresh (1 sec)
st_autorefresh(interval=1000, key="clock")

# 🧠 HEADER
st.markdown("""
    <h1 style='text-align:center; color:#0b3d91;'>📰 NEWS HUB</h1>
    <p style='text-align:center; color:gray;'>Live News • Auto Refresh • IST Time</p>
""", unsafe_allow_html=True)

# ⏰ IST TIME FIX (IMPORTANT)
ist = pytz.timezone('Asia/Kolkata')
now = datetime.now(ist)

st.markdown(
    f"<h3 style='text-align:center;'>⏰ {now.strftime('%I:%M:%S %p')}</h3>",
    unsafe_allow_html=True
)

# 📌 CATEGORIES
categories = {
    "General": "https://www.thehindu.com/news/national/feeder/default.rss",
    "World": "https://www.thehindu.com/news/international/feeder/default.rss",
    "Sports": "https://www.thehindu.com/sport/feeder/default.rss",
    "Business": "https://www.thehindu.com/business/feeder/default.rss",
    "Technology": "https://www.thehindu.com/sci-tech/technology/feeder/default.rss",
    "Health": "https://www.thehindu.com/sci-tech/health/feeder/default.rss",
    "Entertainment": "https://www.thehindu.com/entertainment/feeder/default.rss"
}

# 🧭 SIDEBAR
choice = st.sidebar.radio("📌 Categories", list(categories.keys()))

# 🔗 FEED
feed = feedparser.parse(categories[choice])

st.markdown(f"## 🔥 {choice} News")

# 🟦 NEWS CARDS
for entry in feed.entries[:15]:
    st.markdown(f"""
        <div style="
            background: #f5faff;
            padding:16px;
            margin-bottom:15px;
            border-radius:14px;
            border-left:6px solid #0b3d91;
            box-shadow:0 3px 8px rgba(0,0,0,0.08);
        ">
            <h4 style="color:#0b3d91;">📰 {entry.title}</h4>
            <p style="color:gray; font-size:13px;">
                📅 {entry.published if hasattr(entry,'published') else ''}
            </p>
            <a href="{entry.link}" target="_blank"
               style="color:#0b3d91; font-weight:bold; text-decoration:none;">
               👉 Read Full News
            </a>
        </div>
    """, unsafe_allow_html=True)
