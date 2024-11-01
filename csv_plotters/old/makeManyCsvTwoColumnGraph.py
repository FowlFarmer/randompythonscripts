import pandas as pd
import matplotlib.pyplot as plt

colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'yellow', 'aqua', 'indigo', 'peru', 'maroon']


print('Input the name of your x axis...')
x_axis_name = input()

print('and your y axis...')
y_axis_name = input()

print('How many files?')
length = int(input())
for i in range(length):
    print('Please input the file path for your ' + str(i) + 'th csv.')
    while True:
        try:
            data = pd.read_csv(input())
            print("CSV file loaded successfully!")
            break

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Filepath not found. Please try again.")

        except Exception as e:
            # Catch any other unexpected errors
            print(f"An error occurred: {e}. Please try again.")

    x_filtered = data[x_axis_name]
    y_filtered = data[y_axis_name]
    plt.scatter(x_filtered, y_filtered, color = (colors[i] if (length <= 11) else 'black'), marker='o')


# Add labels and a title
plt.xlabel(x_axis_name)
plt.ylabel(y_axis_name)
plt.title(x_axis_name + ' vs. ' + y_axis_name)

print('creating plot')
# Show the plot
plt.grid(True)
plt.show()
