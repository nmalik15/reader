import sys
import csv

if len(sys.argv) < 3:
    print("Usage of the app:")
    print("Please type in the command in the following format with all arguments provided:")
    print("py reader.py src_file dst_file change1 change2 change3 change4")
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
        print("\nOriginal CSV content:\n")
        # iteration through data in source file
        for old_content in reader:
            print(",".join(old_content))
except FileNotFoundError:
    print(f"\nFile not found: {src_file}")
    sys.exit(1)
