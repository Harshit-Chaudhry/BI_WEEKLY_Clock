import streamlit as st
import datetime
import time

st.markdown(
    """
    <style>
    body {
        background-color: #0f172a; /* A dark blue-gray */
        color: #f8f8f2; /* A light gray */
    }
    .stTitle {
        color: #f8f8f2;
    }
    h3 {
        color: #f8f8f2;
    }
    .stMarkdown {
        color: #f8f8f2;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Deadline Countdown Clock")

st.markdown("### 📂 GitHub Coding Projects")
st.markdown("""
- **Harshit Chaudhary**: <span style='color:#e0af68;'> https://github.com/Harshit-Chaudhry/Battery_Temp_Pred_MATLAB.git </span>
- **Ritesh Hooda**: <span style='color:#e0af68;'> None </span>
- **Soumalya Ghosh**: <span style='color:#e0af68;'> https://github.com/Froskersss/iris_classification </span>
- **Krishna Mehta**: <span style='color:#e0af68;'> None </span>
- **Dipanshu Goyal**: <span style='color:#e0af68;'> https://github.com/dipanshu1907/HR-analysis-Dashboard.git </span>
- **Sahib Taj Singh**: <span style='color:#e0af68;'> None </span>
- **Hardik Tyagi**: <span style='color:#e0af68;'> None </span>
- **Pummy**: <span style='color:#e0af68;'> None </span>
- **Digvijay**: <span style='color:#e0af68;'> None </span>
- **Archit Yadav**: <span style='color:#e0af68;'> https://github.com/Daddy-Myth/Real-Time-Face-Detection-With-Pytorch-Facenet </span>
""", unsafe_allow_html=True)



deadline_date = datetime.date(2025, 6, 22)
deadline_time = datetime.time(23 - 5, 59 - 30)
deadline = datetime.datetime.combine(deadline_date, deadline_time)
countdown_placeholder = st.empty()

while True:
    now = datetime.datetime.now()
    time_left = deadline - now

    if time_left.total_seconds() <= 0:
        countdown_placeholder.markdown("<h3 style='color:#ff6b6b;'>⏰ Deadline Reached!</h3>", unsafe_allow_html=True)
        break

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    countdown_str = f"<h3 style='color:#a8dadc;'>⌛ Time Remaining: {days} days {hours} hours {minutes} min {seconds} sec </h3>"
    countdown_placeholder.markdown(countdown_str, unsafe_allow_html=True)

    time.sleep(1)
