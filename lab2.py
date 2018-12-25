# import Tkinter as tk
# import tkSimpleDialog as simpledialog

# a=[5,10,15,20,25]
# def lis1 (a):
# 	b = [a[0],a[-1]]
# 	print(b)
# lis1(a)


# a = [1,1,2,3,5,8,13,21,34,55,89]
# b=[]
# c = int(input("Enter Number"))
# def lis2(a,b,c):	
# 	for n in range(len(a)):
# 		if a[n] < c:
# 			b.append(a[n])
# 	print(b)

# a = [1,1,2,3,5,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# c = []
# for i1 in range(len(a)):
# 	for i2 in range(len(b)):
# 		if b[i2] == a[i1]:
# 			c.append(a[i1])

# print(c)


# Num = simpledialog.askstring("input","Enter a Number", parent = tk.Tk().withdraw())
# Num = int(Num)
# if ((Num % 2 != 0) and (Num % 3 != 0) and (Num % 5 != 0) and (Num % 7 != 0)):
# 	print("Prime")
# elif ((Num == 2) or (Num == 3) or (Num == 5) or (Num ==7)):
# 	print("Prime")
# else:
# 	print("Not Prime")