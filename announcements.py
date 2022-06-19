import datetime, shutil, os
WEEKS = 42
start = int(input("Enter first announcemnt date in August:\n"))
date = datetime.date(year = datetime.date.today().year, month=8, day=start)
thank = datetime.date(year = date.year+1, month=11, day=int(input("What does does thanksgiving break start in November>\n")))
winter = datetime.date(year=datetime.date.today().year, month=12,day=int(input("What day does winter break start in December?\n")))
spring = datetime.date(year=date.year+1, month=4, day=int(input("What day does spring break start in April?\n")))
try:
	os.mkdir("announcements")
except FileExistsError:
	shutil.rmtree("announcements")
	os.mkdir("announcements")
os.chdir("announcements")
dates = [thank]
for i in range(0,15,7):
	dates.append(winter + datetime.timedelta(days=i))
dates.append(spring + datetime.timedelta(days=2))
for i in range(1, WEEKS+1):
	if date not in dates:
		shutil.copyfile("../blank.odt", f"{i:02} - {date.strftime('%b %d')}.odt")
	date += datetime.timedelta(days=7)
