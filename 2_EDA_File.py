with open('input.txt','r') as file:
    
    print("lines in dataset: ",len(file.readlines()))

    file.seek(0)  # Reset the file pointer to the beginning of the file
    text = file.read()

print("length of dataset in characters: ",len(text))
print(text[:1000])