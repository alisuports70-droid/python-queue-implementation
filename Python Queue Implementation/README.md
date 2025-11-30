<h1 align="center">🧩 Python Queue Data Structure</h1>

<p align="center">
  A clean, efficient, and object-oriented implementation of the 
  <strong>FIFO (First-In–First-Out)</strong> Queue in Python.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Category-Data%20Structures-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

## 📌 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Folder Structure](#-folder-structure)
- [How It Works](#-how-it-works)
- [Usage Example](#-usage-example)
- [Real-World Applications](#-real-world-applications)
- [Output](#-output)
- [Author](#-author)

---

## 🚀 Overview

This project provides a **lightweight, clean, and well-documented Queue implementation** in Python.  
It uses **OOP (Object-Oriented Programming)** principles and Python lists to simulate queue behavior.

This project is perfect for:

- Students learning **DSA**
- Beginners practicing Python OOP
- Developers preparing for **technical interviews**
- Anyone implementing queuing logic in applications

---

## 🌟 Features

- ➕ `enqueue(item)` — Add an element  
- ➖ `dequeue()` — Remove the first element  
- 👀 `peek()` — See front element without removing it  
- 📏 `size()` — Count items in queue  
- ⚠️ `is_empty()` — Check if queue is empty  
- 🧹 Clean & production-ready code  

---

## 🧰 Tech Stack

- **Python 3.x**
- No external libraries required

---

## 📁 Folder Structure

📦 python-queue
┣ 📜 queue.py
┣ 📜 example.py
┗ 📜 README.md

---

## 🧠 How It Works

A Queue follows **FIFO — First In, First Out**.

- The item inserted **first** gets removed **first**
- Works like:  
  - 🎫 Ticket line  
  - 🖨 Printer jobs  
  - 🤖 Task processing queues  

Internally uses:

- `append()` — add item  
- `pop(0)` — remove item  

---

## 📝 Usage Example

```python
from queue import Queue

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print(q.dequeue())  # 1
print(q.peek())     # 2
print(q.size())     # 2
print(q.is_empty()) # False

🌍 Real-World Applications

● Task scheduling

● Background workers

● Message queues

● Customer service systems

● Simulation models

● CPU process scheduling

🖥 Output
Dequeued: 1
Peek: 2
Size: 2
Is empty: False
After removing all items...
Is empty: True
Peek: None

👤 Author

Ali Hassan
Python Developer
GitHub: https://github.com/alisuports70-droid

---
