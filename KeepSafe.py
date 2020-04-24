import yaml
import os
import sys
import json
import io
import shutil
import didumean as did_u

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'holder.yml')
my_error_file = os.path.join(THIS_FOLDER, 'forerror.yml')
askToCopy = False
onlyPassword = 0


def Enc(onlyPassword):
    my_file2 = os.path.join(THIS_FOLDER, 'holder.yml').encode("ascii")
    new_file2 = os.path.join(THIS_FOLDER, 'temp.yml').encode("ascii")
    with io.open(my_file2, "r", encoding="utf-8") as f:
        with io.open(new_file2, "w", encoding="utf-8") as d:
            for line in f:
                for ch in line:
                    d.write(chr((ord(ch) + onlyPassword) % 256))
    d.close()
    f.close()
    os.remove(my_file2)
    os.rename(new_file2, my_file2)


def Dec(onlyPassword):
    my_file3 = os.path.join(THIS_FOLDER, 'holder.yml').encode("ascii")
    new_file3 = os.path.join(THIS_FOLDER, 'temp2.yml').encode("ascii")
    with io.open(my_file3, "r", encoding="utf-8") as f:
        with io.open(new_file3, "w", encoding="utf-8") as d:
            for line in f:
                for ch in line:
                    d.write(chr((ord(ch) - onlyPassword) % 256))
    d.close()
    f.close()
    os.remove(my_file3)
    os.rename(new_file3, my_file3)


def Read(a):
    fixer = []
    might = []
    Dec(onlyPassword)
    try:
        with open(my_file, "r") as rawD:
            data = yaml.load(rawD, Loader=yaml.FullLoader)
    except Exception as ex:
        print("""
        +------------------------+
        |    Fuck of Looser {}   |
        +------------------------+
        """.format(ex))
        savePassword()
        quit()
    if data is None:
        Enc(onlyPassword)
        return None
    asil = data.get(a)
    if asil is None:
        for key, value in data.items():
            might.append(key)
        snc = did_u.u_mean(a, might)
        if snc is not None:
            YorN = input("""
            +---------------------------+
            | Did you mean ? {}  (y/n)  
            +---------------------------+
            """.format(snc))
            if YorN == "y" or YorN == "Y":
                # Enc()
                asil = data.get(snc)
                fixer.append(snc)

            else:
                Enc(onlyPassword)
                return None
        else:
            Enc(onlyPassword)
            return None
            # for key,value in data.items():
        #    might.append(value)
        # Enc()
        # return None
    else:
        fixer.append(a)
    for key, value in asil.items():
        fixer.append(value)
    # print("Kullanici adi : {} Sifre : {} ".format(fixer[0],fixer[1]))
    Enc(onlyPassword)
    return fixer


def Write(a, b, c):
    Dec(onlyPassword)
    data2 = {a: {'kullanici_adi': b, 'sifre': c}}
    try:
        with open(my_file, "a") as rawD:
            yaml.dump(data2, rawD)
    except:
        print("""
        +------------------------+
        |    Fuck of Looser      |
        +------------------------+
        """)
        savePassword()
        quit()
    Enc(onlyPassword)
    global askToCopy
    askToCopy = True
    print("Added!!!")
    print(askToCopy)


def isExist(a):
    Dec(onlyPassword)
    try:
        with open(my_file, "r") as rawD:
            data = yaml.load(rawD, Loader=yaml.FullLoader)
    except:
        print("""
        +------------------------+
        |    Fuck of Looser      |
        +------------------------+
        """)
        savePassword()
        quit()
    if data is None:
        Enc(onlyPassword)
        return False
    asil = data.get(a)
    if asil is None:
        Enc(onlyPassword)
        return False
    else:
        Enc(onlyPassword)
        return True


def Update(a, b, c):
    Delete(a, False)
    Dec(onlyPassword)
    try:
        with open(my_file, "r") as rawD:
            data = yaml.load(rawD, Loader=yaml.FullLoader)
    except Exception as ex:
        print("""
        +------------------------+
        |    Fuck of Looser {}   |
        +------------------------+
        """.format(ex))
        savePassword()
        quit()
    data2 = {a: {'kullanici_adi': b, 'sifre': c}}
    try:
        with open(my_file, "a") as rawD:
            yaml.dump(data2, rawD)
            print("Updated!!!")
    except:
        print("""
        +------------------------+
        |    Fuck of Looser      |
        +------------------------+
        """)
        savePassword()
        quit()
    Enc(onlyPassword)
    global askToCopy
    askToCopy = True


