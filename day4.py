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

sentence = "We love nepal" #-> string is an sequence of a character 
vovals = "aeiouAEIOU"
count = 0
# char in vovals:
#  'W' in "aeiouAEIOU" => False 
#   "e" in "aeiouAEIOU" => True 6
for char in sentence :
    # check if it's vowel 
    if  char in vovals:
        print(char)  
        count += 1
print ("Num of vowel in sentence", count )




