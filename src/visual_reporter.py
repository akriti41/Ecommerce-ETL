import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_report_folder():
    """Ensures the output directory exists before saving graphs."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    report_dir = os.path.join(current_dir, "..", "reports")
    os.makedirs(report_dir, exist_ok=True)
    return report_dir

def plot_revenue_trend(revenue_df):
    report_dir = create_report_folder()
    
    # Set a professional visual theme
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(10, 6))
    
    # Create the line chart
    sns.lineplot(
        data=revenue_df, 
        x='month_year', 
        y='total_order_value', 
        marker='o', 
        linewidth=2.5, 
        color='#2980b9'
    )
    
    plt.title('Monthly Revenue Growth', fontsize=16, pad=15)
    plt.xlabel('Month', fontsize=12)
    plt.ylabel('Total Revenue (BRL)', fontsize=12)
    plt.xticks(rotation=45)
    
    # Save the graph
    save_path = os.path.join(report_dir, "1_revenue_trend.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"Saved graph: {save_path}")
    
    # Show the graph on screen
    plt.show() 
    
    # Close the canvas
    plt.close()

def plot_top_categories(category_df):
    report_dir = create_report_folder()
    
    plt.figure(figsize=(12, 7))
    
    # Horizontal bar chart for readability
    sns.barplot(
        data=category_df, 
        x='price', 
        y='product_category_name_english', 
        hue='product_category_name_english',
        palette='mako',
        legend=False
    )
    
    plt.title('Top 10 Product Categories by Revenue', fontsize=16, pad=15)
    plt.xlabel('Total Revenue (BRL)', fontsize=12)
    plt.ylabel('')
    
    save_path = os.path.join(report_dir, "2_top_categories.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"Saved graph: {save_path}")
    
    # Show the graph on screen
    plt.show()
    
    # Close the canvas
    plt.close()

def plot_delivery_impact(delivery_df):
    report_dir = create_report_folder()
    
    plt.figure(figsize=(8, 5))
    
    # Red for delayed, green for on-time
    sns.barplot(
        data=delivery_df, 
        x='Delivery Status', 
        y='review_score', 
        hue='Delivery Status',
        palette={'On Time / Early': '#27ae60', 'Delayed': '#c0392b'},
        legend=False
    )
    
    plt.title('Impact of Logistics on Customer Satisfaction', fontsize=16, pad=15)
    plt.ylim(1, 5) # Lock y-axis to the 1-5 star scale
    plt.ylabel('Average Review Score', fontsize=12)
    plt.xlabel('')
    
    save_path = os.path.join(report_dir, "3_delivery_impact.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"Saved graph: {save_path}")
    
    # Show the graph on screen
    plt.show()
    
    # Close the canvas
    plt.close()

def plot_freight_analysis(freight_df):
    """Generates a bar chart comparing freight costs to product prices."""
    report_dir = create_report_folder()
    
    plt.figure(figsize=(9, 6))
    
    # Create the bar chart using Seaborn with clean custom colors
    sns.barplot(
        data=freight_df,
        x='Freight Category',
        y='Order Count',
        palette=['#3498db', '#e74c3c', '#2ecc71'],
        hue='Freight Category',
        legend=False
    )
    
    plt.title('Freight vs. Product Price Distribution', fontsize=16, pad=15)
    plt.xlabel('Shipping Cost Category', fontsize=12)
    plt.ylabel('Number of Orders', fontsize=12)
    plt.xticks(rotation=15)
    
    save_path = os.path.join(report_dir, "4_freight_analysis.png")
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    print(f"Saved graph: {save_path}")
    
    # Show the graph on screen
    plt.show()
    
    # Close the canvas
    plt.close()