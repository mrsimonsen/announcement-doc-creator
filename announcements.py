import datetime, shutil, os
WEEKS = 35
start = int(input("Enter first announcemnt date in August:\n"))
date = datetime.date(year = datetime.date.today().year, month=8, day=start)
try:
	os.mkdir("announcements")
except FileExistsError:
	shutil.rmtree("announcements")
	os.mkdir("announcements")
os.chdir("announcements")
for i in range(1, WEEKS+1):
	shutil.copyfile("../blank.odt", f"{i:02} - {date.strftime('%b %d')}")
	date = date + datetime.timedelta(days=7)
