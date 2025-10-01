import pandas as pd
import numpy as np
import re

# Set options to display the full DataFrame for better inspection
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)

# Define file paths
input_file_path = r'D:\Data Science Projects\amazon_india_project\data\Dataset\amazon_india_2025.csv'
output_file_path = r"D:\Data Science Projects\amazon_india_project\data\Cleaned-dataset\cleaned_amazon_india_2025.csv"

# --- Load the dataset ---
try:
    df = pd.read_csv(input_file_path)
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print(f"Error: File not found at '{input_file_path}'. Please ensure the path is correct.")
    exit() # Exit if the file cannot be loaded

# --- Perform a deep copy to avoid modifying the original DataFrame ---
df_clean = df.copy()
print('Dataset before data cleaning (first 5 rows):')
print(df_clean.head())
print('\nStarting data cleaning process...\n')

# --- Challenge 1: Clean and standardize 'order_date' column ---
# Convert to datetime, handling multiple formats and invalid entries by coercing to NaT
print("Cleaning 'order_date' column...")
df_clean['order_date'] = pd.to_datetime(df_clean['order_date'], dayfirst=True, errors='coerce')
print("Successfully cleaned 'order_date'.\n")

# --- Challenge 2: Clean and standardize 'original_price_inr' column ---
# Remove currency symbols and comma separators, then convert to numeric
print("Cleaning 'original_price_inr' column...")
df_clean['original_price_inr'] = df_clean['original_price_inr'].replace('[₹,]', '', regex=True)
df_clean['original_price_inr'] = pd.to_numeric(df_clean['original_price_inr'], errors='coerce')
print("Successfully cleaned 'original_price_inr'.\n")

# --- Challenge 3: Standardize 'customer_rating' column ---
# Convert various rating formats to a consistent numeric scale (1.0-5.0)
print("Cleaning 'customer_rating' column...")
def clean_rating(val):
    if pd.isna(val):
        return np.nan # Use np.nan for missing numeric values
    val = str(val).lower()
    # Extract numeric part, handling formats like '4 stars', '3/5', '2.5/5.0'
    if '/' in val:
        try:
            parts = val.split('/')
            return float(parts[0]) / float(parts[1]) * 5.0 # Convert x/y to a 5.0 scale
        except ValueError:
            return np.nan
    val = re.sub(r'[^0-9\.]', '', val) # Remove non-numeric characters except for the decimal point
    try:
        return float(val)
    except ValueError:
        return np.nan

df_clean['customer_rating'] = df_clean['customer_rating'].apply(clean_rating)
# Ensure ratings are within 1.0-5.0 range after conversion if necessary (optional, but good for robustness)
df_clean['customer_rating'] = df_clean['customer_rating'].clip(1.0, 5.0)
print("Successfully standardized 'customer_rating'.\n")

# --- Challenge 4: Standardize 'customer_city' names ---
print("Standardizing 'customer_city' names...")
city_map = {
    'bangalore': 'Bengaluru', 'bengaluru': 'Bengaluru',
    'mumbai': 'Mumbai', 'bombay': 'Mumbai',
    'delhi': 'Delhi', 'new delhi': 'Delhi'
}
df_clean['customer_city'] = df_clean['customer_city'].astype(str).str.lower().replace(city_map)
df_clean['customer_city'] = df_clean['customer_city'].str.title() # Capitalize first letter of each word
print("Successfully standardized 'customer_city' names.\n")

# --- Challenge 5: Convert boolean columns to consistent True/False format ---
print("Converting boolean columns to consistent True/False format...")
bool_map = {
    'yes': True, 'y': True, '1': True, 'true': True,
    'no': False, 'n': False, '0': False, 'false': False
}
for col in ['is_prime_member', 'is_prime_eligible', 'is_festival_sale']:
    df_clean[col] = df_clean[col].astype(str).str.lower().map(bool_map)
print("Successfully converted boolean columns.\n")

# --- Challenge 6: Standardize 'category' names ---
print("Standardizing 'category' names...")
category_map = {
    'electronics': 'Electronics',
    'electronic': 'Electronics',
    'electronics & accessories': 'Electronics',
    'electronicss':'Electronics'
}
df_clean['category'] = df_clean['category'].astype(str).str.lower().str.strip().replace(category_map)
df_clean['category'] = df_clean['category'].apply(lambda x: x.title() if isinstance(x, str) else x) # Capitalize for consistency
print("Successfully standardized 'category' names.\n")

# --- Challenge 7: Clean 'delivery_days' column ---
print("Cleaning 'delivery_days' column...")
df_clean['delivery_days'] = df_clean['delivery_days'].replace({'Same Day': '0', '1-2 days': '1.5'}) # Convert text to numeric-friendly strings
df_clean['delivery_days'] = pd.to_numeric(df_clean['delivery_days'], errors='coerce')
# Handle unrealistic values: negative values set to NaN, values > 30 (arbitrary high limit) set to NaN
df_clean.loc[df_clean['delivery_days'] < 0, 'delivery_days'] = np.nan
df_clean.loc[df_clean['delivery_days'] > 30, 'delivery_days'] = np.nan
print("Successfully cleaned 'delivery_days'.\n")

# --- Challenge 8: Handle Duplicate Transactions ---
# Drop duplicates based on a subset of key columns, keeping the first occurrence
print("Handling duplicate transactions...")
df_clean = df_clean.drop_duplicates(subset=['customer_id', 'product_id', 'order_date', 'final_amount_inr'], keep='first')
print("Successfully handled duplicate transactions.\n")

# --- Challenge 9: Fix Price Outliers in 'original_price_inr' ---
# Cap outliers using the IQR method (1.5 * IQR rule)
print("Fixing price outliers in 'original_price_inr'...")
Q1 = df_clean['original_price_inr'].quantile(0.25)
Q3 = df_clean['original_price_inr'].quantile(0.75)
IQR = Q3 - Q1
upper_limit = Q3 + 1.5 * IQR
# Cap values above the upper limit, keeping lower outliers as they might be genuine discounts
df_clean.loc[df_clean['original_price_inr'] > upper_limit, 'original_price_inr'] = upper_limit
print("Successfully fixed price outliers.\n")

# --- Challenge 10: Standardize Payment Methods ---
print("Standardizing 'payment_method' categories...")
payment_map = {
    'upi': 'UPI', 'phonepe': 'UPI', 'googlepay': 'UPI',
    'credit card': 'Credit Card', 'credit_card': 'Credit Card', 'cc': 'Credit Card',
    'cash on delivery': 'Cash on Delivery', 'cod': 'Cash on Delivery', 'c.o.d': 'Cash on Delivery'
}
df_clean['payment_method'] = df_clean['payment_method'].astype(str).str.lower().replace(payment_map)
df_clean['payment_method'] = df_clean['payment_method'].apply(lambda x: x.title() if isinstance(x, str) else x) # Capitalize for consistency
print("Successfully standardized 'payment_method'.\n")

# --- Display cleaned data head and info ---
print('\nData cleaning complete. Cleaned dataset head:')
print(df_clean.head())
print('\nCleaned dataset info:')
df_clean.info()

# --- Save Cleaned Data ---
try:
    df_clean.to_csv(output_file_path, index=False)
    print(f"\nCleaned data saved successfully to '{output_file_path}'.")
except Exception as e:
    print(f"\nError saving cleaned data: {e}")
