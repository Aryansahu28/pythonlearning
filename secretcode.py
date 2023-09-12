# Code
# if word is greater than 3 than append the first letter to end
# Then add three letters in beginning and ending
# if word is less than three than just reverse it
# Decode
# if word is less than 3 then just reverse it
# if word is more than 3 then remove the starting and ending 3 letters and then just add the last letter in the beginning

try:
    inp = input("Enter whether you want to code or decode: ")
except:
    print("I think you mistakenly enter the wrong word")

if (inp == "code"):
    secret_code_conversion = input("Enter your code: ")
    if (len(secret_code_conversion) > 3):
        code1 = 'Wer'+secret_code_conversion[1:] + secret_code_conversion[0]+'egd'
        print(code1)
    else:
        print(
            secret_code_conversion[2]+secret_code_conversion[1]+secret_code_conversion[0])

elif (inp == "decode"):
    decoder = input("Enter the code you want to decode: ")
    if (len(decoder) <= 3):
        print(decoder[2]+decoder[1]+decoder[0])

    else:
        code2 = decoder[3:-3]
        code3 = code2[-1]+code2[:((len(code2)-1))]
        print(code3,"\n")
        

