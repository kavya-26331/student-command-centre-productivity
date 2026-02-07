import ollama

def ask_ai(prompt):
    try:
        response = ollama.chat(model="llama3.1", messages=[
            {"role": "user", "content": prompt}
        ])
        return response["message"]["content"]
    except Exception as e:
        return f"Error calling Ollama: {str(e)}"
