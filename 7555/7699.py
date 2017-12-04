#Use this tool to solve multi-time pads
#Written on 4th march 2016
#Took me a good 30 minutes
#How this tool works:
#Suppose you guess a crib " the "
#We have n messages each of length k
#For each of the n messages and at each position k we want to guess the crib
#However, we can make our lives vastly easier if we guess the other way round:
#Instead of guessing each message separately, we guess at the same position for all the messages at the same time
#This will make it easier to spot when crib for message m at position k produces the wrong output for any other message
#Therefore, what this program does is to guess for each combination of message and position the crib for all messages at position k
#Suppose at message m position k the plaintext is " the ", then we can derive the key at position k with the length of our crib
#Once we have derived that part of the key we then apply it to the rest of the messages to see if we get a sensible output
#Therefore for any crib there are n * k outputs where n is the number of ciphertexts and k is the length of each ciphertext
#Each output is n strings of characters representing the "decoded" portion of each message at position k

#Todo: Use a dictionary to automate this.



from itertools import combinations

a="4de61dd9dab5e0701f5e664ff522de12bd588051da4d3f62df"
b="3c3303e696139af0280308f5720d5e45efaa03bc6d37d84294"
c="06b25cded0e2fb74045f681bd4378a5bba10901fd6513b2cc0"
d="343c0aa3c6138df02d1f46e63a090d07f3b602bc653bcd5ad1"
e="00fa5890c4f0e062175d2348bd30c25dbb44c951c0503f6fd8"
f="3d3114b28e1390b4611146e53a091c45f8bc01f56f2ac1459f"

crib = " message ".encode("hex")
#data = [line.strip() for line in open("20k.txt", 'r')]

binary_a = a.decode("hex")
binary_b = b.decode("hex")
binary_c = c.decode("hex")
binary_d = d.decode("hex")
binary_e = e.decode("hex")
binary_f = f.decode("hex")
L1=[binary_a,binary_b,binary_c,binary_d,binary_e,binary_f]

def xor_strings(xs, ys,i=0):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs[i:], ys))

def initial_drag(crib):
    '''for combo in combinations(L1, 2):
        xored= xor_strings(combo[0], combo[1]).encode("hex")
        print combo[0].encode("hex"), combo[1].encode("hex")
        print xored
        for i in range(27):
            print xor_strings(xored.decode("hex"),the2.decode("hex"),i)'''
    for cipher in L1:
        for position in range(len(cipher)-len(crib)):
            key = xor_strings(cipher,crib.decode("hex"),position).encode("hex") #when we XOR our crib with the ciphertext, we should get back the key
            for c in L1:
                print xor_strings(c,key.decode("hex"),position), cipher.encode("hex"),position #we then XOR the key we got back with the other ciphertexts
            print ""

def crib_drag(crib,ciphertext,position):
    key = xor_strings(ciphertext,crib.decode("hex"),position).encode("hex")
    for c in L1:
        print xor_strings(c,key.decode("hex"),position), c.encode("hex"),position #we then XOR the key we got back with the other ciphertexts

# Step 1. Do an initial crib drag through all possible key fragments for your crib.
initial_drag(crib)

# Step 2. Once you have found a valid key fragment, expand on that fragment. I did this manually in the interpreter.
