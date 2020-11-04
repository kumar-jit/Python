with open(r"C:\Users\kumar\OneDrive\Documents\python\filewr\file1.txt",'r') as rf:
    with open(r"C:\Users\kumar\OneDrive\Documents\python\filewr\file2.txt",'a') as wf:
        lines=rf.readlines()
        for line in lines:
            name,salary=line.split(',')
            l=name+"'s salary is "+salary+"\n"
            wf.write(l)