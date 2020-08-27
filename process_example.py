import pandas as pd
import argparse
from pandarallel import pandarallel # for pandas parallelization
import multiprocessing as mp
import gc


pandarallel.initialize()

def f(x): #some operations
    return (x + 100) / 2.5

def process_large_dataset_with_pandarallel(df):
    df['x0'] = df['x3'].parallel_apply(f)
    return df

def process_large_dataset_with_multiprocessing(df):
    with mp.Pool(mp.cpu_count()) as pool:
        df['x0'] = pool.map(f, df['x3'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--datasetPath', type=str)
    args = parser.parse_args()

    if args.datasetPath != None:
        df = pd.read_csv(args.datasetPath) #this can take about 3 times size in memory than on disk
        print(df.info(memory_usage='deep')) #use this to check memory usage
        process_large_dataset_with_pandarallel(df)
        # process_large_dataset_with_multiprocessing(df)
        
        #free the memory after processing
        del df 
        gc.collect()