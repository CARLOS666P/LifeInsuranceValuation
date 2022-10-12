
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def plot_by_rate(function,sex,age):
    ir = np.arange(0.001, 0.1, 0.001)
    df = []
    for i in ir:
      age = age 
      epv = function(age=age, i=i, sex= sex).tolist()
      data = [epv, i]
      df.append(data)  
    
    df = pd.DataFrame(df, columns = ["EPV", "i"])
    df["EPV"] = df["EPV"].astype(str)
    df["EPV"] = df["EPV"].str.replace("[", "",regex=False)
    df["EPV"] = df["EPV"].str.replace("]", "",regex=False)
    df["EPV"] = df["EPV"].astype(float)
    
    df.plot(y="EPV", x="i", kind="line", figsize=(10,10))
    return (plt.show())


