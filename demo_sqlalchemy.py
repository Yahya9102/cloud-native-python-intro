from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)


engine = create_engine("mysql+pymysql://root:12345@localhost:3306/users")
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

session = SessionLocal()


new_user = User(name="Yahya")
session.add(new_user)
session.commit()

session.close()
    
