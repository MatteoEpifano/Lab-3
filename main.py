#First Function


x = [(w) for w in input("Type out a string with spaces between it:\n").split()]

def split (x):
  terms = []
  num = []

  for i in (x): 
    if i.isdigit() == True:
      num.append(i)
    else:
      terms.append(i)
  return terms, num

print(split(x))

def sort(num):
  second list = []
