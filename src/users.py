users = []
# TODO 
# ADD Delete function
# Add update function




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



def delete_user(name): 
    cleaned = name.strip()

    if cleaned in users:
        users.remove(cleaned)
        return True
    return False



def update_user(old_name, new_name):
    cleaned_old_name = old_name.strip()
    cleaned_new_name = new_name.strip()

    if cleaned_old_name not in users:
        return False, "user not found"
    
    if len(cleaned_new_name) == 0:
        return False, "new name can not be empty"
    
    if cleaned_new_name in users:
        return False, "name already taken"
    
    index = users.index(cleaned_old_name)
    
    users[index] = cleaned_new_name
    
    return True, "name updated"
