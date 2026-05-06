-- ============================================
-- RETAIL SALES ANALYSIS - ALL QUERIES
-- ============================================

USE retail_sales;

-- -----------------------------------------------
-- QUERY 1: Total Revenue by Category
-- -----------------------------------------------
SELECT 
    p.category,
    SUM(p.price * oi.quantity)                          AS gross_revenue,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS net_revenue,
    COUNT(DISTINCT oi.order_id)                         AS total_orders
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category
ORDER BY net_revenue DESC;


-- -----------------------------------------------
-- QUERY 2: Top 5 Best-Selling Products
-- -----------------------------------------------
SELECT 
    p.product_name,
    p.category,
    SUM(oi.quantity)                                    AS units_sold,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS net_revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name, p.category
ORDER BY units_sold DESC
LIMIT 5;


-- -----------------------------------------------
-- QUERY 3: Monthly Revenue Trend
-- -----------------------------------------------
SELECT 
    DATE_FORMAT(o.order_date, '%Y-%m')                  AS month,
    COUNT(DISTINCT o.order_id)                          AS total_orders,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS monthly_revenue
FROM orders o
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p     ON oi.product_id = p.product_id
GROUP BY month
ORDER BY month;


-- -----------------------------------------------
-- QUERY 4: Top 5 Customers by Total Spending
-- -----------------------------------------------
SELECT 
    c.customer_name,
    c.city,
    c.state,
    COUNT(DISTINCT o.order_id)                          AS total_orders,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS total_spent
FROM customers c
JOIN orders     o  ON c.customer_id  = o.customer_id
JOIN order_items oi ON o.order_id   = oi.order_id
JOIN products p    ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name, c.city, c.state
ORDER BY total_spent DESC
LIMIT 5;


-- -----------------------------------------------
-- QUERY 5: Revenue by State
-- -----------------------------------------------
SELECT 
    c.state,
    COUNT(DISTINCT c.customer_id)                       AS total_customers,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS state_revenue
FROM customers c
JOIN orders      o  ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id    = oi.order_id
JOIN products p     ON oi.product_id = p.product_id
GROUP BY c.state
ORDER BY state_revenue DESC;


-- -----------------------------------------------
-- QUERY 6: Average Order Value
-- -----------------------------------------------
SELECT 
    ROUND(AVG(order_total), 2)  AS avg_order_value,
    MAX(order_total)            AS highest_order,
    MIN(order_total)            AS lowest_order
FROM (
    SELECT 
        o.order_id,
        SUM(p.price * oi.quantity * (1 - oi.discount)) AS order_total
    FROM orders o
    JOIN order_items oi ON o.order_id    = oi.order_id
    JOIN products p     ON oi.product_id = p.product_id
    GROUP BY o.order_id
) AS order_summary;


-- -----------------------------------------------
-- QUERY 7: Product Rank Within Each Category
--          (Window Function)
-- -----------------------------------------------
SELECT 
    p.category,
    p.product_name,
    SUM(oi.quantity)                                    AS units_sold,
    RANK() OVER (
        PARTITION BY p.category 
        ORDER BY SUM(oi.quantity) DESC
    )                                                   AS rank_in_category
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.category, p.product_id, p.product_name
ORDER BY p.category, rank_in_category;


-- -----------------------------------------------
-- QUERY 8: Repeat Customers
-- -----------------------------------------------
SELECT 
    c.customer_name,
    c.city,
    COUNT(o.order_id)                                   AS total_orders,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS lifetime_value
FROM customers c
JOIN orders      o  ON c.customer_id = o.customer_id
JOIN order_items oi ON o.order_id    = oi.order_id
JOIN products p     ON oi.product_id = p.product_id
GROUP BY c.customer_id, c.customer_name, c.city
HAVING total_orders > 1
ORDER BY total_orders DESC, lifetime_value DESC;


-- -----------------------------------------------
-- QUERY 9: Discount Impact on Revenue
-- -----------------------------------------------
SELECT 
    p.product_name,
    p.category,
    SUM(p.price * oi.quantity)                          AS gross_revenue,
    ROUND(SUM(p.price * oi.quantity * oi.discount), 2)  AS discount_given,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS net_revenue,
    ROUND(
        SUM(p.price * oi.quantity * oi.discount) /
        SUM(p.price * oi.quantity) * 100, 2
    )                                                   AS discount_pct
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY discount_given DESC;


-- -----------------------------------------------
-- QUERY 10: Year-over-Year Revenue Growth (CTE)
-- -----------------------------------------------
WITH yearly_revenue AS (
    SELECT 
        YEAR(o.order_date)                              AS yr,
        SUM(p.price * oi.quantity * (1 - oi.discount))  AS revenue
    FROM orders o
    JOIN order_items oi ON o.order_id    = oi.order_id
    JOIN products p     ON oi.product_id = p.product_id
    GROUP BY yr
)
SELECT 
    yr,
    ROUND(revenue, 2)                                   AS revenue,
    ROUND(LAG(revenue) OVER (ORDER BY yr), 2)           AS prev_year_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY yr)) /
         LAG(revenue) OVER (ORDER BY yr) * 100, 2
    )                                                   AS yoy_growth_pct
FROM yearly_revenue
ORDER BY yr;


-- -----------------------------------------------
-- QUERY 11: Ship Mode Performance
-- -----------------------------------------------
SELECT 
    o.ship_mode,
    COUNT(DISTINCT o.order_id)                          AS total_orders,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS total_revenue,
    ROUND(AVG(p.price * oi.quantity * (1 - oi.discount)), 2) AS avg_order_value
FROM orders o
JOIN order_items oi ON o.order_id    = oi.order_id
JOIN products p     ON oi.product_id = p.product_id
GROUP BY o.ship_mode
ORDER BY total_revenue DESC;


-- -----------------------------------------------
-- QUERY 12: Quarterly Sales Summary
-- -----------------------------------------------
SELECT 
    YEAR(o.order_date)                                  AS yr,
    QUARTER(o.order_date)                               AS quarter,
    COUNT(DISTINCT o.order_id)                          AS orders,
    SUM(p.price * oi.quantity * (1 - oi.discount))      AS quarterly_revenue
FROM orders o
JOIN order_items oi ON o.order_id    = oi.order_id
JOIN products p     ON oi.product_id = p.product_id
GROUP BY yr, quarter
ORDER BY yr, quarter;
