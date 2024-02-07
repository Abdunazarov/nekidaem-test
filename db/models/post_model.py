# thirdparty
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# project
from db.db_setup import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    blog_id = Column(Integer, ForeignKey("blogs.id"))

    blog = relationship("Blog", back_populates="posts")
