# AI-Powered Academic Productivity Hub

## Project Description

The AI-Powered Academic Productivity Hub is a comprehensive web application designed to enhance the productivity of students and academics. It leverages artificial intelligence to assist with task management, idea generation, note organization, and financial tracking. The app provides a user-friendly interface with multiple tools integrated into a single platform, making it easier for users to stay organized and focused on their academic goals.

This project exists to address the common challenges faced by students, such as breaking down complex tasks, managing to-do lists, generating creative ideas, cleaning up messy notes from PDFs, and tracking study-related expenses. By integrating AI capabilities, the app offers intelligent assistance that goes beyond traditional productivity tools, helping users optimize their time and resources effectively.

## Tech Stack

- **Frontend/UI**: Streamlit - A fast way to build and share data apps with Python.
- **Backend**: Python - The core programming language used for all logic and processing.
- **AI Integration**: Ollama - For running local AI models (e.g., Llama 3.1) to provide intelligent responses and suggestions.
- **PDF Processing**: PyPDF2 and FPDF - For extracting text from PDFs and generating new PDF files.
- **Data Handling**: Pandas and OpenPyXL - For managing and exporting financial data to Excel format.
- **File Management**: Standard Python libraries for handling CSV and JSON data storage.
- **Styling**: Custom CSS for a dark, neon-themed glass UI design.

## Features

- **Task Splitter**: Break down complex academic tasks into simple, actionable steps using AI.
- **Todo List**: Organize daily tasks with add, complete, and remove functionalities, including reminders for pending tasks.
- **Idea Generator**: Generate creative ideas for projects, studies, or personal matters with customizable prompts.
- **Notes Cleaner**: Upload PDF notes, extract text, clean and simplify content, and export as a new PDF.
- **Finance Manager**: Track study-related expenses, view summaries, and export reports to Excel.

## Installation

1. Clone the repository:

   ```
   git clone <repository-url>
   cd StudentCommandCentre
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Ensure Ollama is installed and running locally with the Llama 3.1 model:
   - Download and install Ollama from [ollama.ai](https://ollama.ai)
   - Pull the Llama 3.1 model: `ollama pull llama3.1`

## Usage

Run the application using Streamlit:

```
streamlit run app.py
```

The app will open in your default web browser at `http://localhost:8501`. Navigate through the different tabs to access various features.

## Project Structure

- `app.py`: Main application file containing the Streamlit UI and logic.
- `components/`: Directory containing utility modules:
  - `ai_utils.py`: Handles AI interactions with Ollama.
  - `pdf_utils.py`: Functions for PDF text extraction and generation.
  - `finance_utils.py`: Expense management and Excel export.
  - `todo_utils.py`: Todo list management.
- `data/`: Directory for data storage (CSV for expenses, JSON for todos).
- `assets/`: Directory for CSS styling.
- `requirements.txt`: List of Python dependencies.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-source and available under the [MIT License](LICENSE).
