# Given a filename log.txt, use file append mode to add a new log entry each time the function add_log(message) is called. Each message should appear on a new line.

filename = "Phitron-AI-ML/Week01/log.txt"
def add_log(message):
    with open(filename, 'a') as f:
        f.write(message)
        f.write("\n")

add_log("User logged in")
add_log("File uploaded")


