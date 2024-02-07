# thirdparty
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# project
from db.db_setup import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)

    blog = relationship("Blog", back_populates="user", uselist=False)
    subscriptions = relationship("Subscription", back_populates="user")
