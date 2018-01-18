from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
Base.metadata.reflect(some_engine)

class UserInfo(Base):
    __table__ = metadata.tables['userInfo']
