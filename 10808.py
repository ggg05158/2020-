word=input()
w_len=len(word)
list=[]
for j in range(26):
    list.append(0)
for i in range(w_len):
    list[ord(word[i])-97]+=1
for k in range(26):
    print(f"{list[k]} ",end='')