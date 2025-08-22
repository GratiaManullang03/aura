from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository[User]):
    def __init__(self):
        super().__init__(User)
    
    def get_by_name(self, db: Session, name: str) -> Optional[User]:
        """Get user by name"""
        return db.query(User).filter(User.u_name == name).first()