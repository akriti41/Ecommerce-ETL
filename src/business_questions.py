import pandas as pd

def calculate_monthly_revenue(df):
    """Calculates total revenue (price + freight) per month."""
    print("\nCalculating monthly revenue...")
    
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])
    df['month_year'] = df['order_purchase_timestamp'].dt.strftime('%Y-%m')
    df['total_order_value'] = df['price'] + df['freight_value']
    
    monthly_data = df.groupby('month_year')['total_order_value'].sum().reset_index()
    
    # Sort chronologically
    monthly_data = monthly_data.sort_values(by='month_year')
    return monthly_data

def calculate_top_categories(df):
    """Identifies the top 10 product categories by total revenue."""
    print("\nCalculating top 10 categories by revenue...")
    
    category_sales = df.groupby('product_category_name_english')['price'].sum().reset_index()
    top_10 = category_sales.sort_values(by='price', ascending=False).head(10)
    
    return top_10

def analyze_delivery_impact(df):
    """Compares review scores between on-time and delayed deliveries."""
    print("\nAnalyzing delivery impact on review scores...")
    
    df['order_delivered_customer_date'] = pd.to_datetime(df['order_delivered_customer_date'])
    df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
    
    df['is_delayed'] = df['order_delivered_customer_date'] > df['order_estimated_delivery_date']
    
    delay_summary = df.groupby('is_delayed')['review_score'].mean().reset_index()
    
    # Map True/False to readable labels
    delay_summary['Delivery Status'] = delay_summary['is_delayed'].map({
        False: 'On Time / Early', 
        True: 'Delayed'
    })
    
    return delay_summary[['Delivery Status', 'review_score']]

def analyze_freight_cost(df):
    """Categorizes orders based on how the shipping cost compares to the product price."""
    print("\nAnalyzing freight cost vs. product price...")
    
    # Create a clean slice of the data to avoid SettingWithCopy warnings
    df_freight = df[['freight_value', 'price']].dropna().copy()
    
    # Set default category, then apply conditional logic
    df_freight['Freight_Category'] = 'Freight <= Product Price' 
    df_freight.loc[df_freight['freight_value'] == 0, 'Freight_Category'] = 'Free Shipping'
    df_freight.loc[df_freight['freight_value'] > df_freight['price'], 'Freight_Category'] = 'Freight > Product Price'
    
    # Group and count
    freight_summary = df_freight['Freight_Category'].value_counts().reset_index()
    freight_summary.columns = ['Freight Category', 'Order Count']
    
    return freight_summary

if __name__ == "__main__":
    # Import our pipeline functions
    from data_ingestion import load_data
    from data_transformation import merge_data
    
    print("=== STARTING OLIST ANALYTICS PIPELINE ===")
    
    orders, reviews, items, products, translations = load_data()
    
    master_df = merge_data(orders, reviews, items, products, translations)
    
    # Answer Business Questions
    revenue_df = calculate_monthly_revenue(master_df)
    print("\n--- Monthly Revenue (First 5 Months) ---")
    print(revenue_df.head(5))
    
    top_categories_df = calculate_top_categories(master_df)
    print("\n--- Top 10 Product Categories ---")
    print(top_categories_df)
    
    delivery_df = analyze_delivery_impact(master_df)
    print("\n--- Impact of Delays on Review Scores ---")
    print(delivery_df)
    
    freight_df = analyze_freight_cost(master_df)
    print("\n--- Freight vs. Product Price ---")
    print(freight_df)