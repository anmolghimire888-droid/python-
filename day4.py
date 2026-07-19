# CONTROL FLOW 
## CONDITIONAL STATEMENT
### LOOPING STATEMENT

#1. Finite looping (for_in)

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World"

# 2. EXM OF LOOPING [--FOR--]

# for i  in range(5):   
#  print("ANMOL_BARVE")

# range(1,5,2) => 1  is stsrting value , 5 is stoping value , 5 is excluded ,2 is called step value 

# for i in range (1, 5, 2):
#     print("Welcome home",i)

# MULTIPLICATION TABLE 

# > Writing code manually to righbt multiplication table does not resally amle sense 
#   so here we gana use for loop , range to make multipplication table ti use code ifficenty 

# for i in range(1 , 11):
#     print("2 X", i , "=" ,i*2) -------> purpose of looping FOR

# -----------multipication table using for loop----------------

# number = int(input("Enter your number wich you want to multiply: "))

# for num in range(10 , 0 , -1):
#     print(f"{number} X {num} = {number*num}")

# sentence = "We love nepal" #-> string is an sequence of a character 
# vovals = "aeiouAEIOU"
# count = 0
# char in vovals:
#  'W' in "aeiouAEIOU" => False 
#   "e" in "aeiouAEIOU" => True 6
# for each_char in sentence :
    # check if it's vowel  
#     if  each_char in vovals:
#         print(each_char)
#         count += 1
# print("Num of vowecls in sentence is", count )

# ----------- INFINITE LOOP -----------
#  ----WHILE------------
 
# line_xa  = True # YESS

# fan loop
# while line_xa :
#     print("fam ghumdaixa")
     
#     user_answer = input("Line xa ?? (yes/no):")
    
#     "no"= "no" =>True
#     if user_answer == "no" :
#          line_xa = False

# Account block new variyant 

dummey_password = "adimin123"
MAX_ATTEMPTS = 3
user_attempt = 0

while user_attempt < MAX_ATTEMPTS :
    user_password = input("Enter your password: ")

    if user_password != dummey_password :
        print("Wrong password")
        user_attempt += 1
        print("Attemes left", MAX_ATTEMPTS-user_attempt)
    else :
        print("Login Successfull")
        print("End PROGRAM")
        break
else:
    print("You have attemped wrong passwoed for all attempes")
    print("So your account has been temorarily blocked. Visited office for re-acctivation in nearest branch ")

# --------NOTE-
# --continue => skip the code below 
# --break => means sstrikly dont run code below 