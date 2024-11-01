import pandas as pd
import matplotlib.pyplot as plt

print('Please input the file path for your first csv.')
data1 = pd.read_csv(input())

print('Please input the file path for your second csv.')
data2 = pd.read_csv(input())

print('Now input the name of your x axis...')
x_axis_name = input()
x_axis_data_1 = data1[x_axis_name]
x_axis_data_2 = data2[x_axis_name]


print('and your y axis...')
y_axis_name = input()
y_axis_data_1 = data1[y_axis_name]
y_axis_data_2 = data2[y_axis_name]

# Create a scatter plot
plt.scatter(x_axis_data_1, y_axis_data_1, color='blue', marker='o')
plt.scatter(x_axis_data_2, y_axis_data_2, color='red', marker='o')

# Add labels and a title
plt.xlabel(x_axis_name)
plt.ylabel(y_axis_name)
plt.title(x_axis_name + ' vs. ' + y_axis_name)

print('creating plot of ' + x_axis_name + ' of length ' + str(len(x_axis_data_1) + len(x_axis_data_2)) + ' vs. ' + y_axis_name + ' of length ' + str(len(y_axis_data_1) + len(y_axis_data_2)))
# Show the plot
plt.grid(True)
plt.show()
