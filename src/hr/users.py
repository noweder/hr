import pwd

# We are naming our function fetch_users
def fetch_users():
    # we will start with an empty user list
    users = []
    
    # Now we are going to start a loop. Show ALL of the users, and we will figure out if this is a system user or not with a couple of tests.
    for user in pwd.getpwall():
        # If they have a UID of over 1000, and home is listed in the password directory
        if user.pw_uid >=1000 and 'home' in user.pw_dir:
            # If those are true, then we are going to run a users.append and create a dictionary entry with 4 attributes: name, id, home, and shell.
            users.append({
                'name': user.pw_name,
                'id': user.pw_uid,
                'home': user.pw_dir,
                'shell': user.pw_shell,
            })
        # Back out of our if and for loops                                   
         
    # And then end the function
    return users
