-- ============================================
-- RETAIL SALES ANALYSIS - DATABASE SCHEMA
-- ============================================

CREATE DATABASE IF NOT EXISTS retail_sales;
USE retail_sales;

-- Customers Table
CREATE TABLE customers (
    customer_id   INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    email         VARCHAR(100),
    city          VARCHAR(50),
    state         VARCHAR(50),
    country       VARCHAR(50) DEFAULT 'India'
);

-- Products Table
CREATE TABLE products (
    product_id   INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category     VARCHAR(50),
    sub_category VARCHAR(50),
    price        DECIMAL(10,2) NOT NULL
);

-- Orders Table
CREATE TABLE orders (
    order_id    INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date  DATE NOT NULL,
    ship_mode   VARCHAR(50),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Order Items Table
CREATE TABLE order_items (
    item_id    INT PRIMARY KEY AUTO_INCREMENT,
    order_id   INT NOT NULL,
    product_id INT NOT NULL,
    quantity   INT NOT NULL DEFAULT 1,
    discount   DECIMAL(4,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (order_id)   REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
