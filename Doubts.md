# When I use wget in Google Colab, like I did to download a file, who exactly is sending the HTTP request? Is it my Python code that's making the request, or is there something else involved in this process? Also, when the server responds with '200 OK', what’s actually happening behind the scenes during this exchange? I’m a beginner to networking and would love to understand how HTTP requests work in this context."



with open('input.txt','r') as file:
    print(len(file.readlines()))
    text = file.read()

print(len(text))

VS

with open('input.txt','r') as file:
    text = file.read()
    print(len(file.readlines()))

print(len(text))


# The read() method moves the file pointer to the end of the file. After calling read() or readlines(), if you try to read again, the file pointer is at the end, so subsequent reads will return nothing.



