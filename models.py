from db import connect
from validators import validate_positive_float, validate_non_negative_int, validate_email, validate_non_empty
from utils import hash_password, verify_password, print_table

# ──────────────────────────────────────────────
# USER OPERATIONS
# ──────────────────────────────────────────────

def register_user():
    """Register a new user with salted SHA-256 hashed password."""
    conn = connect()
    cur = conn.cursor()
    try:
        name     = validate_non_empty(input("  Full Name: "), "Name")
        email    = validate_email(input("  Email: "))
        password = validate_non_empty(input("  Password: "), "Password")

        # Generate unique salt + hash for this user
        hashed, salt = hash_password(password)

        cur.execute(
            "INSERT INTO users (name, email, password, salt) VALUES (?, ?, ?, ?)",
            (name, email, hashed, salt)
        )
        conn.commit()
        print("  ✅ User registered successfully!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


def login_user():
    """Login a user and return user_id if successful."""
    conn = connect()
    cur = conn.cursor()
    try:
        email    = input("  Email: ").strip()
        password = input("  Password: ").strip()

        # Fetch stored hash AND salt for this user
        cur.execute("SELECT id, name, password, salt FROM users WHERE email=?", (email,))
        row = cur.fetchone()

        if not row:
            print("  ❌ User not found.")
            return None

        # Verify using the stored salt
        if verify_password(password, row["password"], row["salt"]):
            print(f"  ✅ Welcome back, {row['name']}!")
            return row["id"]
        else:
            print("  ❌ Incorrect password.")
            return None

    except Exception as e:
        print(f"  ❌ Error: {e}")
        return None
    finally:
        conn.close()


def view_all_users():
    """Display all registered users."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email, created_at FROM users")
    rows = cur.fetchall()
    conn.close()
    print("\n  --- All Users ---")
    print_table(["ID", "Name", "Email", "Registered At"], [tuple(r) for r in rows])


# ──────────────────────────────────────────────
# PRODUCT OPERATIONS
# ──────────────────────────────────────────────

def add_product():
    """Add a new product to the catalog."""
    conn = connect()
    cur = conn.cursor()
    try:
        name     = validate_non_empty(input("  Product Name: "), "Product Name")
        price    = validate_positive_float(input("  Price: "), "Price")
        stock    = validate_non_negative_int(input("  Stock Quantity: "), "Stock")
        category = input("  Category (default: General): ").strip() or "General"

        cur.execute(
            "INSERT INTO products (name, price, stock, category) VALUES (?, ?, ?, ?)",
            (name, price, stock, category)
        )
        conn.commit()
        print("  ✅ Product added successfully!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


def view_products():
    """Display all available products."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price, stock, category FROM products ORDER BY category, name")
    rows = cur.fetchall()
    conn.close()
    print("\n  --- Product Catalog ---")
    print_table(["ID", "Name", "Price (₹)", "Stock", "Category"], [tuple(r) for r in rows])


def update_stock():
    """Update stock quantity for a product."""
    conn = connect()
    cur = conn.cursor()
    try:
        view_products()
        pid       = int(input("\n  Enter Product ID to update stock: "))
        new_stock = validate_non_negative_int(input("  New Stock Quantity: "), "Stock")

        cur.execute("UPDATE products SET stock=? WHERE id=?", (new_stock, pid))
        if cur.rowcount == 0:
            print("  ❌ Product not found.")
        else:
            conn.commit()
            print("  ✅ Stock updated successfully!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


def update_price():
    """Update price for a product."""
    conn = connect()
    cur = conn.cursor()
    try:
        view_products()
        pid       = int(input("\n  Enter Product ID to update price: "))
        new_price = validate_positive_float(input("  New Price: "), "Price")

        cur.execute("UPDATE products SET price=? WHERE id=?", (new_price, pid))
        if cur.rowcount == 0:
            print("  ❌ Product not found.")
        else:
            conn.commit()
            print("  ✅ Price updated successfully!")
    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


def low_stock_alert():
    """Show products with stock below threshold."""
    conn = connect()
    cur = conn.cursor()
    threshold = 5
    cur.execute("SELECT id, name, stock, category FROM products WHERE stock < ?", (threshold,))
    rows = cur.fetchall()
    conn.close()
    print(f"\n  --- Low Stock Alert (stock < {threshold}) ---")
    print_table(["ID", "Name", "Stock", "Category"], [tuple(r) for r in rows])
