import pandas as pd
from datetime import datetime


class Computation:
    data = pd.read_csv("./files/dataBRA.csv")
    data['Data'] = pd.to_datetime(data['Data'])
