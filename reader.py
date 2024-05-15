# Import of built-in packages
import sys
import csv
import os

# Check for provided arguments and changes
if len(sys.argv) < 7:
    print("Usage of the app:")
    print("Please type in the command in the following format with all arguments provided:")
    if (os.name) == "nt":
        print("py reader.py src_file dst_file change1 change2 change3 change4")
    else:
        print("python3 reader.py src_file dst_file change1 change2 change3 change4")
    sys.exit(1)

src_file = sys.argv[1]
dst_file = sys.argv[2]
change1 = sys.argv[3]
change2 = sys.argv[4]
change3 = sys.argv[5]
change4 = sys.argv[6]

# Reading the source file
try:
    with open(src_file, "r") as file:
        reader = list(csv.reader(file))
        print("\n'IN.CSV' file:\n")
        # iteration through data in source file
        for old_content in reader:
            print(",".join(old_content))
except FileNotFoundError:
    print(f"\nFile not found: {src_file}")
    sys.exit(1)

# Splitting the data from source file
try:
    col1, row1, value1 = [int(x) if i < 2 else x.strip() for i, x in enumerate(change1.split(","))]
    col2, row2, value2 = [int(x) if i < 2 else x.strip() for i, x in enumerate(change2.split(","))]
    col3, row3, value3 = [int(x) if i < 2 else x.strip() for i, x in enumerate(change3.split(","))]
    col4, row4, value4 = [int(x) if i < 2 else x.strip() for i, x in enumerate(change4.split(","))]

    reader[row1][col1] = value1
    reader[row2][col2] = value2
    reader[row3][col3] = value3
    reader[row4][col4] = value4
except (ValueError, IndexError):
    print("\nError with changes! Please try again.")
    sys.exit(1)

# Saving destiantion file
try:
    with open(dst_file, "w", newline="") as file2:
        writer = csv.writer(file2)
        writer.writerows(reader)
except:
    print(f"\nError writing in file: {dst_file}")

# printing destiantion file to terminal
print("\n'OUT.CSV' file:\n")
for new_content in reader:
    print(",".join(new_content))