from repository.user_repository import UserRepository

class UserService:

    def __init__(self, session):
        self.repo = UserRepository(session)
        


    def list_users(self):
        return self.repo.get_all()





    def add_user(self,name):
        cleaned = name.strip()
        
        if len(cleaned) == 0:
            return False, "empty name"
        
        
        exisiting_user = self.repo.get_by_name(cleaned)
        if exisiting_user is not None:
            return False, "deplicate name"
        
        user = self.repo.add(cleaned)
        return True,user




    def user_exists(self,name):
        cleaned = name.strip()
        return self.repo.get_by_name(cleaned)

    
    def delete_user(self,name): 
        cleaned = name.strip()

        user = self.repo.get_by_name(cleaned)

        if user is None:
            return False
        
        self.repo.delete(user)
        return True



    def update_user(self,old_name, new_name):
        cleaned_old_name = old_name.strip()
        cleaned_new_name = new_name.strip()

        user = self.repo.get_by_name(cleaned_old_name)
        if user is None:
            return False, "user not found"
        
        if len(cleaned_new_name) == 0:
            return False, "new name can not be empty"
        
    
        exisiting_user = self.repo.get_by_name(cleaned_new_name)
        if exisiting_user is not None and exisiting_user.id != user.id:
            return False, "name already taken"
        
        
        updated_user = self.repo.update_name(user,cleaned_new_name)
        return True, updated_user