def Delete(a, bol):
    Dec(onlyPassword)
    try:
        with open(my_file, "r") as rawD:
            data = yaml.load(rawD, Loader=yaml.FullLoader)
    except Exception as ex:
        print("""
        +------------------------+
        |    Fuck of Looser {}   |
        +------------------------+
        """.format(ex))
        savePassword()
        quit()
    f = open(my_file, "r")
    d = open("temp.yml", "w")
    q = -1
    lena = len(a) + 2
    isex = False
    for line in f:
        if a in line and lena == len(line):
            if bol:
                print("Found and Deleted!!")
                isex = True
            d.write("")
            q = 2
        elif q > 0:
            d.write("")
            q = q - 1
        else:
            d.write(str(line))
    d.close()
    f.close()
    os.remove(my_file)
    os.rename("temp.yml", my_file)
    Enc(onlyPassword)
    if isex == False and bol == True:
        print("This site does not exist!!")
    global askToCopy
    askToCopy = True


def ALL():
    Dec(onlyPassword)
    cnt = 1
    try:
        with open(my_file, "r") as rawD:
            data = yaml.load(rawD, Loader=yaml.FullLoader)
    except Exception as ex:
        print("""
        +------------------------+
        |    Fuck of Looser      |
        +------------------------+
        """)
        savePassword()
        quit()
    if data is None:
        print("Ups. Looks like we have nothing to show :) ")
        Enc(onlyPassword)
        return
    for key, value in data.items():
        print("""
        +------------------------+
        | {}. site | {}
        +------------------------+
        """.format(str(cnt), key))
        cnt = cnt + 1
    Enc(onlyPassword)


def savePassword():
    os.remove(my_file)
    shutil.copy2(my_error_file, my_file)


def updateBackup():
    os.remove(my_error_file)
    shutil.copy2(my_file, my_error_file)


onlyPasswordStr = input("""
+--------------------------------------------+
| The Only Key Which You Have To Remember ?  |
+--------------------------------------------+
""")
onlyPassword = int(onlyPasswordStr)

while True:

    choose = input("""
    +--------------------+
    | What you wanna do? |
    +--------------------+
    | 1.Add Password     |
    | 2.Search Password  |
    | 3.Update Password  |
    | 4.Delete Password  |
    | 5.Display ALL      |
    | 6.Quit             |
    +--------------------+
    """)
    if choose == '1':
        getA = input("""
        +------------------------+
        | Give me the site name  |
        +------------------------+
        """)
        getB = input("""
        +------------------------+
        | Give me the useer name |
        +------------------------+
        """)
        getC = input("""
        +------------------------+
        | Give me the password   |
        +------------------------+
        """)
        Write(getA, getB, getC)
    elif choose == '2':
        getA = input("""
        +------------------------+
        | Give me the site name  |
        +------------------------+
        """)
        temp = Read(getA)
        if temp is None:
            print("This site does not exist!!")
        else:
            print("""
            +----------------+-----------------------------+
            | The Site Name  | {}                            
            +----------------+-----------------------------+
            | The User Name  | {}                          
            +----------------+-----------------------------+
            | The Password   | {}                         
            +----------------+-----------------------------+
            """.format(temp[0], temp[1], temp[2]))
    elif choose == '3':
        getA = input("""
        +------------------------+
        | Give me the site name  |
        +------------------------+
        """)
        check = isExist(getA)
        if check:
            b = input("""
            +-------------------+
            | The New User Name |                      
            +-------------------+
            """)
            c = input("""
            +-------------------+
            | The New Password  |                      
            +-------------------+
            """)
            Update(getA, b, c)
        else:
            print("This site does not exist!!")
    elif choose == '4':
        getA = input("""
        +------------------------+
        | Give me the site name  |
        +------------------------+
        """)
        Delete(getA, True)
    elif choose == '5':
        ALL()
    elif choose == '6':
        if askToCopy:
            getSave = input("""
            +-----------------------------------+
            | Do You wanna replace backup (yes) |
            +-----------------------------------+
            """)
            if getSave == 'yes':
                print("Good choice: )")
                updateBackup()
                quit()
            else:
                print("YOUR LOST MATE......")
                quit()
        else:
            quit()
    else:
        print("Choose one of 'em!!@!")
