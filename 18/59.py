# a = input("enter your message")
# if(a<=):
#     print(re)
# b = input("enter three character")
st = input("Enter message:-")
words = st.split(" ")
coding = input("1 for Coding or 0 for Decoding:-")
coding = True if (coding=="1") else False
print(coding)
if(coding):
    nwords = []
    r1 = input("enter first rendom character:-")
    r2 = input("enter another random character:-")

    for word in words:
    
      if(len(word)>=3):
        stnew = r1 + word[1:] + word[0] + r2
        nwords.append(stnew)
      else:
         nwords.append(word[::-1])

    print(" ".join(nwords))

else:
    nwords = []
    for word in words:
    
      if(len(word)>=3):
        stnew = word[3:-3] 
        stnew = stnew[-1] + stnew[:-1]
        nwords.append(stnew)
      else:
         nwords.append(word[::-1])
    print(" ".join(nwords))