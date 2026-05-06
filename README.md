# 🛒 E-Commerce Order Management System

A fully functional **E-Commerce CLI application** built with **Python and SQLite** — featuring user authentication, product management, order processing, stock validation, and sales analytics.

---

## 📌 Features

### 👤 User Management
- User Registration with **hashed passwords** (SHA-256)
- Secure Login / Logout
- Admin and Customer roles

### 📦 Product Management
- Add, view, update products
- Stock and price management
- Category-wise organization
- Low stock alerts

### 🛒 Order Management
- Browse product catalog
- Place orders with **real-time stock validation**
- **Atomic transactions** — order rolls back if anything fails
- View order history
- View order item details
- Cancel orders with automatic **stock restoration**

### 📊 Analytics & Reports
- Total revenue dashboard
- Top 5 best-selling products
- Revenue by category
- Export full sales report to **CSV**

---

## 🗂️ Project Structure

```
ecommerce_project/
│── main.py          # CLI entry point & menus
│── db.py            # Database connection
│── models.py        # User & Product operations
│── operations.py    # Order, Analytics & Reports
│── validators.py    # Input validation functions
│── utils.py         # Password hashing, CSV export, table printer
│── schema.sql       # Database schema
│── init_db.py       # Database initializer
│── README.md
```

---

## 🗄️ Database Schema

```
users        → id, name, email, password (hashed), created_at
products     → id, name, price, stock, category, created_at
orders       → id, user_id, total, status, created_at
order_items  → id, order_id, product_id, quantity, unit_price
```

---

## ⚙️ Tech Stack

- **Language:** Python 3
- **Database:** SQLite3
- **Security:** SHA-256 password hashing
- **Data Export:** CSV

---

## 🚀 How to Run

### 1. Initialize the database
```bash
python init_db.py
```

### 2. Run the application
```bash
python main.py
```

---

## 🔐 Roles

| Role  | Access |
|-------|--------|
| Admin | User ID = 1 (first registered user) |
| User  | All other registered users |

---

## 📋 How to Use

1. Run `python init_db.py` to set up the database
2. Run `python main.py`
3. Register → first registered user becomes **Admin**
4. Admin can add products and view analytics
5. Other users can browse, order, and track orders

---

## 👨‍💻 Author

**Dayanidhi Gudimetla**  
GitHub: [github.com/DayanidhiGudimetla](https://github.com/DayanidhiGudimetla)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
