import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def memory_storage_popularity():
    data = {
        "Memory": ["4GB", "4GB", "6GB", "8GB", "8GB", "4GB", "6GB", "8GB", "4GB", "8GB"],
        "Storage": ["64GB", "128GB", "128GB", "256GB", "128GB", "64GB", "256GB", "256GB", "64GB", "256GB"]
    }
    df = pd.DataFrame(data)
    memory_storage_popularity = df.groupby(['Memory', 'Storage']).size().reset_index(name='Count')
    pivot_table = memory_storage_popularity.pivot(index='Memory', columns='Storage', values='Count').fillna(0)

    plt.figure(figsize=(8, 6))
    sns.heatmap(pivot_table, annot=True, fmt='g', cmap='Blues', cbar_kws={'label': 'Popularity'})
    plt.title('Popularity of Memory and Storage Combinations')
    plt.xlabel('Storage Options')
    plt.ylabel('Memory Options')
    st.pyplot(plt)

    avg_memory_storage = df.groupby('Memory')['Storage'].count().reset_index(name='Count')
    st.write("### Average Value per Memory Option:")
    st.dataframe(avg_memory_storage)

    st.write("### Conclusion:")
    st.write("The heatmap shows that '8GB RAM with 256GB storage' is the most popular combination among the sampled data, while '4GB RAM with 256GB storage' is the least popular.")

def sales_volume_by_price_range():
    df = pd.read_csv("df.csv")  # Ensure the file is in the same directory or provide the correct path
    df['Selling Price'] = pd.to_numeric(df['Selling Price'], errors='coerce')

    if df['Selling Price'].isnull().any():
        st.warning("Warning: Missing or invalid 'Selling Price' values found. These will be ignored.")
        df = df.dropna(subset=['Selling Price'])

    bins = [0, 10000, 20000, 30000, 40000, 50000, df['Selling Price'].max() + 1]  # Add 1 to include max value
    labels = ['0-10k', '10k-20k', '20k-30k', '30k-40k', '40k-50k', '50k+']
    df['Price Range'] = pd.cut(df['Selling Price'], bins=bins, labels=labels, include_lowest=True)

    price_range_sales = df.groupby('Price Range').size().reset_index(name='Sales Volume')

    plt.figure(figsize=(10, 6))
    sns.barplot(x='Price Range', y='Sales Volume', data=price_range_sales, palette="coolwarm")
    plt.title('Sales Volume by Price Range', fontsize=16)
    plt.xlabel('Price Range', fontsize=14)
    plt.ylabel('Sales Volume', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)

    avg_price_range = df.groupby('Price Range')['Selling Price'].mean().reset_index(name='Average Selling Price')
    st.write("### Average Selling Price per Price Range:")
    st.dataframe(avg_price_range)

    st.write("### Conclusion:")
    st.write("The bar plot indicates that the sales volume is highest in the '20k-30k' price range, suggesting this is the most popular price range among consumers.")

def average_rating_highest_sales():
    df = pd.read_csv("df.csv")  # Ensure the file is in the same directory or provide the correct path
    df['Selling Price'] = pd.to_numeric(df['Selling Price'], errors='coerce')
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df = df.dropna(subset=['Selling Price', 'Rating'])

    highest_sales_value = df['Selling Price'].max()
    highest_sales_mobiles = df[df['Selling Price'] == highest_sales_value]
    average_rating = highest_sales_mobiles['Rating'].mean()

    plt.figure(figsize=(5, 5))
    plt.bar(['Highest Sales Mobiles'], [average_rating], color='skyblue')
    plt.title('Average Rating of Mobiles with Highest Sales', fontsize=14)
    plt.ylabel('Average Rating', fontsize=12)
    plt.xticks(fontsize=10)
    plt.yticks(fontsize=10)
    plt.ylim(0, 5)  # Assuming ratings are on a scale of 0 to 5
    st.pyplot(plt)
    st.write(f"The average rating of mobiles with the highest sales is: {average_rating:.2f}")

    avg_rating_sales = df.groupby('Selling Price')['Rating'].mean().reset_index(name='Average Rating')
    st.write("### Average Rating by Selling Price:")
    st.dataframe(avg_rating_sales)

    st.write("### Conclusion:")
    st.write("The average rating of the highest selling mobiles is significantly high, indicating that high sales correlate with good customer satisfaction.")

