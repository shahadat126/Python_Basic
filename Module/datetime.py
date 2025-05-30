# import time
# from datetime import datetime,date

# print(datetime.now())
# print(date(2025,5,29))
# print(time.time())

# currentime = datetime.now()
# print(currentime.time())
# time.sleep(5)
# print(datetime.now().time())


from datetime import datetime,timedelta
# now = datetime.now()
# print(now.date())
# print(now.year)
# print(now.time())
# print(now)
# print(now.strftime("%y:%m:%d:%H:%M:%B"))
# print(now.strftime("%B"))
# onedate = datetime(2027,5,29,17,58)
# twodate = datetime(2025,5,29,5,55)

# print(onedate - twodate)
# print(type(onedate - twodate))
# text = "15/05/2025"
# a = datetime.strptime(text,"%d/%m/%Y")
# print(a)
# print(type(a))

today= datetime.now()
bill_payment_Day = today + timedelta(days=5, hours=2, minutes=20)
print(bill_payment_Day)
bill_payment_Day = today - timedelta(days=3 , seconds=50)
print(bill_payment_Day)