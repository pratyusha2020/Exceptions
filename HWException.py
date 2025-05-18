valid= False

while not valid:
    try:
      n=int(input("Enter age:"))
      if n%2==0:
       print("even")
      else:
       print("odd")
       valid=True

    except ValueError:
      print("Invalid input")


      
    