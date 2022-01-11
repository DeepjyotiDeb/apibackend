from sqlalchemy.sql.schema import ForeignKey
from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

class BlogDetails(Base):
    __tablename__ = 'blog-details'
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    id = Column(Integer, primary_key= True, index = True)
    title = Column(String(20))
    summary = Column(String)
    body = Column(String)
    # createdOn = Column(DateTime, default= datetime.date.today().strftime("%A"))
    created_on=Column(DateTime(timezone=True), server_default=func.now())
    
    user_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship("User", back_populates= "blogs")

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key= True, index =True)
    # id = Column(uid, primary_key= True, index = True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    blogs = relationship('BlogDetails', back_populates= "creator")
