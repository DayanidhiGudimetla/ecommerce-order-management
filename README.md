# 🛒 Retail Sales Analysis — SQL Project

A complete SQL project analyzing retail sales data to uncover revenue trends, top products, customer behavior, and business insights.

---

## 📁 Project Structure

```
retail-sales-sql/
│
├── schema.sql                  # Database & table creation
├── data/
│   └── sample_data.sql         # Sample data (customers, products, orders)
├── queries/
│   └── analysis_queries.sql    # All 12 analysis queries
├── docs/
│   └── insights.md             # Key findings & insights
└── README.md
```

---

## 🗄️ Database Schema

```
customers ──< orders ──< order_items >── products
```

| Table | Description |
|-------|-------------|
| `customers` | Customer info (name, city, state) |
| `products` | Product catalog with price & category |
| `orders` | Order header (date, ship mode) |
| `order_items` | Line items with quantity & discount |

---

## 🔍 Queries Covered

| # | Query | Concepts Used |
|---|-------|---------------|
| 1 | Total Revenue by Category | GROUP BY, SUM, JOIN |
| 2 | Top 5 Best-Selling Products | ORDER BY, LIMIT |
| 3 | Monthly Revenue Trend | DATE_FORMAT, GROUP BY |
| 4 | Top 5 Customers by Spending | Multi-table JOIN |
| 5 | Revenue by State | GROUP BY, Aggregation |
| 6 | Average Order Value | Subquery, AVG/MAX/MIN |
| 7 | Product Rank in Category | RANK(), PARTITION BY |
| 8 | Repeat Customers | HAVING, COUNT |
| 9 | Discount Impact | Calculated columns |
| 10 | Year-over-Year Growth | CTE, LAG() Window Function |
| 11 | Ship Mode Performance | GROUP BY, AVG |
| 12 | Quarterly Sales Summary | QUARTER(), YEAR() |

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/retail-sales-sql.git
cd retail-sales-sql
```

### 2. Set Up Database (MySQL)
```bash
mysql -u root -p < schema.sql
mysql -u root -p retail_sales < data/sample_data.sql
```

### 3. Run Queries
```bash
mysql -u root -p retail_sales < queries/analysis_queries.sql
```

Or open in **MySQL Workbench / DBeaver** and run manually.

---

## 💡 Key Insights

- **Electronics** is the top revenue-generating category
- **Repeat customers** drive ~40% of total revenue
- **Q4** shows highest quarterly sales (festive season)
- **Express shipping** orders have higher average order value
- Discounts beyond **10%** significantly reduce net margins

---

## 🛠️ Tools Used

- **MySQL 8.0** — Database engine
- **MySQL Workbench** — Query editor
- **Power BI / Tableau** *(optional)* — Dashboard visualization

---

## 📊 Dataset

Sample data is included in `/data/sample_data.sql`.  
For a larger real-world dataset, download from:  
🔗 [Kaggle Superstore Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

---

## 👤 Author

**Your Name**  
📧 gudimetladaya11@gmail.com 
🔗 [LinkedIn](https://www.linkedin.com/in/dayanidhi-gudimetla-2b08013ab)
🐙 [GitHub](https://github.com/DayanidhiGudimetla)

---

## 📄 License

MIT License — free to use and modify.
