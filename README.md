# 🛒 Amazon India: A Decade of Sales Analytics 📈🇮🇳

## 📌 Project Overview
This project analyzes **10 years of synthetic e-commerce transactional data (2015–2025)** from Amazon India, covering **~1 million transactions**.  
It demonstrates an **end-to-end data analytics pipeline** — from raw messy data to professional **Business Intelligence dashboards** — delivering actionable insights for revenue growth, customer segmentation, inventory optimization, and operational efficiency.

---

## 👤 Author
**Sarath Kumar R**  
GitHub Repository: [https://github.com/SK112713/amazon-india-sales-analytics.git](https://github.com/SK112713/amazon-india-sales-analytics.git)

---

## 🎯 Problem Statement
Build a comprehensive **e-commerce analytics platform** that:
- Cleans and processes messy transactional data with **25% data quality issues**.
- Performs **Exploratory Data Analysis (EDA)** with 20+ visualizations.
- Stores cleaned data in an **SQL database** for analytics.
- Creates **interactive dashboards** using **Power BI** or **Streamlit**.
- Generates **strategic business insights** for decision-making.

---

## 📊 Business Use Cases
1. **E-Commerce Platform Management**
 - Revenue trend analysis & forecasting
 - Product category performance optimization
 - Customer segmentation for targeted marketing
 - Geographic expansion analysis

2. **Business Intelligence & Strategic Planning**
 - Executive dashboards for C-level decisions
 - KPI monitoring & seasonal pattern analysis
 - Market penetration insights

3. **Digital Marketing & Customer Analytics**
 - Customer behavior analysis
 - Festival sales impact measurement
 - Payment method evolution tracking
 - Prime membership value analysis

4. **Financial & Operational Excellence**
 - Pricing strategy optimization
 - Delivery performance tracking
 - Return rate analysis
 - Cost structure analysis

---

## 🏗 Project Workflow

### **Phase 1: Data Understanding & Cleaning**
- Load and inspect raw dataset (`amazon_india_complete_2015_2025.csv`)
- Handle missing values, inconsistent formats, duplicates, and outliers
- Standardize:
- Dates (`YYYY-MM-DD`)
- Prices (numeric INR)
- Ratings (1.0–5.0 scale)
- City names
- Boolean values
- Product categories
- Payment methods

### **Phase 2: Exploratory Data Analysis (EDA)**
- Revenue trends (2015–2025)
- Seasonal sales patterns
- RFM customer segmentation
- Payment method evolution
- Geographic performance
- Festival sales impact
- Price vs demand correlation
- Product rating impact on sales

### **Phase 3: SQL Database Integration**
- Create tables: `transactions`, `products`, `customers`, `time_dimension`
- Bulk insert cleaned data
- Create indexes for performance
- Write aggregation queries for KPIs

### **Phase 4: Dashboard Development**
- Using **Streamlit**
- 25–30 interactive visualizations
- Executive summary, revenue analytics, customer analytics, product & inventory analytics, operations & logistics, advanced analytics

### **Phase 5: Business Insights & Reporting**
- Identify top-performing categories
- Track fastest-growing payment methods
- Analyze Prime membership impact
- Recommend pricing & discount strategies
- Suggest inventory planning improvements

---

## 📂 Project Structure
amazon-india-sales-analytics/ 
│── data/           # Raw & cleaned datasets 
│── notebooks/      # Jupyter notebooks for data understanding
│── scripts/        # Scripts for data cleaning and EDA analysis
│── sql/            # SQL schema & queries 
│── dashboard/      # Power BI or Streamlit files along with EDA analysis result images
│── reports/        # Business health Insights reports 
│── README.md       # Project documentation


---

## 🛠 Tech Stack
- **Languages:** Python, SQL
- **Libraries:** pandas, numpy, matplotlib, seaborn, plotly, sqlalchemy
- **Database:** MySQL
- **Visualization:** Power BI / Streamlit
- **Version Control:** Git & GitHub

---

## 🚀 How to Run the Project

### **1. Clone the Repository**
```bash
git clone https://github.com/SK112713/amazon-india-sales-analytics.git
cd amazon-india-sales-analytics
2. Install Dependencies
pip install -r requirements.txt
3. Run Data Cleaning
python scripts/data_cleaning.py
4. Perform EDA
Open Jupyter Notebook:

jupyter notebook notebooks/eda_analysis.ipynb
5. Load Data into SQL
Open the sql folder and run the load_to_sql.ipynb notebook cells
6. Launch Dashboard
If using Streamlit:

streamlit run dashboard/app.py
If using Power BI:

Open dashboard/amazon_india_dashboard.pbix in Power BI Desktop.
📈 Expected Deliverables
Cleaned dataset (cleaned_amazon_india_2015_2025.csv)
EDA notebook with 20+ visualizations
SQL database schema & queries
Interactive dashboard (Power BI or Streamlit)
Business insights report (PDF)