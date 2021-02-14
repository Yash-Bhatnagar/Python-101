def count_qty(cont,char):
    count = 0
    for x in cont:
        if x == char:
            count +=1
    return count

def all_alphabets(cont):
    tot=0.0
    for a in "abcdefghijklmnopqrstuvwxyz ":
        count = count_qty(cont,a)
        total_len=len(cont)
        percent_qty = count*100/total_len
        tot+=round(percent_qty,2)
        print("{0} occurs : {1} % ".format(a,round(percent_qty,2)))
    print("Total percent = {} %".format(round(tot),2))

#Writing
print()
with open("D:\Yash\Practical\Learning Python\Files to access\TextAnalyzer.txt") as file :
    txt_cont=file.read()
    all_alphabets(txt_cont)


