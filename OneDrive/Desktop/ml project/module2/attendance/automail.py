import yagmail
import os
import datetime
from datetime import datetime;
#date = datetime.date.today().strftime("%B %d, %Y")
path = 'attendance\\firebase\\attendance_files'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(datetime.now().date())
# mail information
yag = yagmail.SMTP("hasan.usmani.ug20@nsut.ac.in", "thus hlls vvwb pnrx")

# sent the mail
yag.send(
    to='zrusmani@gmail.com',
    subject='Attendance of ECAM_2', # email subject
    contents='please find attached the attendance for'+str(datetime.now().date())+"." , # email body
    attachments= filename  # file attached 
)
print("Email Sent!")
