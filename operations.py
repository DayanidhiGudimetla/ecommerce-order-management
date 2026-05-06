from db import connect
from models import view_products
from utils import print_table, export_to_csv
from validators import validate_positive_int

# ──────────────────────────────────────────────
# ORDER OPERATIONS
# ──────────────────────────────────────────────

def place_order(user_id):
    """Place a new order with stock validation and atomic transaction."""
    conn = connect()
    cur = conn.cursor()
    try:
        view_products()

        n = validate_positive_int(input("\n  How many products to order? "), "Count")
        items = []

        for i in range(n):
            print(f"\n  Item {i + 1}:")
            pid = int(input("    Product ID: "))
            qty = validate_positive_int(input("    Quantity: "), "Quantity")

            # Validate product and stock
            cur.execute("SELECT id, name, price, stock FROM products WHERE id=?", (pid,))
            product = cur.fetchone()

            if not product:
                print(f"    ❌ Product ID {pid} not found. Skipping.")
                continue

            if qty > product["stock"]:
                print(f"    ❌ Insufficient stock for '{product['name']}'. Available: {product['stock']}. Skipping.")
                continue

            items.append((pid, qty, product["price"], product["name"]))

        if not items:
            print("\n  ❌ No valid items to order.")
            return

        # Show order summary
        print("\n  --- Order Summary ---")
        total = 0
        for pid, qty, price, name in items:
            subtotal = price * qty
            total += subtotal
            print(f"    {name} x{qty} @ ₹{price:.2f} = ₹{subtotal:.2f}")
        print(f"    {'─'*35}")
        print(f"    Total: ₹{total:.2f}")

        confirm = input("\n  Confirm order? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("  ❌ Order cancelled.")
            return

        # Atomic transaction — all or nothing
        cur.execute("BEGIN")

        cur.execute(
            "INSERT INTO orders (user_id, total, status) VALUES (?, ?, 'confirmed')",
            (user_id, total)
        )
        order_id = cur.lastrowid

        for pid, qty, price, _ in items:
            cur.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES (?, ?, ?, ?)",
                (order_id, pid, qty, price)
            )
            cur.execute(
                "UPDATE products SET stock = stock - ? WHERE id=?",
                (qty, pid)
            )

        conn.commit()
        print(f"\n  ✅ Order #{order_id} placed successfully! Total: ₹{total:.2f}")

    except Exception as e:
        conn.rollback()
        print(f"  ❌ Order failed, rolled back. Error: {e}")
    finally:
        conn.close()


