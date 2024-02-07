# thirdparty
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

# project
from db.db_setup import Base


class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="blog")
    posts = relationship("Post", back_populates="blog", post_update=True)
    subscribers = relationship("Subscription", back_populates="blog")
