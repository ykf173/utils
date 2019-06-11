#空格分隔txt文件，读取成为csv文件
#2019-6-11
#闫凯峰

import csv

def data_read(filepath):
    fp = open(filepath, "r")
    datas = []  # 存储处理后的数据
    lines = fp.readlines()  # 读取整个文件数据
    i = 0  # 为一行数据
    for line in lines:
        row = line.strip('\n').split()  # 去除两头的换行符，按空格分割
        datas.append(row)
        i = i + 1
        #print("读取第", i, "行")

    fp.close()
    return datas

horse_txt_file = 'data/horse-colic_train.txt'
horse_csv_file = 'data/csv/horse-colic_train.csv'
with open(horse_csv_file, "w", newline='') as f:
    writer = csv.writer(f)
    #writer.writerows([birth_header])
    horse_data = data_read(horse_txt_file)
    print(horse_data)
    writer.writerows(horse_data)
    f.close()

