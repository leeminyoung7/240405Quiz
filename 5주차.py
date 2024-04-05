ex = input("점수를 입력하세요 : ")

num_ex = int(ex)

if num_ex > 70 :
    print("A")
elif num_ex <= 70 and num_ex > 40 :
    print("B")
elif num_ex <= 40 and num_ex > 10 :
    print("C")
else :
    print("D")
