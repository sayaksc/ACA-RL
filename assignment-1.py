def newstring(string,number):
    if number==0: return string
    else:
        return string+'('+str(number)+')'
def FileNaming(names):
    D={}
    i=0
    ans=[]
    for i in range(len(names)):
        if (names[i] in D.keys()):
            D[names[i]]+=1
        else:
            D[names[i]]=0
        ans.append(newstring(names[i],D[names[i]]))
        # print ans[i],' ',
        if D[names[i]]!=0:
            if (ans[i] in D.keys()):
                D[ans[i]]+=1
            else:
                D[ans[i]]=0
    # print "\n",D
    return ans


#main
names=input()
#names=x.split(" ")
print FileNaming(names);