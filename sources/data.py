import pandas as pd
import numpy as np

def genDataFrame():
    x = np.arange(1, 10, 0.1)
    y1 = np.sin(x)
    y2 = np.sqrt(x)
    data = {'x':x, 'y1':y1, 'y2':y2}
    df = pd.DataFrame(data)
    #print(df)
    return df
    