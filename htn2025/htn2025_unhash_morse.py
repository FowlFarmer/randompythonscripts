# remove_hashes.py

input_file = input()     # Change to your file name
output_file = input()   # File to save the cleaned text

with open(input_file, 'r') as f:
    lines = f.readlines()

# Remove all '#' symbols
cleaned_lines = [line.replace('#', '') for line in lines]

with open(output_file, 'w') as f:
    f.writelines(cleaned_lines)

print(f"Hashes removed. Output saved to '{output_file}'")
