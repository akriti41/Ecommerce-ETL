import pandas as pd

def merge_data(orders, reviews, items, products, translations):
    """
    Merges all 5 datasets together into one master table.
    """
    print("Merging datasets step-by-step...")
    
    # Step 1: Merge orders with reviews (using order_id)
    df = pd.merge(left=orders, right=reviews, on="order_id", how="left")
    
    # Step 2: Merge the result with items (using order_id)
    df = pd.merge(left=df, right=items, on="order_id", how="left")
    
    # Step 3: Merge with products (using product_id)
    df = pd.merge(left=df, right=products, on="product_id", how="left")
    
    # Step 4: Merge with translations to get English names (using product_category_name)
    df = pd.merge(left=df, right=translations, on="product_category_name", how="left")
    
    print(f"Merge successful! The master dataset has {df.shape[0]} rows and {df.shape[1]} columns.")
    return df

# The testing block
if __name__ == "__main__":
    from data_ingestion import load_data
    
    # 1. Load all 5 files
    orders, reviews, items, products, translations = load_data()
    
    # 2. Merge them all together
    master_df = merge_data(orders, reviews, items, products, translations)
    
    # 3. Print out columns to verify it worked
    print("\nColumns in our new master dataframe:")
    print(master_df.columns.tolist())