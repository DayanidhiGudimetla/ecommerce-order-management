-- ============================================
-- RETAIL SALES ANALYSIS - SAMPLE DATA
-- ============================================

USE retail_sales;

-- ----------------------
-- Insert Customers
-- ----------------------
INSERT INTO customers (customer_name, email, city, state) VALUES
('Rahul Sharma',    'rahul@email.com',   'Mumbai',      'Maharashtra'),
('Priya Nair',      'priya@email.com',   'Kochi',       'Kerala'),
('Amit Patel',      'amit@email.com',    'Ahmedabad',   'Gujarat'),
('Sneha Reddy',     'sneha@email.com',   'Hyderabad',   'Telangana'),
('Vikram Singh',    'vikram@email.com',  'Delhi',       'Delhi'),
('Deepa Menon',     'deepa@email.com',   'Bangalore',   'Karnataka'),
('Rohit Kumar',     'rohit@email.com',   'Chennai',     'Tamil Nadu'),
('Anjali Gupta',    'anjali@email.com',  'Pune',        'Maharashtra'),
('Suresh Babu',     'suresh@email.com',  'Vizag',       'Andhra Pradesh'),
('Kavya Thomas',    'kavya@email.com',   'Thrissur',    'Kerala');

-- ----------------------
-- Insert Products
-- ----------------------
INSERT INTO products (product_name, category, sub_category, price) VALUES
('Samsung Galaxy S23',     'Electronics',  'Mobiles',    79999.00),
('Apple MacBook Air M2',   'Electronics',  'Laptops',   114999.00),
('Sony WH-1000XM5',        'Electronics',  'Audio',      29999.00),
('Levi\'s 511 Jeans',      'Clothing',     'Bottoms',     3499.00),
('Nike Air Max 270',       'Footwear',     'Sneakers',    8999.00),
('Prestige Induction',     'Appliances',   'Kitchen',     3299.00),
('Wildcraft Backpack',     'Accessories',  'Bags',        2499.00),
('Atomic Habits Book',     'Books',        'Self-Help',    499.00),
('Yoga Mat Premium',       'Sports',       'Fitness',     1299.00),
('Boat Airdopes 141',      'Electronics',  'Audio',       1299.00),
('HP LaserJet Printer',    'Electronics',  'Printers',   14999.00),
('Puma Track Pants',       'Clothing',     'Bottoms',     1799.00),
('Milton Water Bottle',    'Accessories',  'Kitchen',      399.00),
('Fastrack Wristwatch',    'Accessories',  'Watches',     2999.00),
('Classmate Notebook Set', 'Stationery',   'Notebooks',    299.00);

-- ----------------------
-- Insert Orders
-- ----------------------
INSERT INTO orders (customer_id, order_date, ship_mode) VALUES
(1,  '2024-01-05', 'Standard'),
(2,  '2024-01-12', 'Express'),
(3,  '2024-02-03', 'Standard'),
(4,  '2024-02-18', 'Express'),
(5,  '2024-03-07', 'Standard'),
(6,  '2024-03-22', 'Express'),
(7,  '2024-04-10', 'Standard'),
(8,  '2024-04-25', 'Standard'),
(9,  '2024-05-08', 'Express'),
(10, '2024-05-19', 'Standard'),
(1,  '2024-06-01', 'Express'),   -- Repeat customer
(2,  '2024-06-15', 'Standard'),  -- Repeat customer
(3,  '2024-07-04', 'Express'),
(5,  '2024-07-20', 'Standard'),  -- Repeat customer
(6,  '2024-08-09', 'Express'),
(7,  '2024-08-25', 'Standard'),
(4,  '2024-09-11', 'Express'),   -- Repeat customer
(8,  '2024-09-28', 'Standard'),
(9,  '2024-10-14', 'Express'),
(10, '2024-11-03', 'Standard'),
(1,  '2024-11-22', 'Express'),   -- Repeat customer
(2,  '2024-12-05', 'Standard'),
(5,  '2024-12-19', 'Express'),   -- Repeat customer
(3,  '2025-01-08', 'Standard'),
(6,  '2025-01-25', 'Express');

-- ----------------------
-- Insert Order Items
-- ----------------------
INSERT INTO order_items (order_id, product_id, quantity, discount) VALUES
(1,  1,  1, 0.05),
(1,  10, 2, 0.00),
(2,  3,  1, 0.10),
(3,  2,  1, 0.05),
(4,  5,  2, 0.00),
(4,  4,  1, 0.10),
(5,  6,  1, 0.00),
(5,  9,  3, 0.05),
(6,  7,  2, 0.00),
(6,  8,  4, 0.10),
(7,  11, 1, 0.05),
(7,  14, 1, 0.00),
(8,  12, 2, 0.10),
(8,  13, 5, 0.00),
(9,  1,  1, 0.00),
(10, 15,10, 0.05),
(10, 8,  3, 0.00),
(11, 3,  1, 0.10),
(11, 10, 1, 0.00),
(12, 4,  2, 0.05),
(13, 2,  1, 0.00),
(14, 5,  1, 0.10),
(14, 9,  2, 0.05),
(15, 6,  2, 0.00),
(16, 7,  1, 0.10),
(17, 11, 1, 0.05),
(18, 12, 3, 0.00),
(19, 1,  2, 0.10),
(20, 13, 4, 0.00),
(21, 3,  1, 0.05),
(22, 14, 2, 0.10),
(23, 2,  1, 0.00),
(24, 5,  3, 0.05),
(25, 8,  5, 0.00);
