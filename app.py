import streamlit as st
from components.ai_utils import ask_ai
from components.pdf_utils import extract_pdf_text, clean_notes, export_clean_pdf
from components.finance_utils import add_expense, load_expenses, get_expense_summary, export_excel
from components.todo_utils import load_todos, save_todos

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------
st.set_page_config(
    page_title="AI-Powered Academic Productivity Hub",
    page_icon="🎓",
    layout="wide",
)

# --------------------------------------------------------
# GLOBAL DARK + NEON CSS THEME (GLASS UI)
# --------------------------------------------------------
custom_css = """
<style>

body {
    background: #0a0f1a;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(145deg, #05060a, #0f1629);
}

h1, h2, h3, h4, h5, .stTabs [role="tab"] p {
    color: #A8D0FF !important;
    font-weight: 700;
    letter-spacing: 1px;
}

.stTabs [role="tab"] {
    background: rgba(255,255,255,0.04);
    border-radius: 8px;
    padding: 10px;
    color: #8ab4ff !important;
    border: 1px solid #1f2a44;
}

.stTabs [role="tab"][aria-selected="true"] {
    background: rgba(0, 119, 255, 0.2);
    border-bottom: 2px solid #00c3ff;
    color: #fff !important;
}

.block-container {
    padding-top: 2rem;
}

.glass-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 18px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 25px rgba(0, 140, 255, 0.15);
}

textarea, input, select {
    background: rgba(255,255,255,0.06) !important;
    color: #d7e3ff !important;
    border-radius: 10px !important;
    border: 1px solid #304068 !important;
}

.stButton button {
    background: linear-gradient(90deg, #0077ff, #00e0ff);
    border-radius: 10px;
    color: white;
    border: none;
    padding: 0.6rem 1.3rem;
    font-weight: 700;
    transition: 0.2s ease-in-out;
}

.stButton button:hover {
    transform: scale(1.04);
    box-shadow: 0 0 15px #00b7ff;
}

/* Hide line under tabs */
.stTabs [data-baseweb="tab-list"]::after {
    display: none;
}

</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

# Header
st.markdown("<h1 style='text-align:center;'>🎓 AI-Powered Academic Productivity Hub </h1>", unsafe_allow_html=True)

tabs = st.tabs(["🧩 Task Splitter", "📝 Todo List", "💡 Idea Generator", "🧽 Notes Cleaner", "💰 Finance Manager"])



# --------------------------------------------------------
# TASK SPLITTER
# --------------------------------------------------------
with tabs[0]:
    st.markdown("### 🔹 Break down complex tasks into simple steps")
    with st.container():
        st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

        task_input = st.text_area("Enter a complex task", height=150)

        if st.button("Split Task"):
            if task_input:
                prompt = f"Split this task into simple step-by-step actions:\n{task_input}"
                steps = ask_ai(prompt)
                st.text_area("Steps:", steps, height=300)
            else:
                st.error("Please enter a task.")

        st.markdown("</div>", unsafe_allow_html=True)



# --------------------------------------------------------
# TODO LIST
# --------------------------------------------------------
with tabs[1]:
    st.markdown("### 🗂 Organize your daily tasks efficiently")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    from components.todo_utils import add_task, remove_completed_tasks, mark_task_completed, load_todos, get_pending_reminder, save_todos

    # --- Load and migrate old todos ---
    todos = load_todos()
    updated = False
    for t in todos:
        # Migrate old "done" key to "completed"
        if "done" in t and "completed" not in t:
            t["completed"] = t.pop("done")
            updated = True
        # Ensure all tasks have 'added_at'
        if "added_at" not in t:
            from datetime import datetime
            t["added_at"] = datetime.now().isoformat()
            updated = True
    if updated:
        save_todos(todos)

    # --- Reminder message ---
    reminder = get_pending_reminder()
    if reminder:
        st.warning(reminder)

    # --- Add new task ---
    new_todo = st.text_input("Add new task")
    if st.button("Add Task"):
        if new_todo.strip():
            add_task(new_todo.strip())
            st.success("Task added!")
            st.rerun()
        else:
            st.warning("Task cannot be empty!")

    # --- Pending tasks ---
    st.write("#### Pending Tasks:")
    pending_tasks = [t for t in todos if not t["completed"]]
    if pending_tasks:
        for i, t in enumerate(pending_tasks):
            if st.checkbox(t["task"], key=f"pending_{i}"):
                mark_task_completed(t["task"])
                st.rerun()
    else:
        st.info("✅ No pending tasks!")

    # --- Completed tasks ---
    st.write("#### Completed Tasks:")
    completed_tasks = [t for t in todos if t["completed"]]
    if completed_tasks:
        for t in completed_tasks:
            st.markdown(f"~~{t['task']}~~")
    else:
        st.info("No completed tasks yet.")

    # --- Remove completed tasks button ---
    if st.button("🗑️ Remove Completed Tasks"):
        remove_completed_tasks()
        st.success("Removed all completed tasks!")
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)



# --------------------------------------------------------
# IDEA GENERATOR
# --------------------------------------------------------
with tabs[2]:
    st.markdown("### 💡 Get smart ideas instantly!")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    idea_type = st.selectbox("Choose idea type", ["Project", "Study", "Personal", "Custom"])
    user_prompt = st.text_area("Optional custom prompt")

    if st.button("Generate Idea"):
        prompt = f"Generate {idea_type} ideas. {user_prompt}"
        result = ask_ai(prompt)
        st.text_area("Ideas:", result, height=300)

    st.markdown("</div>", unsafe_allow_html=True)



# --------------------------------------------------------
# NOTES CLEANER
# --------------------------------------------------------
with tabs[3]:
    st.markdown("### 🧼 Clean and simplify your study notes")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_pdf and st.button("Clean Notes"):
        raw_text = extract_pdf_text(uploaded_pdf)
        cleaned = clean_notes(raw_text)
        st.text_area("Cleaned Notes", cleaned, height=300)

        pdf_path = export_clean_pdf(cleaned)
        st.success("PDF Exported!")
        st.download_button("Download Clean PDF", open(pdf_path, "rb"), file_name="clean_notes.pdf")

    st.markdown("</div>", unsafe_allow_html=True)



# --------------------------------------------------------
# FINANCE MANAGER
# --------------------------------------------------------
with tabs[4]:
    st.markdown("### 💰 Track and manage your study expenses")
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        date = st.date_input("Date")
    with col2:
        category = st.text_input("Category")
    with col3:
        amount = st.number_input("Amount", min_value=1.0)

    if st.button("Add Expense"):
        add_expense(str(date), category, amount)
        st.success("Expense added!")

    if st.button("View Summary"):
        summary = get_expense_summary()
        st.write(summary)

    if st.button("Export Excel Report"):
        file_path = export_excel()
        st.download_button("Download Excel", open(file_path, "rb"), file_name="expenses.xlsx")

    st.markdown("</div>", unsafe_allow_html=True)