import smtplib

def send_an_email(str):
	smtpUser='your mail address'
	smtpPass='your password'

	toAdd='atakancesim88@yahoo.com'
	fromAdd=smtpUser

	subject='mail subject'
	header='header'
	body=str

	mail=header + '\n\n' + body
	#print(mail)

	s=smtplib.SMTP('smtp.gmail.com',587)

	s.ehlo()
	s.starttls()
	s.ehlo()	

	s.login(smtpUser,smtpPass)
	s.sendmail(fromAdd,toAdd,mail)

	s.quit()
	return mail