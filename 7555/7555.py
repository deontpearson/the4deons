cipher-text1 = "3b101c091d53320c000910"
cipher-text2 = "071d154502010a04000419"

a = "3c0d094c1f523808000d09"

def xor_strings(xs, ys,i=0):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs[i:], ys))

if __name__ == "__main__":
    crib = "the"
    print xor_strings(a,crib.encode("hex"))
