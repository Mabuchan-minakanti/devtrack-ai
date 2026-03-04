from datetime import datetime

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(datetime,default = datetime.utcnow)