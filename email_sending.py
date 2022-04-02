import smtplib
smtpObj = smtplib.SMTP('smtp.outlook.com', 587)
smtpObj.ehlo()

smtpObj.starttls() #encryption
print('*******INLINE EMAIL SENDER 1.0*******')
print('enter email: ')
email = input()

print('enter password: ')
magic_word = input()

smtpObj.login(email,magic_word)


print('processing...')


print('email of recipeint: ')
person = input()
print('message?: ')
message = input()

smtpObj.sendmail('the_classic7@hotmail.com',person,'subject:'+ message + '\nsent through email 1.0')

print('successfully sent...')
print('quitting')
smtpObj.quit()

# today test
