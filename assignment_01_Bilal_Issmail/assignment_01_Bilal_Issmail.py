print("Excercise 1:")
def findFactorial (n = int(input("Enter an integer: ")),f = ""):
  i=1
  f=1
  for i in range(1,n):
    i+=1
    f*=i
  print("The factorial of your integer is: " + str(f))
findFactorial()
print("Excercise 2")
def findDevisors (n = int(input("Enter a number: ")),list = []):
  i = 0
  while i<=n:
    i+=1
    if n%i==0:
      list.append(i)
  print(list)
findDevisors()
print("Excercise 3")
def reverseString (string = input("Enter your input here:"),reversed_string = ""):
    i = len(string)
    while i >0:
      i-=1
      reversed_string = reversed_string + string[i]
    print (reversed_string)
reverseString()
print("Exercise 4:")
##########
#########
#######
lst = []
n = int(input("how many integer do you want to add to the list? "))
while len(lst) < n:
    item = int(input("Enter an integer:"))
    lst.append(item)
lst1 = []
for x in range(len(lst)):
  if int(lst[x]) %2 == 0:
    lst1.append(lst[x])
print(lst1)
###########
##########
#########
print("Excercise 5:")
str = input("Enter your password: ")
upercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
digit = "1234567890"
special_char = "#?!$"
for char in str:
  if len(str) > 8:
        if (char) == (upercase()):
                  if (char) == (lowercase()):
                            if (char) == (digit()):
                                      if (char) == (special_char()):
                                        print("Strong password")
                                        break
                                      else:
                                        print("Weak password")
                                        break
                            else:
                             print("Weak password")
                             break
                  else:
                      print("Weak password")
                      break
        else:
          print("Weak password")
          break
  else:
    print("Weak password")
    break