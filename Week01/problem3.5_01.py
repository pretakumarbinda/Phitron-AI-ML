"""
Problem 1  Create and Write to a File


Write a function create_file(filename, content) that creates a new text file with the given filename and writes the content into it. Call it using positional arguments.
"""
def create_file(filename, content):
    with open(filename,"w") as f:
        f.writelines(content)


        
in1 = input()
in2 = input()

create_file(in1, in2)
