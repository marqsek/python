import os

directory = r'c:\results'

if not os.path.exists(directory):
    os.makedirs(directory)

file_path = os.path.join(directory, 'wynik.txt')

with open(file_path, 'w') as f:
    print("This if first line", file=f)
    print("This if second line", file=f)
    print("This if third line", file=f)

print(f"results have been saved to: {file_path}")