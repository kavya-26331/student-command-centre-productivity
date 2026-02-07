import pandas as pd
import os

EXPENSE_FILE = "data/expense.csv"

def add_expense(date, category, amount):
    if not os.path.exists(EXPENSE_FILE):
        df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    else:
        df = pd.read_csv(EXPENSE_FILE)
    new_row = pd.DataFrame({"Date": [date], "Category": [category], "Amount": [amount]})
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(EXPENSE_FILE, index=False)

def load_expenses():
    if not os.path.exists(EXPENSE_FILE):
        return pd.DataFrame(columns=["Date", "Category", "Amount"])
    return pd.read_csv(EXPENSE_FILE)

def get_expense_summary():
    df = load_expenses()
    if df.empty:
        return "No expenses recorded."
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    return summary.to_string(index=False)

def export_excel():
    df = load_expenses()
    output_path = "expenses.xlsx"
    df.to_excel(output_path, index=False)
    return output_path
