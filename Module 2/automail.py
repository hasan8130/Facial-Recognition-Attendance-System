import yagmail
import os
import datetime
from datetime import datetime;
#date = datetime.date.today().strftime("%B %d, %Y")
path = 'firebase\attendance_files'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(datetime.now().date())
# mail information
yag = yagmail.SMTP("", "thus hlls vvwb pnrx")

# sent the mail
yag.send(
    to='',
    subject='Attendance of ECAM_2', # email subject
    contents='please find attached the attendance for'+str(datetime.now().date())+"." , # email body
    attachments= filename  # file attached 
)
print("Email Sent!")
