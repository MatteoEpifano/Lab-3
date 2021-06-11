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

#set p, z = to the split(x)
p, z = split(x)

#set z = to the int(1) for i in z 
z = [int(i) for i in z]


#define two function to represent the second list of numbers that will have each second number in order of decreasing value
def two(z):

  #Create a list called Last to represent last 
  last = []
  #create new list called patty that will be the final
  patty = []


  #Set patty = to sorted and swap z using 1::2 function, while setting reverse equal to true along with it. With this we can order the second numbers from greatest to least 
  patty = sorted(z[1::2], reverse = True)
  #use del function z [1::2] with [1::2] function 
  del z[1::2]

  #set last list = to none function multiplied by the len(z) + len(patty) to complete list polishing
  last = [None] * (len(z) + len(patty))

  #last list [::2] set equalto z
  last[::2] = z


  #finally set last list [1::2] equal to the patty list
  last[1::2] = patty

  #return the 'last' list
  return last

#Print the modified list
print("These are your numbers with every second placed in decending order: ")

#Print the modified list
print(two(x))