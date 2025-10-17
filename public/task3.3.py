q = input("you want to decrypt or encrypt: ")

def encrypt():

    raw_input = input('Write Text: ')
    raw_input = raw_input.lower()

    brut_key = input('tell me secret key word: ')
    brut_key = brut_key.lower()
 
    output = []

    for c in raw_input:
        numb = ord(c) - 96
        output.append(numb)

    key_out = []

    for a in brut_key:
        num = ord(a) - 96
        key_out.append(num)

    lst = []

    output_len = len(output)

    k = 0

    for i in output:
        
        if k > len(key_out) - 1:
           k = 0
        key = key_out[k]
    

        if i == -64:
            lst.append(i)
            k += 1
        else:

            if i + key > 26:
                diff = (i + key) - 26
                lst.append(diff)
                k += 1
            else:
                lst.append(i + key)
                k += 1

    x = []

    for i in lst:
        x.append(chr(ord('`')+ i))

    final = ''.join(x)
    print(final)


def decrypt():
    
    raw_input = input("what's the message? ")
    raw_input = raw_input.lower()

    brut_key = input("gimmy tha key: ")
    brut_key = brut_key.lower()

    k = 0

    output = []

    key_out = []

    lst = []

    for c in raw_input:
        numb = ord(c) - 96
        output.append(numb)

    for c in brut_key:
        numb = ord(c) - 96
        key_out.append(numb)

    key_len = len(key_out)

    for i in output:
    
        if k > key_len - 1:
            k = 0
        
        key = key_out[k]

        if i == -64:
            lst.append(i)
            k += 1
        else:
            if i - key < 1:
                diff = 1 - (i - key)
                lst.append(26 - diff + 1)
                k += 1
            else:
                lst.append(i - key)
                k += 1




    x = []


    for i in lst:
        x.append(chr(ord('`') + i))

    final = ''.join(x)

    print(final)

if q == "encrypt":
    encrypt()
elif q == "decrypt":
    decrypt()
else:
    print("i didn't understand what you want")
    q = input("you want to encrypt or decrypt")
