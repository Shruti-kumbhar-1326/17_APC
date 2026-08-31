# Open both files in read mode
file1 = open("file1.txt", "r")
file2 = open("file2.txt", "r")

# Read all lines
lines1 = file1.readlines()
lines2 = file2.readlines()

# Close the files
file1.close()
file2.close()

# Compare the files
if lines1 == lines2:
    print("Both files have identical contents.")
else:
    print("Files are different.")

    # Find the first different line
    min_lines = min(len(lines1), len(lines2))

    found = False

    for i in range(min_lines):
        if lines1[i] != lines2[i]:
            print("First difference found at line:", i + 1)
            print("File 1:", lines1[i].strip())
            print("File 2:", lines2[i].strip())
            found = True
            break

    # If one file has extra lines
    if not found:
        print("First difference found at line:", min_lines + 1)

        if len(lines1) > len(lines2):
            print("File 1 has an extra line:", lines1[min_lines].strip())
        else:
            print("File 2 has an extra line:", lines2[min_lines].strip())