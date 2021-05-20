user_input=int(input("enter a number:-"))
index1=1
print("")
while index1<=user_input:
    print(" ---"*user_input)
    print(f"| {0} "*user_input+"|")
    index1+=1
if index1==user_input+1:
    print(" ---"*user_input)
    