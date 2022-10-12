



import pandas as pd
import numpy as np




def temporary_life_annuity_due(age,i,n,sex):
   """Function to compute the EPV of a whole Temporary life annuity  for a given age, interest rate i ,sex="m" or "f", and n-qty of payments
   Arg:
   age:age to calculate the EPV
   i:interes rate
   sex:sex betwen m for male f for female
   n: qty of payments
   return EPV
   """ 
   male=pd.read_excel("male.xlsx")
   female=pd.read_excel("female.xlsx")
   if sex in ("M","m","male","Male") :
      x=male
   elif sex in ("F","f","Female","female"):
      x=female
   else: 
      return print("choose sex between "" M"" m male for Male or  ""F""f female  for Female in quotation marks")
   if (i >1) :
      
    print("i need to be less than 1")  
   elif(i<0):

      print("i need to be more than 0")
   else:
     i=i   
   if age>len(x):
     print("age is large than the life table")
   elif(age<1):

      print("age need to be more than 1")  
   else:
      age=age   
     
      
   x["px"]= 1-x["qx"]
   px=x[["Age","px"]]
   kpx=px[age+1:age+n+1]
   kpx=kpx.cumprod()
   kpx.loc[age,['px']] = 1
   kpx=kpx.sort_index()
   kpx=kpx.drop(["Age"],axis=1)
   kpx=np.array(kpx)
   lista=np.array(range(0,n+1, 1))
   discount=(1+(i))**-lista
 
   return print(np.dot(discount,kpx))




