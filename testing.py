import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.starttls()
smtpObj.login('Vaxxo9000@gmail.com', 'DuperSuper1337')
smtpObj.sendmail("Vaxxo9000@gmail.com", "sokolov_lev2003@mail.ru", "go to bed!")
smtpObj.quit()
