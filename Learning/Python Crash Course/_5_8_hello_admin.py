#make list of five or more usernames
usernames = ['admin','james','bruce','steve','barry']

#print message for admin
if usernames:
    for username in usernames:
        if username == 'admin':
            message = 'Hello admin, would you like to see a status report?'
        else:
            message = 'Hello {}, thank you for logging in again.'.format(username)
        print(message)
