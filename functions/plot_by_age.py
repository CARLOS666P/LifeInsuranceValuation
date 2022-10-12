
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt






def plot_by_age(function, i, sex):
    ages = range(0, 100, 1)
    df = []
    for age in ages:
      age = age + 1
      epv = function(age=age, i=i, sex= sex).tolist()
      data = [epv, age]
      df.append(data)  
    
    df = pd.DataFrame(df, columns = ["EPV", "Age"])
    df["EPV"] = df["EPV"].astype(str)
    df["EPV"] = df["EPV"].str.replace("[", "",regex=False)
    df["EPV"] = df["EPV"].str.replace("]", "",regex=False)
    df["EPV"] = df["EPV"].astype(float)
    
    df.plot(y="EPV", x="Age", kind="line", figsize=(10,10))
    return (plt.show())









