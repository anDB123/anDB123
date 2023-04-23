#Web scraping for a driving instructor
import smtplib
instructorEmails = [["InstuctorName","instructor.name@email.com"]]


sender = "my@yahoo.com"

date='23/04/23'
  
username = str('my@yahoo.com')  
password = str('PASSWORD')  


for instructorEmail in instructorEmails:
    try:
        print(f"instructor name = and email = {instructorEmail[1]}")
        server = smtplib.SMTP("smtp.mail.yahoo.com",587)
        server.starttls()
        server.login(username,password)
        firstName = instructorEmail[0].split()[0]
        subj="Andrew Brown driving instructor request"
        to  = instructorEmail[1]
        message_text=f"Hello {firstName},\nMy name is Andrew and I'm looking for a driving instructor.\nI live in Jesmond and I'm available from 5pm weekdays or at weekend.\nDo you have any availability and what is your hourly rate?\nRegards, Andrew"
        msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( fromMy, to, subj, date, message_text )
        server.sendmail(sender, instructorEmail[1],msg)      
        print(f"Successfully sent email to {instructorEmail[1]}")
    except :
        print (f'can\'t send the Email to {instructorEmail[1]} ')
