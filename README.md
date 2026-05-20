# 🛒 E-Commerce Order Management System

A fully functional **E-Commerce CLI application** built with **Python and SQLite** — featuring role-based authentication, product management, atomic order processing, stock validation, revenue analytics, and automated CSV reporting.

---

## 📌 Features

### 👤 User Management
- User registration with **salted SHA-256 password hashing** (unique salt per user)
- Secure login / logout with hash verification
- Admin and Customer roles

### 📦 Product Management
- Add, view, and update products
- Stock and price management
- Category-wise organization
- Low stock alerts (threshold-based)

### 🛒 Order Management
- Browse product catalog
- Place orders with **real-time stock validation**
- **Atomic transactions** — full rollback if anything fails
- View order history and item details
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
│── utils.py         # Salted SHA-256 hashing, CSV export, table printer
│── schema.sql       # Database schema (users, products, orders, order_items)
│── init_db.py       # Database initializer
│── tests/
│   ├── __init__.py
│   └── test_core.py # 12 pytest unit tests
└── README.md
```

---

## 🗄️ Database Schema

| Table | Description |
| --- | --- |
| `users` | id, name, email, password (SHA-256 hashed), salt, created_at |
| `products` | id, name, price, stock, category, created_at |
| `orders` | id, user_id, total, status, created_at |
| `order_items` | id, order_id, product_id, quantity, unit_price |

---

## ⚙️ Tech Stack

| Layer | Technology |
| --- | --- |
| Language | Python 3 |
| Database | SQLite3 |
| Security | SHA-256 hashing with random salt |
| Export | CSV (built-in) |
| Testing | pytest |

---

## 🚀 How to Run

### 1. Clone the repository
```
git clone https://github.com/DayanidhiGudimetla/ecommerce-order-management.git
cd ecommerce-order-management
```

### 2. Initialize the database
```
python init_db.py
```

### 3. Run the application
```
python main.py
```
> No external dependencies required — uses Python standard library only.

---

## 🧪 Running Tests

```
python -m pip install pytest
python -m pytest tests/test_core.py -v
```

### Test Coverage

| Test Area | Cases Covered |
| --- | --- |
| Password hashing | Salt uniqueness, hash length (64 chars), deterministic with same salt |
| Password verification | Correct password, wrong password, wrong salt |
| CSV export | File creation, header accuracy, data rows, empty data |

**12 tests — all passing ✅**

---

## 🔐 Roles

| Role | How it works | Access |
| --- | --- | --- |
| Admin | First registered user (user ID = 1) | Products, users, analytics |
| User | All other registered users | Browse, order, track orders |

---

## 📋 Usage Guide

1. Run `python init_db.py` to set up the database
2. Run `python main.py` to launch the CLI
3. **Register** — the first registered user automatically becomes Admin
4. **Admin** can add products, manage stock/prices, view analytics, export reports
5. **Users** can browse products, place orders, view history, and cancel orders

---

## 📊 Analytics Available (Admin Only)

- 💰 Total revenue from all confirmed orders
- 📦 Total number of orders placed
- 🏆 Top 5 best-selling products (by quantity)
- 📂 Revenue breakdown by product category
- 📄 Full sales report exportable to `sales_report.csv`

---

## 🔐 Security Design

Passwords are never stored in plain text. Each user gets a unique **16-byte random salt** at registration. The salt is combined with the password before SHA-256 hashing, making rainbow table attacks ineffective even if the database is compromised.

```
Registration: password + random_salt → SHA-256 → store (hash, salt)
Login:        password + stored_salt → SHA-256 → compare with stored hash
```

---

## 👨‍💻 Author

**Dayanidhi Gudimetla**
- 📧 gudimetladaya11@gmail.com
- 🔗 [LinkedIn](https://www.linkedin.com/in/dayanidhi-gudimetla-2b08013ab)
- 🐙 [GitHub](https://github.com/DayanidhiGudimetla)

---

## 📄 License

This project is open source and available under the [MIT License](https://github.com/DayanidhiGudimetla/ecommerce-order-management/blob/main/LICENSE).
