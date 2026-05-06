from models import (
    register_user, login_user, view_all_users,
    add_product, view_products, update_stock,
    update_price, low_stock_alert
)
from operations import (
    place_order, view_my_orders, view_order_details,
    cancel_order, analytics, export_sales_report
)

current_user = None  # Stores logged-in user ID

# ──────────────────────────────────────────────
# MENUS
# ──────────────────────────────────────────────

def auth_menu():
    print("\n╔══════════════════════════════╗")
    print("║   E-Commerce Management CLI  ║")
    print("╚══════════════════════════════╝")
    print("  1. Register")
    print("  2. Login")
    print("  3. Exit")

def admin_menu():
    print("\n╔══════════════════════════════╗")
    print("║        ADMIN PANEL           ║")
    print("╚══════════════════════════════╝")
    print("  --- Products ---")
    print("  1. Add Product")
    print("  2. View All Products")
    print("  3. Update Stock")
    print("  4. Update Price")
    print("  5. Low Stock Alert")
    print("  --- Users ---")
    print("  6. View All Users")
    print("  --- Reports ---")
    print("  7. Analytics Dashboard")
    print("  8. Export Sales Report (CSV)")
    print("  --- Account ---")
    print("  9. Logout")

def user_menu():
    print("\n╔══════════════════════════════╗")
    print("║        USER PANEL            ║")
    print("╚══════════════════════════════╝")
    print("  1. Browse Products")
    print("  2. Place Order")
    print("  3. My Orders")
    print("  4. Order Details")
    print("  5. Cancel Order")
    print("  6. Logout")

# ──────────────────────────────────────────────
# MAIN APP
# ──────────────────────────────────────────────

def run():
    global current_user

    while True:
        if current_user is None:
            auth_menu()
            choice = input("\n  Choice: ").strip()

            if choice == "1":
                register_user()

            elif choice == "2":
                uid = login_user()
                if uid:
                    current_user = uid

            elif choice == "3":
                print("\n  👋 Goodbye!")
                break

            else:
                print("  ❌ Invalid choice.")

        else:
            # Simple role: user_id == 1 is admin
            if current_user == 1:
                admin_menu()
                choice = input("\n  Choice: ").strip()

                if choice == "1":
                    add_product()
                elif choice == "2":
                    view_products()
                elif choice == "3":
                    update_stock()
                elif choice == "4":
                    update_price()
                elif choice == "5":
                    low_stock_alert()
                elif choice == "6":
                    view_all_users()
                elif choice == "7":
                    analytics()
                elif choice == "8":
                    export_sales_report()
                elif choice == "9":
                    current_user = None
                    print("  ✅ Logged out.")
                else:
                    print("  ❌ Invalid choice.")

            else:
                user_menu()
                choice = input("\n  Choice: ").strip()

                if choice == "1":
                    view_products()
                elif choice == "2":
                    place_order(current_user)
                elif choice == "3":
                    view_my_orders(current_user)
                elif choice == "4":
                    view_order_details(current_user)
                elif choice == "5":
                    cancel_order(current_user)
                elif choice == "6":
                    current_user = None
                    print("  ✅ Logged out.")
                else:
                    print("  ❌ Invalid choice.")

if __name__ == "__main__":
    run()
