import matplotlib.pyplot as plt

# Example data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [200, 250, 300, 350, 400]

# Create a line plot
plt.plot(months, sales, marker='o')
plt.title('Sales Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
