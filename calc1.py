import os
import csv
# print(os.getcwd()) 
master = "/Users/sasakiryou/Desktop/演習用フォルダ/python_excel/lesson/analysisLesson/"
dir = "data/"
file = "WORK_分析共有_顧客情報"
csv_file = open(master + dir + file + ".csv", encoding="shift-jis")
c = csv.reader(csv_file)
header = next(c)
print(header)