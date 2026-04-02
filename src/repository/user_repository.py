from sqlalchemy import select
from models.user import User

class UserRepository:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        statement = select(User)
        return self.session.scalars(statement).all() #Select * from users;
    
    def get_by_name(self,name):
        statement = select(User).where(User.name == name) #Select * from users where name = "Yahya";
        return self.session.scalars(statement).first()
    
    def add(self, name):
        user = User(name = name)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
    
    def delete(self, user):
        self.session.delete(user)
        self.session.commit()


    def update_name(self, user, new_name):
        user.name = new_name
        self.session.commit()
        self.session.refresh(user)
        return user    
       
