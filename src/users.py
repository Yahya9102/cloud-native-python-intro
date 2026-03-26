users = []
# TODO 
# ADD Delete function
# Add update function




# TODO EXTRA IF ABOVE IS NOT ENOUGH
# Implemnt age for each user
# Check age of user to see if they are allowed to register
# if below 14 NO REGISTER ALLOWED
# otherwise its okey



def add_user(name):
    cleaned = name.strip()

    if len(cleaned) == 0:
        return False
    
    if cleaned in users:
        return False
    
    users.append(cleaned)
    return True



def list_users():
    return users


def user_exists(name):

    cleaned = name.strip()
    return cleaned in users