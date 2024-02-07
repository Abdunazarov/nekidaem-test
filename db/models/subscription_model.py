# thirdparty
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

# project
from db.db_setup import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    user = relationship("User", back_populates="subscriptions")
    blog = relationship("Blog", back_populates="subscribers")
