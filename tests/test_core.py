"""
Unit tests for E-Commerce Order Management System
Run with: pytest tests/test_core.py -v
"""
import pytest
import os
import csv
import sys

# Make sure imports work when running from repo root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import hash_password, verify_password, export_to_csv


# ── Password Hashing Tests ─────────────────────────────────────────────────

def test_hash_password_returns_tuple():
    """hash_password should return (hash, salt) tuple."""
    result = hash_password("mypassword")
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_hash_is_64_chars():
    """SHA-256 hex digest must always be exactly 64 characters."""
    hashed, salt = hash_password("testpass")
    assert len(hashed) == 64


def test_salt_is_32_chars():
    """Salt should be 16 bytes = 32 hex characters."""
    _, salt = hash_password("testpass")
    assert len(salt) == 32


def test_same_password_different_salts_produce_different_hashes():
    """Two registrations with the same password must produce different hashes."""
    hash1, salt1 = hash_password("password123")
    hash2, salt2 = hash_password("password123")
    assert hash1 != hash2      # Different hashes
    assert salt1 != salt2      # Different salts


def test_verify_correct_password_returns_true():
    """Correct password must verify successfully."""
    hashed, salt = hash_password("secure123")
    assert verify_password("secure123", hashed, salt) is True


def test_verify_wrong_password_returns_false():
    """Wrong password must fail verification."""
    hashed, salt = hash_password("secure123")
    assert verify_password("wrongpass", hashed, salt) is False


def test_verify_password_wrong_salt_fails():
    """Correct password with wrong salt must fail."""
    hashed, salt = hash_password("secure123")
    _, wrong_salt = hash_password("other")
    assert verify_password("secure123", hashed, wrong_salt) is False


def test_hash_password_with_provided_salt_is_deterministic():
    """Same password + same salt must always produce the same hash (login flow)."""
    hashed1, salt = hash_password("mypass")
    hashed2, _   = hash_password("mypass", salt)
    assert hashed1 == hashed2


# ── CSV Export Tests ────────────────────────────────────────────────────────

def test_export_to_csv_creates_file(tmp_path):
    """export_to_csv must create the file on disk."""
    filepath = str(tmp_path / "report.csv")
    export_to_csv(filepath, ["Product", "Qty", "Revenue"], [("Laptop", 5, 50000)])
    assert os.path.exists(filepath)


def test_export_to_csv_correct_headers(tmp_path):
    """First row in CSV must match provided headers exactly."""
    filepath = str(tmp_path / "report.csv")
    export_to_csv(filepath, ["Name", "Amount"], [("Order A", 1000)])
    with open(filepath, newline="") as f:
        reader = list(csv.reader(f))
    assert reader[0] == ["Name", "Amount"]


def test_export_to_csv_correct_data_rows(tmp_path):
    """Data rows must be written correctly after the header."""
    filepath = str(tmp_path / "report.csv")
    export_to_csv(filepath, ["Name", "Amount"], [("Order A", 1000), ("Order B", 2000)])
    with open(filepath, newline="") as f:
        reader = list(csv.reader(f))
    assert reader[1] == ["Order A", "1000"]
    assert reader[2] == ["Order B", "2000"]


def test_export_to_csv_empty_rows_only_header(tmp_path):
    """Empty rows list should produce a file with only the header row."""
    filepath = str(tmp_path / "empty.csv")
    export_to_csv(filepath, ["Col1", "Col2"], [])
    with open(filepath, newline="") as f:
        reader = list(csv.reader(f))
    assert len(reader) == 1
    assert reader[0] == ["Col1", "Col2"]
