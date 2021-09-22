import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# minimal setting
columns_name = ['instance1','instance2','instance3']
row_cnt = 480
max_value = 100

# all series are equal
def exp_data_a():
    df = pd.DataFrame(index=range(row_cnt), columns=columns_name)
    df = df.assign(instance1=75)
    df = df.assign(instance2=75)
    df = df.assign(instance3=75)
    return df


# all series are random, but has the same mean value
def exp_data_b():
    data = np.random.randint(50, 100, size=(row_cnt, len(columns_name)))
    df = pd.DataFrame(data, columns=columns_name)
    return df


# series has some spike at different time
def exp_data_c():
    df = pd.DataFrame(columns=columns_name)
    data1 = np.random.randint(70, 80, size=row_cnt)
    data2 = np.random.randint(70, 80, size=row_cnt)
    data3 = np.random.randint(70, 80, size=row_cnt)
    for i in range(row_cnt):
        m = i % 120
        if m < 35:
            data1[i] += 20
        elif 40 <= m < 75:
            data2[i] += 20
        elif 80 <= m < 115:
            data3[i] += 20
    df['instance1'] = data1
    df['instance2'] = data2
    df['instance3'] = data3
    return df


def exp_data_d():
    df = pd.DataFrame(columns=columns_name)
    data1 = np.random.randint(60, 80, size=row_cnt)
    data2 = np.random.randint(70, 90, size=row_cnt)
    data3 = np.random.randint(80, 100, size=row_cnt)
    df['instance1'] = data1
    df['instance2'] = data2
    df['instance3'] = data3
    return df


def exp_data_e():
    df = pd.DataFrame(index=range(row_cnt), columns=columns_name)
    df = df.assign(instance1=70)
    df = df.assign(instance2=80)
    df = df.assign(instance3=90)
    return df


def gen_exp_data(folder: str):
    data_a = exp_data_a()
    data_b = exp_data_b()
    data_c = exp_data_c()
    data_d = exp_data_d()
    data_e = exp_data_e()
    data_a.to_csv(path_or_buf=os.path.join(folder, 'data_a.csv'), sep=',', index=False)
    data_b.to_csv(path_or_buf=os.path.join(folder, 'data_b.csv'), sep=',', index=False)
    data_c.to_csv(path_or_buf=os.path.join(folder, 'data_c.csv'), sep=',', index=False)
    data_d.to_csv(path_or_buf=os.path.join(folder, 'data_d.csv'), sep=',', index=False)
    data_e.to_csv(path_or_buf=os.path.join(folder, 'data_e.csv'), sep=',', index=False)


if __name__ == "__main__":
    folder = 'data'
    gen_exp_data(folder)

