#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import modules
import numpy.core._dtype_ctypes
import pandas as pd
import glob
import os
import warnings
warnings.filterwarnings('ignore')


# parameters
#try:
#    input_ = input('閾値 = ')#
#    threshold = float(input_)
#except:
#    print('入力が正しくありません')
while True:
    try:
        input_ = input("閾値 = ")
        threshold = float(input_)
        #if type(threshold) == 'float' :
        #    break
        #print(input_)
        break
    except:
        print('入力が正しくありません')

# get names of directory
path = 'CSV'
dir_name_tmp = os.listdir(path)
dir_name_tmp = [f for f in dir_name_tmp if os.path.isdir(os.path.join(path, f))]


for dir_name in dir_name_tmp:
    print("\n")
    print("-----現在のフォルダ-----")
    print(dir_name)
    # get names of  csv files
    path = 'CSV/' + dir_name
    files = os.listdir(path)
    files_file = [f for f in files if os.path.isfile(os.path.join(path, f))]
    csv_name_tmp = files_file

    print("-----csvのリスト-----")
    print(csv_name_tmp)

    print('-----csvファイルを結合します-----')
    for i in range(len(csv_name_tmp)):
        # load data
        target_file_name = path + '/' + csv_name_tmp[i]
        print(target_file_name)
        df = pd.read_csv(target_file_name,encoding='cp932',header = None)

        # split csv_data into head and data
        df_head = df[:14].rename(columns={0: 'data'})
        df_data = df[14:].rename(columns={0: 'data'})

        # extract data threshold or below
        tmp_data = df_data['data'].astype(float)
        tmp_data = [a for a in tmp_data if a>=threshold]
        df_data = pd.DataFrame({'data':tmp_data})

        # merge data
        if i==0:
            # header
            df_head_all = df_head

            # create df_data_all
            df_data_all = df_data
            #print(len(df_data_all))
        else:
            # concat data
            df_data_all = pd.concat([df_data_all,df_data])
            #print(len(df_data_all))


    # save merged data
    df_all = pd.concat([df_head_all,df_data_all])
    path = 'CSV_MERGED/' + dir_name + '.csv'
    df_all.to_csv(path,header=False,index=False,encoding='cp932')
    print('-----CSVファイルが保存されました-----')
    print(path)

print("\n")
