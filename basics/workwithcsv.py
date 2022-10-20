# Below code reads data from a csv file for stocks and writes data into another csv with a formula to calculate daily returns on stocks
import csv
from datetime import datetime


# path = "D:\Suchi\Google Stock Market Data - google_stock_data.csv"
# lines = [line for line in open(path)]
# print(lines[0].strip())
# print(lines[0].strip().split(','))

path = "D:\Suchi\Google Stock Market Data - google_stock_data.csv"
file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)
data = []
for row in reader:
    datetimess = datetime.strptime(row[0],'%m/%d/%Y')
    openss = float(row[1])
    highss = float(row[2])
    lowss = float(row[3])
    closess = float(row[4])
    volumess = int(row[5])
    adjclosess = float(row[6])

    data.append([datetimess,openss,highss,lowss,closess,volumess,adjclosess])
# print(data[0])

return_path = "D:\Suchi\ss.csv"
file = (open(return_path,'w'))

writer = csv.writer(file)
writer.writerow(['Date','DailyReturns'])
# daily return formula  = (today's price - yesterday's price )/yesterday's price
for i in range(len(data) - 1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]

    dailyreturn = (todays_price - yesterdays_price)/yesterdays_price
    # writer.writerow([todays_date,dailyreturn])
    formatteddate = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatteddate,dailyreturn])




