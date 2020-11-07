import os

def textInFile(string,r,newtext=""):
    oldtext=""
    text=""
    with open(r"C:\Users\kumar\OneDrive\Documents\python\test\text.txt","r") as rf:
        text=rf.read()
        post=text.find(string)
        fist_index=text.find("\"",post)
        last_index=text.find("\"",fist_index+1)
        oldtext=text[fist_index+1:last_index]
    if r!="read":
        text=text.replace(oldtext,newtext)
        with open(r"C:\Users\kumar\OneDrive\Documents\python\test\text.txt","w") as rf:
            rf.write(text)
            return True
    else:
        return oldtext