def view_my_orders(user_id):
    """View all orders for a specific user."""
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT o.id, o.total, o.status, o.created_at
        FROM orders o
        WHERE o.user_id = ?
        ORDER BY o.created_at DESC
    """, (user_id,))
    orders = cur.fetchall()
    conn.close()

    print("\n  --- My Orders ---")
    if not orders:
        print("  No orders found.")
        return

    print_table(["Order ID", "Total (₹)", "Status", "Date"], [tuple(r) for r in orders])


def view_order_details(user_id):
    """View detailed items of a specific order."""
    conn = connect()
    cur = conn.cursor()
    try:
        view_my_orders(user_id)
        order_id = int(input("\n  Enter Order ID to view details: "))

        # Verify order belongs to user
        cur.execute("SELECT id FROM orders WHERE id=? AND user_id=?", (order_id, user_id))
        if not cur.fetchone():
            print("  ❌ Order not found or does not belong to you.")
            return

        cur.execute("""
            SELECT p.name, oi.quantity, oi.unit_price, (oi.quantity * oi.unit_price) AS subtotal
            FROM order_items oi
            JOIN products p ON p.id = oi.product_id
            WHERE oi.order_id = ?
        """, (order_id,))
        items = cur.fetchall()

        print(f"\n  --- Order #{order_id} Details ---")
        print_table(["Product", "Quantity", "Unit Price (₹)", "Subtotal (₹)"], [tuple(r) for r in items])

    except Exception as e:
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


def cancel_order(user_id):
    """Cancel a pending/confirmed order and restore stock."""
    conn = connect()
    cur = conn.cursor()
    try:
        view_my_orders(user_id)
        order_id = int(input("\n  Enter Order ID to cancel: "))

        cur.execute(
            "SELECT id, status FROM orders WHERE id=? AND user_id=?",
            (order_id, user_id)
        )
        order = cur.fetchone()

        if not order:
            print("  ❌ Order not found.")
            return

        if order["status"] == "cancelled":
            print("  ❌ Order is already cancelled.")
            return

        # Restore stock atomically
        cur.execute("BEGIN")

        cur.execute("SELECT product_id, quantity FROM order_items WHERE order_id=?", (order_id,))
        items = cur.fetchall()

        for item in items:
            cur.execute(
                "UPDATE products SET stock = stock + ? WHERE id=?",
                (item["quantity"], item["product_id"])
            )

        cur.execute("UPDATE orders SET status='cancelled' WHERE id=?", (order_id,))
        conn.commit()
        print(f"  ✅ Order #{order_id} cancelled. Stock restored.")

    except Exception as e:
        conn.rollback()
        print(f"  ❌ Error: {e}")
    finally:
        conn.close()


# ──────────────────────────────────────────────
# ANALYTICS & REPORTS
# ──────────────────────────────────────────────

def analytics():
    """Show business analytics and revenue reports."""
    conn = connect()
    cur = conn.cursor()

    print("\n  --- Business Analytics ---")

    # Total revenue
    cur.execute("SELECT SUM(total) FROM orders WHERE status != 'cancelled'")
    revenue = cur.fetchone()[0] or 0
    print(f"\n  💰 Total Revenue: ₹{revenue:.2f}")

    # Total orders
    cur.execute("SELECT COUNT(*) FROM orders WHERE status != 'cancelled'")
    total_orders = cur.fetchone()[0]
    print(f"  📦 Total Orders: {total_orders}")

    # Top selling products
    cur.execute("""
        SELECT p.name, SUM(oi.quantity) AS total_qty, SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        JOIN products p ON p.id = oi.product_id
        JOIN orders o ON o.id = oi.order_id
        WHERE o.status != 'cancelled'
        GROUP BY p.name
        ORDER BY total_qty DESC
        LIMIT 5
    """)
    rows = cur.fetchall()
    print("\n  🏆 Top 5 Best Selling Products:")
    print_table(["Product", "Qty Sold", "Revenue (₹)"], [tuple(r) for r in rows])

    # Revenue by category
    cur.execute("""
        SELECT p.category, SUM(oi.quantity * oi.unit_price) AS revenue
        FROM order_items oi
        JOIN products p ON p.id = oi.product_id
        JOIN orders o ON o.id = oi.order_id
        WHERE o.status != 'cancelled'
        GROUP BY p.category
        ORDER BY revenue DESC
    """)
    rows = cur.fetchall()
    print("\n  📊 Revenue by Category:")
    print_table(["Category", "Revenue (₹)"], [tuple(r) for r in rows])

    conn.close()


def export_sales_report():
    """Export full sales report to CSV."""
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT u.name AS customer, p.name AS product,
               oi.quantity, oi.unit_price,
               (oi.quantity * oi.unit_price) AS subtotal,
               o.status, o.created_at
        FROM order_items oi
        JOIN orders o ON o.id = oi.order_id
        JOIN users u ON u.id = o.user_id
        JOIN products p ON p.id = oi.product_id
        ORDER BY o.created_at DESC
    """)
    rows = cur.fetchall()
    conn.close()

    headers = ["Customer", "Product", "Quantity", "Unit Price", "Subtotal", "Status", "Date"]
    export_to_csv("sales_report.csv", headers, [tuple(r) for r in rows])
