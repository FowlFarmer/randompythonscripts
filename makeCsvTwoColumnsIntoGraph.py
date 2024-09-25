import pandas as pd
import matplotlib.pyplot as plt

print('Please input the file path for your csv.')
path = input()
data = pd.read_csv(path)

print('Now input the name of your x axis...')
x_axis_name = input()
x_axis_data = data[x_axis_name]

print('and your y axis...')
y_axis_name = input()
y_axis_data = data[y_axis_name]

# Create a scatter plot
plt.scatter(x_axis_data, y_axis_data, color='blue', marker='o')

# Add labels and a title
plt.xlabel(x_axis_name)
plt.ylabel(y_axis_name)
plt.title(x_axis_name + ' vs. ' + y_axis_name)

print('creating plot of ' + x_axis_name + ' of length ' + str(len(x_axis_data)) + ' vs. ' + y_axis_name + ' of length ' + str(len(x_axis_data)))
# Show the plot
plt.grid(True)
plt.show()
