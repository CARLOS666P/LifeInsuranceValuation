
from functions.life_immediate_annuity import life_immediate_annuity
from functions.life_annuity_due import life_annuity_due
from functions.plot_by_age import plot_by_age
from functions.temporary_life_annuity import temporary_life_annuity_due
from functions.whole_life_insurance import whole_life_insurance
from functions.plot_by_age import plot_by_age
from functions.plot_by_rate import plot_by_rate
from functions.Temporary_life_insurance import temporary_life_insurance
from functions.deferred_whole_life_insurance import deferred_whole_life_insurance

#function that calculates the EPV of a (whole) life annuity due on  for a given constant interest rate  and sex life table.



#run with a Male ,20 year and interest rate = 3%

life_annuity_due(20,0.03,"M")

#run with a Female,30 year and interest rate = 7%

life_annuity_due(30,0.07,"F")

#Since the benefit is constant at 1 EUR, there is no need to take it explicitly into account in the calculations.


#Function to compute the EPV of a whole life immediate annuity for a given age, interest rate i and sex life table

#run with a Male ,20 year and interest rate = 3%

life_immediate_annuity(20,0.03,"M")

#run with a Female,30 year and interest rate = 7%

life_immediate_annuity(30,0.07,"F")

#Since the benefit is constant at 1 EUR, there is no need to take it explicitly into account in the calculations.

## Function to compute the EPV of a temporary life annuity due for a given age, period of n years, interest rate i and  sex life table

#run with a Male ,20 year and interest rate = 3% and temporary of 10 years 

temporary_life_annuity_due(20,0.03,10,"M")

#run with a Female ,30 year and interest rate = 7% and temporary of 15 years 

temporary_life_annuity_due(30,0.07,15,"F")

#Since the benefit is constant at 1 EUR, there is no need to take it explicitly into account in the calculations.

# Function to compute the EPV of a whole life insurance

#run with a Male ,20 year and interest rate = 3%

whole_life_insurance(20,0.03,"M")
#doing some plots

plot_by_age(whole_life_insurance,0.03,"M")
plot_by_rate(whole_life_insurance,"M",20)


#Since the benefit is constant at 1 EUR, there is no need to take it explicitly into account in the calculations.

# Function to compute the EPV of a temporary life insurance

#run with a Male ,20 year and interest rate = 3% and temporary insurance of 45 years 

temporary_life_insurance(20,0.03,45,"M")

#Since the benefit is constant at 1 EUR, there is no need to take it explicitly into account in the calculations.

# Function to compute the EPV of a deferred whole life insurance

#run with a Male ,20 year and interest rate = 3% and deferred 10 years

deferred_whole_life_insurance(20,10,0.03,"M")

