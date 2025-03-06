with open('input.txt','r') as file:
    text = file.read()



unique_char = set(text)

sorted_list_unique_char = sorted(list(unique_char))


# Tokenization started from here:-

def encode(sorted_list_unique_char):
  encode_dict = {}
  k = 0
  for i in sorted_list_unique_char:
    encode_dict[i] = k=k+1
  return (encode_dict)


def decode(sorted_list_unique_char):
  decode_dic ={}
  for i in  range(len(sorted_list_unique_char)):
    decode_dic[i+1] = sorted_list_unique_char[i]
  return(decode_dic)
  
encode_dict = encode(sorted_list_unique_char)
decode_dic = decode(sorted_list_unique_char)

input_str = """First Citizen:
Before we proceed any further, hear me speak.

All:
Speak, speak.

First Citizen:
You are all resolved rather to die than to famish?

All:
Resolved. resolved.

First Citizen:
First, you know Caius Marcius is chief enemy to the people.

All:
We know't, we know't.

First Citizen:
Let us kill him, and we'll have corn at our own price.
Is't a verdict?

All:
No more talking on't; let it be done: away, away!

Second Citizen:
One word, good citizens.

First Citizen:
We are accounted poor citizens, the patricians good.
What authority surfeits on would relieve us: if they
would yield us but the superfluity, while it were
wholesome, we might guess they relieved us humanely;
but they think we are too dear: the leanness that
afflicts us, the object of our misery, is as an
inventory to particularise their abundance; our
sufferance is a gain to them Let us revenge this with
our pikes, ere we become rakes: for the gods know I
speak this in hunger for bread, not in thirst for revenge.


"""
print(input_str)


encoded_str = ','.join(str(encode_dict[i]) for i in input_str)
print(encoded_str)


decoded_str = ''.join(str(decode_dic[int(j)]) for j in encoded_str.split(','))
print(decoded_str)

