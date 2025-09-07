# 🧾 Python Billing System with Excel Export

A simple **menu-driven billing system** written in Python.  
This program allows you to enter customer details and up to 4 items, calculates totals, and exports the bill into an **Excel (.xlsx)** file using [openpyxl](https://pypi.org/project/openpyxl/).

---

## 🚀 Features

- Input **customer name** and **contact number**.
- Add up to **4 items** with quantity & unit price.
- Calculates:
  - Item total (`quantity × price`)
  - Grand total of all items
- Saves the bill as **`Bill_<CustomerName>.xlsx`**.
- Easy-to-use **menu-driven interface**.

---

## 📦 Requirements

- Python **3.7+**
- [openpyxl](https://pypi.org/project/openpyxl/) (for Excel export)

### Install dependencies

```bash
pip install -r requirements.txt
```
