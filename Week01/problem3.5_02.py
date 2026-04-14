# Write a function read_lines(filename) that reads a text file and prints each line with its line number.

def read_lines(filename):
    with open(filename, "r") as f:
        for i, line in enumerate(f, start=1):
            print(f"{i}: {line.strip()}")

read_lines("Phitron-AI-ML/Week01/data.txt")