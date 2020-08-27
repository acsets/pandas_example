#!/bin/bash

fileList=('~/Desktop/pandas_example/0.csv' '~/Desktop/pandas_example/1.csv' '~/Desktop/pandas_example/2.csv')

for i in "${fileList[@]}"
do
	python3 process_example.py --datasetPath $i
done