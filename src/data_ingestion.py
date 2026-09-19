import pandas as pd
import os

def load_data():

    # 1. Get the exact directory where this script lives (the 'src' folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 2. From 'src', go up one level ('..'), then into 'data'
    data_dir = os.path.join(current_dir, "..", "data")
    
    # 1. Orders
    orders_path = os.path.join(data_dir, "olist_orders_dataset.csv")
    df_orders = pd.read_csv(orders_path)
    
    # 2. Reviews
    reviews_path = os.path.join(data_dir, "olist_order_reviews_dataset.csv")
    df_reviews = pd.read_csv(reviews_path)
    
    # 3. Items (gives us 'price' and 'freight_value')
    items_path = os.path.join(data_dir, "olist_order_items_dataset.csv")
    df_items = pd.read_csv(items_path)
    
    # 4. Products (gives us the Portuguese category names)
    products_path = os.path.join(data_dir, "olist_products_dataset.csv")
    df_products = pd.read_csv(products_path)
    
    # 5. Translations (gives us the English category names)
    translations_path = os.path.join(data_dir, "product_category_name_translation.csv")
    df_translations = pd.read_csv(translations_path)
    
    print("Data loaded successfully!")
    
    return df_orders, df_reviews, df_items, df_products, df_translations

if __name__ == "__main__":
    orders, reviews, items, products, translations = load_data()

    print("\n--- Orders Table Info ---")
    print(orders.info())
    
    print("\n--- First 3 Rows of Items (checking for price) ---")
    print(items.head(3))