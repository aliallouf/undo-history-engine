# undo-history-engine
# Undo History Engine

A Python implementation of a **Singly Linked List** designed to mimic the 'Undo' functionality found in modern text editors and software applications.

## 🚀 The Concept
This project demonstrates how a Linked List is superior to an Array for "Undo" operations. By inserting and deleting at the **Head** of the list, we achieve **O(1) time complexity**, meaning the operation is lightning-fast regardless of how many thousands of actions are in the history.

## 🛠️ Logic & Design
- **Node-Based Storage:** Each action is stored as a `Task` node containing data and a reference to the next action.
- **Custom Exceptions:** Includes `HistoryEmptyError` to prevent program crashes during empty-state interactions.
- **Memory Efficient:** Uses dynamic memory allocation, only consuming RAM for active history items.

## 📂 Project Structure
- `Task`: The basic unit (Node) of the list.
- `ActionHistory`: The controller (Linked List) that manages pointers.

## 🖥️ How to Run
1. Ensure you have Python 3.x installed.
2. Clone this repository.
3. Run the script:
   ```bash
   python linked_list_app.py
