PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS users (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT    NOT NULL,
    email      TEXT    UNIQUE NOT NULL,
    password   TEXT    NOT NULL,
    salt       TEXT    NOT NULL,                          -- random salt for SHA-256 hashing
    created_at TEXT    DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS products (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    name       TEXT  UNIQUE NOT NULL,
    price      REAL  CHECK(price > 0),
    stock      INTEGER CHECK(stock >= 0) DEFAULT 0,
    category   TEXT  DEFAULT 'General',
    created_at TEXT  DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS orders (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id    INTEGER NOT NULL,
    total      REAL,
    status     TEXT DEFAULT 'pending',
    created_at TEXT DEFAULT (datetime('now')),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS order_items (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id   INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity   INTEGER CHECK(quantity > 0),
    unit_price REAL,
    FOREIGN KEY(order_id)   REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
);
