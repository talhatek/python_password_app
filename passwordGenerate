import random
import pyperclip
import string
from sklearn.utils import shuffle


def lc(L):
    letter=random.choice(string.ascii_lowercase)
    if letter in L:
        return None
    else:
        return letter
def uc(L):
    letter=random.choice(string.ascii_uppercase)
    if letter in L:
        return None
    else:
        return letter
def digit(L):
    letter=random.choice(string.digits)
    if letter in L:
       return None
    else:
        return letter
def special(L):
    letter=random.choice(string.printable[62:93])
    if letter in L:
        return None
    else:
        return letter
def generate():    
    lenght=int(input("Lengt of key ?\n"))
    forbiddenStr=[]
    forbiddenStr=input("Forbidden letters ?\n")
    forbidden=[]
    for i in forbiddenStr:
        forbidden.append(i.lower())
        forbidden.append(i.upper())
    res=[]
    while True:
        add1=lc(forbidden)
        if add1 is not None:
            res.append(add1)
            break
    while True:
        add2=uc(forbidden)
        if add1 is not None:
            res.append(add1)
            break    
    while True:
        add3=digit(forbidden)
        if add3 is not None:
            res.append(add1)
            break
    while True:
        add1=special(forbidden)
        if add1 is not None:
            res.append(add1)
            break
    for i in range(1,lenght-3):
        which=random.randint(0, 3)
        if which==1:
            while True:
                lttr=lc(forbidden)
                if lttr is not None:
                    res.append(lttr)
                    break
        elif which==2:
            while True:
                lttr=uc(forbidden)
                if lttr is not None:
                    res.append(lttr)
                    break
        elif which==3:
            while True:
                lttr=digit(forbidden)
                if lttr is not None:
                    res.append(lttr)
                    break
        elif which==0:
            while True:
                lttr=special(forbidden)
                if lttr is not None:
                    res.append(lttr)
                    break
    lastResult=shuffle(res)
    final=''.join(lastResult)
    pyperclip.copy(final)
    print(final)
    print("copied on the clipboard")
    return final

