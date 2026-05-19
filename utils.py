import hashlib
import csv
import os


def hash_password(password: str, salt: str = None):
    """
    Hash password using SHA-256 with a random salt.
    - salt is auto-generated on registration (first call)
    - salt must be passed on login (verify call)
    Returns: (hashed_password, salt)
    """
    if salt is None:
        salt = os.urandom(16).hex()  # 16-byte random salt → unique per user
    salted = (salt + password).encode()
    hashed = hashlib.sha256(salted).hexdigest()
    return hashed, salt


def verify_password(input_password: str, stored_hash: str, salt: str) -> bool:
    """Verify entered password against stored hash using the original salt."""
    hashed, _ = hash_password(input_password, salt)
    return hashed == stored_hash


def export_to_csv(filename: str, headers: list, rows: list) -> None:
    """Export data to a CSV file."""
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f"✅ Data exported to '{filename}'")


def print_table(headers: list, rows: list) -> None:
    """Print data in a clean formatted table."""
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
