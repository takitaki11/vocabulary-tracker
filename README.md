# 📚 Language Learning Vocabulary Tracker

## 👩‍💻 Developed by: Takhmina Zhusupova

---

### 📌 Project Description

This is a command-line Python application designed to help users track and manage vocabulary while learning a new language. It allows adding, viewing, updating, deleting words, and also provides a simple learning report. All data is saved in a CSV file to ensure it remains between sessions.

---

### 🎯 Objectives

- Help language learners systematically track vocabulary.
- Practice CRUD operations in Python.
- Apply file handling to store data persistently.
- Structure code using functions and modular programming.
- Build a simple and user-friendly CLI tool for personal learning.

---

## ✅ Project Requirements

1. Add a new word with translation.
2. View all saved words in a list.
3. Update existing word or translation.
4. Delete a word from the list.
5. Store data persistently using a `.csv` file.
6. Load data from file at program startup.
7. Save changes automatically after each operation.
8. Generate report: total number of words and how many were reviewed.
9. Use separate functions for each action (e.g., `add_word()`, `view_words()`).
10. Handle invalid input gracefully with helpful messages.

---

## 📘 Documentation

### 🔄 Algorithms and Logic

- Program flow is based on a simple menu loop allowing users to choose actions.
- Each core feature is implemented through a function: add, update, delete, view, report.
- File handling uses Python’s built-in `csv` module for easy and structured storage.

### 🧱 Data Structures

- Vocabulary is stored in a list of dictionaries with keys: `"word"` and `"translation"`.
- All data is saved in `words.csv`, which acts like a mini database.

### 🧩 Functions/Modules Used

- `load_words()`: Loads words from the CSV file on startup.
- `save_words()`: Saves the current list of words to the file.
- `add_word()`: Adds a new word and its translation.
- `view_words()`: Displays the current vocabulary list.
- `update_word()`: Updates a word or its translation.
- `delete_word()`: Deletes a word from the list.
- `show_report()`: Shows statistics such as total number of words.

### ⚠️ Challenges Faced

- Preventing duplicate entries while adding words.
- Ensuring the CSV file format remained consistent even after multiple updates/deletes.
- Structuring the program cleanly to avoid spaghetti code.
- Handling empty input or typos without breaking the program.

---

### 🎥 Presentation Link

[Click to View Presentation](https://www.canva.com/design/DAGoDzig_dk/Fp9RsQmLyuogZeNXFzGhZg/edit?utm_content=DAGoDzig_dk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

---

✅ All functionality works through a simple menu in the terminal.  
📂 All data is saved in `words.csv`, and the program remembers it the next time you run it.  
🧠 A great start to learning Python, file I/O, and structured programming!

