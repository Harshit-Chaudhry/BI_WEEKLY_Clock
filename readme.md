# ⏳ Deadline Countdown Clock with GitHub Tracker

This Streamlit app displays a real-time countdown to a selected deadline, along with GitHub project and study material tracking for your team members.

---

## 🚀 Features

- ⏰ Live countdown timer to a specified deadline
- 🧠 Two categorized sections:
  - **GitHub Coding Projects**
  - **GitHub Study Materials**
- 🎨 Custom dark theme styling with color highlights
- 👨‍💻 Useful for team/project accountability and end-semester planning

---

## 🛠️ Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [HTML & CSS](https://developer.mozilla.org/en-US/docs/Web/HTML) (for custom styling)

---

## 🧾 Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/Harshit-Chaudhry/BI_WEEKLY_Clock.git
    cd your-repo-name
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```

---

## 📌 How to Use

- The app shows a countdown timer to a pre-set deadline (27th April 2025, 11:59 PM).
- Track project or study progress by replacing `"None"` with your actual GitHub links.
- Easily customize the list by editing the Markdown in `app.py`.

---

## 📎 Example GitHub Entry Format

```markdown
- **Name**: [Project Title](https://github.com/username/repo-name)

---
🧑‍🏫 Contributing
Feel free to fork and add your own GitHub links, deadlines, or features!

---

📄 License
This project is licensed under the MIT License.