# with open("file.txt" , mode='w') as file:
#     file.write("adding text on file.txt")

with open("file.txt" , mode='r') as file:
    contents = file.read()
    print(contents)