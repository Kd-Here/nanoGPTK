import wget

url = "https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt"
filename = wget.download(url)
print(f"File downloaded: {filename}")
