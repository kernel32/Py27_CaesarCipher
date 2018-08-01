import re
import string

def caesarCipher(textInput, shifts):
    alphaDefinition = list(string.ascii_lowercase)
    alphaInput = list(textInput)
    
    s = ""
    for i in textInput:
        comboIndex = alphaInput.index(i)
        cipherText = alphaDefinition [comboIndex + shifts]
        s += cipherText
    print(s)
    return;
    
def decodeCipher(textInput, shifts):
    alphaDefinition = list(string.ascii_lowercase)
    alphaInput = list(textInput)
    
    o = ""
    for i in textInput:
        comboIndex = alphaInput.index(i)
        cipherText = alphaDefinition [(comboIndex + shifts) - shifts]
        o += cipherText
    print(o)
    return;

params = input("\nDo you want to encode(e) or decode(d) [Enter characters e or d]?: ")

if params == "e":
    textInput = input("\nEnter desired plaintext which you want to encode: ")
    shifts = int(input("\nEnter desired number of shifts for the encoding operation: "))

    regex = re.compile('[^a-zA-Z]')
    regex.sub('', textInput)
    
    if shifts <= 0 or shifts % 26 == 0:
        print("Invalid operation, index needs to be bigger than zero.")
    
    elif shifts > 26:
        shifts = shifts % 26
        print(caesarCipher(textInput, shifts))
        
    else:
        print(caesarCipher(textInput, shifts))
    
elif params == "d":
    textInput = input("\nEnter desired ciphertext which you want to decode:")
    shifts = int(input("\nEnter desired number of shifts for the decoding operation: "))

    regex = re.compile('[^a-zA-Z]')
    regex.sub('', textInput)
    
    if shifts <= 0 or shifts % 26 == 0:
        print("Invalid operation, index needs to be bigger than zero.")
    
    elif shifts > 26:
        shifts = shifts % 26
        print(decodeCipher(textInput, shifts))
        
    else:
        print(decodeCipher(textInput, shifts))
    
else:
    print("No valid arguments given")