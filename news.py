import streamlit as st
import feedparser
from datetime import datetime
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1000, key="clock")

# 🌐 Page setup
st.set_page_config(page_title="News Hub", layout="wide")

# 🔄 Auto refresh
st_autorefresh(interval=60000, key="refresh")

# 🎨 HEADER STYLE
st.markdown("""
    <h1 style='text-align:center; color:#1f4e79;'>📰 NEWS HUB</h1>
    <p style='text-align:center; color:gray;'>Live Updates | Clean UI | Fast News</p>
""", unsafe_allow_html=True)

# ⏰ TIME
st.markdown(f"""
    <h4 style='text-align:center;'>⏰ {datetime.now().strftime("%I:%M:%S %p")}</h4>
""", unsafe_allow_html=True)

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

choice = st.sidebar.radio("📌 Categories", list(categories.keys()))

feed = feedparser.parse(categories[choice])

st.markdown(f"## 🔥 {choice} News")

# 🟦 NEWS CARDS (CLEAN + MODERN STYLE)
for entry in feed.entries[:15]:
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f5faff, #e6f2ff);
            padding:16px;
            margin-bottom:15px;
            border-radius:14px;
            box-shadow:0 4px 10px rgba(0,0,0,0.08);
            border-left:6px solid #1f4e79;
        ">
            <h4 style="color:#0b3d91;">📰 {entry.title}</h4>
            <p style="color:gray; font-size:13px;">
                📅 {entry.published if hasattr(entry,'published') else ''}
            </p>
            <a href="{entry.link}" target="_blank" style="
                text-decoration:none;
                color:#1f4e79;
                font-weight:bold;
            ">👉 Read Full News</a>
        </div>
    """, unsafe_allow_html=True)
