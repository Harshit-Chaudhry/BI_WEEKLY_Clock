import streamlit as st
import datetime
import time

st.title("Deadline Countdown Clock")

st.markdown("### 📂 GitHub Coding Projects")
st.markdown("""
- **Harshit Chaudhary**: None
- **Ritesh Hooda**: None  
- **Krishna Mehta**: None  
- **Digvijay**: None
- **Archit Yadav**: None  
""")

st.markdown("### 📚 GitHub Study Material You've Uploaded")
st.markdown("""
- **Dipanshu Goyal**: None 
- **Ritesh Hooda**: None  
- **Krishna Mehta**: None 
- **Sahib Taj Singh**: None
- **Soumalya Gosh**: None 
- **Hardik**: None 
- **Digvijay**: None
""")


deadline_date = datetime.date(2025, 4, 27)
deadline_time = datetime.time(23, 59)


deadline = datetime.datetime.combine(deadline_date, deadline_time)


countdown_placeholder = st.empty()


while True:
    now = datetime.datetime.now()
    time_left = deadline - now

    if time_left.total_seconds() <= 0:
        countdown_placeholder.markdown("### ⏰ Deadline Reached!")
        break


    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)


    countdown_str = f"{days} days  {hours} hours  {minutes} min  {seconds} sec"


    countdown_placeholder.markdown(f"### ⌛ Time Remaining: {countdown_str}")

    time.sleep(1)
