# Open the file for reading
file_name = "script1.txt"
data = ""
with open(file_name,"r") as f:
    data = f.read()
print(data)
with open(file_name,"w") as f1:
    for t in data:
        if len(t) > 1:
            print("t: ",t)
            f1.write(t)
