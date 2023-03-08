def uppercase(str):
    print(len(str))
    for ele in str:
        if ord(ele) >= 97:
            uppercase = ord(ele) - 32
            print( "{:c}".format(uppercase) if  len(str)-1 else "{:c}\n".format(uppercase), end="")
        else:
            print("{}".format(ele) if len(str)-1 else "{}\n".format(ele), end="")
