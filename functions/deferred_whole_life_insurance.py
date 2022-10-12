
import pandas as pd
import numpy as np




def deferred_whole_life_insurance(age,u,i,sex):
   """Function to compute the EPV of a whole life insurance for a given age, interest rate i and life tableand u-qty of deferred payments and sex life tab;e
   Arg:
   Arg:
   age:age to calculate the EPV
   i:interes rate
   sex:sex betwen m for male f for female
   u:qty of deferred payments
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
     
   qx=x[ ["Age","qx"] ]
   qx=qx.drop(["Age"],axis=1)
   x["px"]= 1-x["qx"]
   px=x[["Age","px"]]
   kpx=px[age+1:len(px)-1]
   kpx=kpx.cumprod()
   kpx.loc[age,['px']] = 1
   kpx=kpx.sort_index()
   kpx=kpx.drop(["Age"],axis=1)
   kpx=np.array(kpx)

   kqx=kpx*qx[(age+1):len(qx)]
   
   
   limit = len(kqx)
   kqx=kqx["qx"]
   kqx=np.array(kqx)
   lista=np.array(range(1, limit+1, 1))
   discount=(1+(i))**-lista
   benefit1=pd.Series([0,1])
   benefit=benefit1.repeat([u,len(kpx)-u])
   benefit=np.array(benefit)
   final=discount*benefit
   return print(np.dot(final,kqx))




