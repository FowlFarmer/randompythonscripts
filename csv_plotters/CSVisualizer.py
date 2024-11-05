import pandas as pd
import matplotlib.pyplot as plt
import time
import math



def processCommand(command):
    while True:
        print('enter a command...')
        cmd_list = input().split(" ")
        # if cmd_list[0] == "drawline":
        #     if(length(cmd_list) != 3):
        #         print("error incorrect args (drawline x)") needa fix this for x1y1
        #     else:
        #         cmd_list.pop(0)
        #         plt.plot([int(i) for i in cmd_list])
        #     return
        print(cmd_list)
        if cmd_list[0] == "end":
            break
        if cmd_list[0] == "logline":
            if(len(cmd_list) != 5):
                print("error incorrect args for base 10 logline (logline m res x1 y0)")
            else:
                m = float(cmd_list[1])
                resolution = int(cmd_list[2])
                endpt = float(cmd_list[3])
                y0 = float(cmd_list[4])
                plotx = []
                ploty = []

                for i in range(resolution):
                    x = i*(endpt/resolution)
                    y = 10**(m*x + y0)
                    plotx.append(x)
                    ploty.append(y)
                plt.plot(plotx, ploty)
            break
        if cmd_list[0] == "logscatter":
            if(len(cmd_list) != 5):
                print("error incorrect args for base 10 logline (logscatter m res x1 y0)")
            else:
                m = float(cmd_list[1])
                resolution = int(cmd_list[2])
                endpt = float(cmd_list[3])
                y0 = float(cmd_list[4])
                plotx = []
                ploty = []

                for i in range(resolution):
                    x = i*(endpt/resolution)
                    y = 10**(m*x + y0)
                    plotx.append(x)
                    ploty.append(y)
                plt.scatter(plotx, ploty, color = 'black', marker = 'o')


print('Input the name of your x axis...')
x_axis_name = input()

print('and your y axis...')
y_axis_name = input()

print('How many files?')
length = int(input())

use_custom_color = False

print('do you want to have custom colors?')
if(input() == 'yes'):
    colors = []
    use_custom_color = True
    for i in range(length):
        print('give color for ' + str(i))
        colors.append(input())

else:
    colors = ['red', 'blue', 'green', 'orange', 'purple', 'black', 'yellow', 'aqua', 'indigo', 'peru', 'maroon']

for i in range(length):
    print('Please input the file path for your ' + str(i) + 'th csv.')
    while True:
        try:
            data = pd.read_csv(input())
            print("CSV file loaded successfully! press any to continue...")
            break

        except FileNotFoundError:
            # Handle the case where the file is not found
            print("Filepath not found. Please try again.")
            continue
        except EOFError:
            print("EOF")
            break
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An error occurred: {e}. Please try again.")

    x_filtered = data[x_axis_name]
    y_filtered = data[y_axis_name]
    plt.scatter(x_filtered, y_filtered, color = (colors[i] if (use_custom_color or length <= 11) else 'black'), marker='o')
processCommand(input())

# Add labels and a title
plt.xlabel(x_axis_name)
plt.ylabel(y_axis_name)
plt.title(x_axis_name + ' vs. ' + y_axis_name)

print('creating plot')
# Show the plot
plt.grid(True)
plt.show()




