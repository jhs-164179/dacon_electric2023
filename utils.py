def seed_everything(seed):
    import os
    import random
    import numpy as np
    random.seed(seed)
    np.random.seed(seed)
    os.environ['PYTHONHASHSEED'] = str(seed)



def open_csv(path, file_name):
    import pandas as pd
    f = file_name + '.csv'
    return pd.read_csv(path + f)


def split_datetime(df, col_name, datetime=True):
    import pandas as pd
    # 월, 주, 일, 시간으로 분리
    if datetime:
        df['month'] = df[col_name].dt.month
        df['week'] = df[col_name].dt.week
        df['weekday'] = df[col_name].dt.weekday
        df['day'] = df[col_name].dt.day
        df['hour'] = df[col_name].dt.hour
        df.drop(col_name, axis=1, inplace=True)
    else:
        df['month'] = pd.to_datetime(df[col_name]).dt.month
        df['week'] = pd.to_datetime(df[col_name]).dt.week
        df['weekday'] = pd.to_datetime(df[col_name]).dt.weekday
        df['day'] = pd.to_datetime(df[col_name]).dt.day
        df['hour'] = pd.to_datetime(df[col_name]).dt.hour
        df.drop(col_name, axis=1, inplace=True)


def SMAPE(true, pred):
    import numpy as np
    return np.mean((np.abs(true-pred))/(np.abs(true) + np.abs(pred))) * 100