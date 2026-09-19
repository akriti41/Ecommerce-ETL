import data_ingestion
import data_transformation
import business_questions
import visual_reporter

if __name__ == "__main__":
    print("--- 1. Starting Data Ingestion ---")
    orders, reviews, items, products, translations = data_ingestion.load_data()
    
    print("--- 2. Transforming and Merging Data ---")
    master_df = data_transformation.merge_data(orders, reviews, items, products, translations)
    
    print("--- 3. Analyzing Business Questions ---")
    revenue_df = business_questions.calculate_monthly_revenue(master_df)
    category_df = business_questions.calculate_top_categories(master_df)
    delivery_df = business_questions.analyze_delivery_impact(master_df)
    freight_df = business_questions.analyze_freight_cost(master_df)
    
    print("--- 4. Generating Visual Reports ---")
    visual_reporter.plot_revenue_trend(revenue_df)
    visual_reporter.plot_top_categories(category_df)
    visual_reporter.plot_delivery_impact(delivery_df)
    visual_reporter.plot_freight_analysis(freight_df)
    
    print("--- Pipeline Execution Complete! ---")