#Function 1

#define x as a string input letting the user know to input a string value with spaces between it. Also make it as a list and use .split function
x = [(w) for w in input("Type out a string with spaces between it:\n").split()]

#define split (x) fest 
def split (x):

  #Create list known as terms
  terms = []
  #create list known as num
  num = []

  #create for loop for x value where if the .isdigit is detected to be true it loops but if it isn't it returns the values
  for i in (x): 

    #If i.isdigit (function) is true, num.append(i) add to list and recycle
    if i.isdigit() == True:
      #num.append and recycle
      num.append(i)

    #else, if i.isdigit != true, append all of the terms and finally return them
    else:
      terms.append(i)

  #returnlists
  return terms, num

#print the split(x)
print(split(x))

#define the sort(num) function and set second list
def sort(num):
  secondlist = []

#Function 2

p, z = split(x)
z = [int(i) for i in z]

def two(z):
  last = []
  patty = []
  patty = sorted(z[1::2], reverse = True)
  del z[1::2]
  last = [None] * (len(z) + len(patty))
  last[::2] = z
  last[1::2] = patty
  return last

print(two(x))