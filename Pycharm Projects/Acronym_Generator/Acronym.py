user_input = str(input("Enter Your Phrase : "))
lst = user_input.split(" ")
st = ""
for wrd in lst:
    st = st+str(wrd[0]).upper()
print(st)
