from sqlalchemy import Column, BigInteger, String, DateTime
from sqlalchemy.sql import func

from app.db.base import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "atabot"}
    
    u_id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    u_name = Column(String, nullable=True)
    u_created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    u_updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)