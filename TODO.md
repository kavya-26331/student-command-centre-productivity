# TODO List for Implementing Missing Components

## Completed Tasks

- [x] Implement components/ai_utils.py with ask_ai function (mock response)

  - **Technology:** Python, OpenAI API (mocked)
  - **Features:** AI-powered task splitting, idea generation using prompt engineering

- [x] Implement components/pdf_utils.py with extract_pdf_text, clean_notes, export_clean_pdf

  - **Technology:** Python, PyPDF2 for PDF text extraction, FPDF for PDF generation
  - **Features:** PDF text extraction, note cleaning using regex and NLP techniques, export cleaned notes to PDF

- [x] Implement components/finance_utils.py with add_expense, load_expenses, get_expense_summary, export_excel

  - **Technology:** Python, Pandas for data manipulation, OpenPyXL for Excel export
  - **Features:** Expense tracking with CSV storage, summary calculations (total, category-wise), Excel report generation

- [x] Fix Streamlit duplicate element key error in TODO list
  - **Technology:** Streamlit, Python
  - **Features:** Unique checkbox keys using loop index instead of timestamps, replaced deprecated st.experimental_rerun() with st.rerun() for app refresh after state changes
