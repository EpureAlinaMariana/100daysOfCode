from art import logo
print (logo)

def suma(a,b):
  """Returneaza rezultatul adunarii"""
  return a +b
  
def scadere(a,b):
  """Returneaza rezultatul scaderii"""
  return a-b

def inmultire(a,b):
  """Returneaza rezultatul inmultirii"""
  return a*b
  
def impartire(a,b):
  """Returneaza rezultatul impartirii"""
  return a/b

operations = {
    "+":suma,
    "-":scadere,
    "*":inmultire,
    "/":impartire
  }

def calculator():
  doAgain = 1
  number1 = float(input("What's the first number?"))
  while (doAgain):
    for key in operations:
      print (key)
    operation =  input("Pick an operation from the item above:")
    number2 = float(input("What's the next number?"))
   
    for key in operations:
      if(key == operation):
        result = operations[operation](number1,number2)
        print (f"{number1} {key} {number2} = {result}")
  
    continueCalc = input(f"Pres y to continue calculation with {result} or'n' to start a new calculation\n")
    if(continueCalc =="y"):
     number1 = result
    else:
      doAgain =0
      calculator()
calculator()