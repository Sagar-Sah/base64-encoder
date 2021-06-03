def myfunc():
    z = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "/"]
    global final_result
    final_result = z[decimal]
def mainfunc():
    calc = len((temp_res)) / 6
    output =""
    while calc != 0:
        global a , b , decimal
        temp_res1 = temp_res[a:b]
        a +=  6
        b +=  6
        calc = calc - 1
        decimal = int(temp_res1, 2)
        myfunc()
        output += final_result
    if len(output)%4==0:
        print("Result : " + output)
    else:
        output +="="
        if len(output)%4==0:
            print("Result : " +output)
        else:
            output +="="
            print("Result : " + output)


a = 0
b = 6
print("""\

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▀█░▄▄▀█░▄▄█░▄▄█▀▄▄▀██░▄░█████░▄▄▄█░▄▄▀█▀▄▀█▀▄▄▀█░▄▀█░▄▄█░▄▄▀
██░▄▄▀█░▀▀░█▄▄▀█░▄▄█░▀▀██░▀▀░▀████░▄▄▄█░██░█░█▀█░██░█░█░█░▄▄█░▀▀▄
██░▀▀░█▄██▄█▄▄▄█▄▄▄█▄▀▀▄████░█████░▀▀▀█▄██▄██▄███▄▄██▄▄██▄▄▄█▄█▄▄
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
        ^^^ Made by \033[1;32mAnonSagar\033[0m ^^^
""" )


main_val = input("Enter the text: ")
print("The original string is : " + str(main_val))
temp_res = ''.join(format(ord(i), '08b') for i in main_val)
temp_res = str(temp_res)
if len(temp_res)%6==0:
    mainfunc()
else:
    temp_res = temp_res + "00"
    if len(temp_res)%6==0:
        mainfunc()
    else:
        temp_res = temp_res + "00"
        mainfunc()









