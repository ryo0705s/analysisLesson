import os
import csv
# print(os.getcwd()) 
master = "/Users/sasakiryou/Desktop/演習用フォルダ/python_excel/lesson/analysisLesson/"
dir = "data/"
c_file = "WORK_分析共有_顧客情報"
csv_file = open(master + dir + c_file + ".csv", encoding="shift-jis")
c = csv.reader(csv_file)
header = next(c)
c_list = []
for i in c:
  c_list.append(i)
  
# print(c_list) 
new_header = header
new_header.extend(["退会週", "登録更新者", "hosid分類", "キャンペーン分類"])
# print(new_header)
