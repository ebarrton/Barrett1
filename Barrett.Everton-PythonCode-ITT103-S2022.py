
# Author : Everton Barrett
# Date Created : May 5, 2022
# Course : ITT103
# Purpose ( To create a sales commission calculator program for JamEx Limited to compute each sales person's commission).



##Get sales amount, class number, and sales person number 

answer = "yes"
while answer == "yes":
       
 # Get input of sales amount, class number and sales person number.  

    salesPersNum = str(input("Please enter the salesperson number: "))
    answer = str(input("Please enter the salesperson number: "))
    while (salesPersNum) == answer:   
       print("Please enter the salesperson number: ")

    salesAmt = float(input("Please enter the sales amount: "))

    classNum = int(input("Please enter the class number: "))
   
# compute commission for class number 1 inputs
    if classNum == (1):
     if salesAmt <= 1000:
      commission = salesAmt * 0.06
      print("Sales Person Number is: ", salesPersNum)
      print ("Sales Commission is: ", commission)
     elif salesAmt > 1000 and salesAmt < 2000:
      commission = salesAmt * 0.07
      print("Sales Person Number is: ", salesPersNum)
      print ("Sales Commission is: ", commission)
     elif salesAmt >= 2000:
       commission = salesAmt * 0.1
       print("Sales Person Number is: ", salesPersNum)
       print ("Sales Commission is: ", commission)
  # compute commission for class number 2 inputs 
    if classNum == (2):
     if salesAmt <1000:
       commission = salesAmt * 0.04
       print("Sales Person Number is: ", salesPersNum)
       print ("Sales Commission is ", commission)
     elif salesAmt >= 1000:
       commission = salesAmt * 0.06
       print("Sales Person Number is: ", salesPersNum)
       print ("Sales Commission is: ", commission)
 # compute commission for class number 3 inputs      

    if classNum == (3):
     if salesAmt >0:
       commission = salesAmt * 0.045
       print("Sales Person Number is: ", salesPersNum)
       print ("Sales Commission is: ", commission)
# invalid class number input 
    if classNum > (3):   
       print("Incorrect class number")
             
    else:
       answer = input("Would you like to do another calculation? (yes or no): ")
        

    
  

