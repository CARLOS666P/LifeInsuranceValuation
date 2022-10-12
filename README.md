# LifeInsuranceValutation

Using the life tables of the Dominican Republic for the year 2000, and through financial and Actuarial stochastic models, develop a series of functions in Python for the valuation of simple life insurance based on the calculation of the expected present value, as you will see in detail below.

life annuity due
![lifeannuitydue](https://user-images.githubusercontent.com/59314598/195382812-a555066f-e20b-4903-bf39-90b511c89923.jpg)
 
through the function: life_annuity_due(age,interesRate, sex)
for example a Male ,20 year and interest rate = 3%

life_annuity_due(20,0.03,"M")

[26.99898183]

life immediaty annuity

![immeaditannuity1](https://user-images.githubusercontent.com/59314598/195383950-86799c0f-884d-49af-8e7a-519995c62410.jpg)

through the function: life_immediaty_annuity(age,interesRate, sex)
for example a Male ,20 year and interest rate = 3%

life_immediaty_annuity(20,0.03,"M")

[28.10594413]

temporary life annuity due

![3](https://user-images.githubusercontent.com/59314598/195385635-63a3dff7-6217-4a87-949d-1cd69d7e923e.jpg)

through the function: temporary_life_annuity_due(age,interesRate,n, sex)
for example a Male ,20 year ,period of 10 years and interest rate = 3%

temporary_life_annuity_due(20,0.03,10,"M")

[27.10594413]

whole life insurance

![4](https://user-images.githubusercontent.com/59314598/195386734-5dddcb93-5b0a-459c-9f74-998b193ba920.png)

through the function: whole_life_insurance(age,interesRate,sex)

for example a Male ,20 year and interest rate = 3%

whole_life_insurance(20,0.03,"M")

[9.48982548]

doing some plots includes in the functions 

plot_by_age(whole_life_insurance,0.03,"M")
![plotbyage](https://user-images.githubusercontent.com/59314598/195387376-019333c4-e147-49a7-bb5b-964135daf17c.jpg)

plot_by_rate(whole_life_insurance,"M",20)


![plotbyrate](https://user-images.githubusercontent.com/59314598/195387408-b3d7e464-1890-4b3c-943f-212f665199ea.jpg)

temporary life insurance

through the function: temporary_life_insurance(age,interesRate,n,"M")

for example a male,20 year, interest rate= 3%  a duration of 45 year

temporary_life_insurance(20,0.03,45,"M")

[0.07455318]

deferred whole life insurance
![6](https://user-images.githubusercontent.com/59314598/195390405-14fa15a6-6224-47e7-a1e7-b7988b5eea10.jpg)

trough the function: deferred_whole_life_insurance(age,deferred,interestRate,sex)

for example a male, 20 year, interest rate=3% and deferred 10 periods
deferred_whole_life_insurance(20,10,0.03,"M")

0.2050367514161077