def average_discount_by_brand():
    df = pd.read_csv("df.csv")  # Ensure the file is in the same directory or provide the correct path
    df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')
    #df = df.dropna(subset(['Brands', 'Discount']))

    average_discount = df.groupby('Brands')['Discount'].mean().reset_index()
    average_discount = average_discount.sort_values(by='Discount', ascending=False)
    top_brands = average_discount.iloc[0]['Brands']
    top_discount = average_discount.iloc[0]['Discount']

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Brands', y='Discount', data=average_discount, palette='viridis')
    plt.title(f'Average Discount by Brands (Highest: {top_brands})', fontsize=16)
    plt.xlabel('Brands', fontsize=14)
    plt.ylabel('Average Discount', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    st.pyplot(plt)
    st.write(f"The brands offering the highest average discount is: {top_brands} with an average discount of {top_discount:.2f}.")
    avg_discount_brand = df.groupby('Brands')['Discount'].mean().reset_index(name='Average Discount')
    st.write("### Average Discount by Brands:")
    st.dataframe(avg_discount_brand)
    st.write("### Conclusion:")
    st.write(f"The bar plot illustrates that {top_brands} offers the highest average discount, making it the most discount-friendly brand.")

    

def average_discount_percentage_by_brand():
    df = pd.read_csv("df.csv")  # Ensure the file is in the same directory or provide the correct path
    df['discount percentage'] = pd.to_numeric(df['discount percentage'], errors='coerce')
    #df = df.dropna(subset=['Brands', 'discount percentage'])

    avg_discount_per_brands = df.groupby('Brands')['discount percentage'].mean().reset_index()
    overall_avg_discount = avg_discount_per_brands['discount percentage'].mean()

    plt.figure(figsize=(12, 6))
    sns.barplot(x='Brands', y='discount percentage', data=avg_discount_per_brands, palette='coolwarm')
    plt.title('Average Discount Percentage by Brands', fontsize=16)
    plt.xlabel('Brands', fontsize=14)
    plt.ylabel('Average Discount Percentage (%)', fontsize=14)
    plt.xticks(rotation=45, fontsize=12)
    plt.yticks(fontsize=12)
    plt.axhline(overall_avg_discount, color='red', linestyle='--', label=f'Overall Avg: {overall_avg_discount:.2f}%')
    plt.legend(loc='upper right', fontsize=12)
    st.pyplot(plt)

    st.write("Average Discount Percentage by Brands:")
    st.write(avg_discount_per_brands)
    st.write(f"\nOverall Average Discount Percentage: {overall_avg_discount:.2f}%")

    st.write("### Conclusion:")
    st.write(f"The overall average discount percentage is {overall_avg_discount:.2f}%. The plot shows variations in discount percentages among different brands, highlighting which brands offer higher discounts compared to others.")

def about_author():
    st.write("## About the Author")
    st.write("""
    This dashboard was created by [Hemendra suman], a data analyst with a passion for uncovering insights from data. 
    With a background in data Analysis, [Hemendra suman] specializes in creating interactive visualizations 
    and dashboards to help businesses and individuals make data-driven decisions.
    """)

# Streamlit App
st.title("Data Visualization Dashboard")

menu = ["Memory and Storage Popularity", "Sales Volume by Price Range", "Average Rating of Highest Sales", "Average Discount by Brand", "Average Discount Percentage by Brand", "About the Author"]
choice = st.sidebar.selectbox("Select Analysis", menu)

if choice == "Memory and Storage Popularity":
    memory_storage_popularity()
elif choice == "Sales Volume by Price Range":
    sales_volume_by_price_range()
elif choice == "Average Rating of Highest Sales":
    average_rating_highest_sales()
elif choice == "Average Discount by Brand":
    average_discount_by_brand()
elif choice == "Average Discount Percentage by Brand":
    average_discount_percentage_by_brand()
elif choice == "About the Author":
    about_author()
