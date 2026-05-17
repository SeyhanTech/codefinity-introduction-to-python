# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for revenues in range(len(quantities_sold)):
        total = quantities_sold[revenues] * prices[revenues]
        revenue.append(total)
    return revenue
    
def formatted_output(revenues):
    for product, rev in sorted(revenues):
        print(f"{product} has total revenue of ${rev}") 
revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)
# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")
# Example of expected output line (do not remove):
print(f"{revenue[0]} has total revenue of ${revenue[1]}")
