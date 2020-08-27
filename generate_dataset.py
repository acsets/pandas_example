import pandas as pd
import numpy as np


def create_large_dataset(length):
    df = pd.DataFrame(np.random.randint(0, 100, size=(length, 3)), columns=['x1', 'x2', 'x3'])
    return df


def main():
    dataset_dir = '~/Desktop/pandas_example/'

    for i in range(3):
        df = create_large_dataset(length = 100000000) #generate large dataset, about 900MB if not changed
        df.to_csv(dataset_dir + str(i) + '.csv', index = False)
main()