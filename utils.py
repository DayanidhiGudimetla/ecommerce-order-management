import hashlib
import csv

def hash_password(password):
    """Hash password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(input_password, stored_hash):
    """Verify entered password against stored hash."""
    return hash_password(input_password) == stored_hash

def export_to_csv(filename, headers, rows):
    """Export data to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"✅ Data exported to '{filename}'")

def print_table(headers, rows):
    """Print data in a formatted table."""
    if not rows:
        print("  No records found.")
        return

    col_widths = [len(h) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    separator = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    header_row = "| " + " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"

    print(separator)
    print(header_row)
    print(separator)
    for row in rows:
        print("| " + " | ".join(str(v).ljust(col_widths[i]) for i, v in enumerate(row)) + " |")
    print(separator)
