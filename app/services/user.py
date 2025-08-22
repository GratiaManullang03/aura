from typing import Optional, List
from sqlalchemy.orm import Session

from app.repositories.user import UserRepository
from app.schemas.user import UserCreate, UserUpdate, User


class UserService:
    def __init__(self):
        self.repository = UserRepository()
    
    def get_user(self, db: Session, user_id: int) -> Optional[User]:
        """Get single user"""
        db_user = self.repository.get(db, user_id)
        return User.model_validate(db_user) if db_user else None
    
    def get_users(
        self, 
        db: Session, 
        skip: int = 0, 
        limit: int = 100
    ) -> List[User]:
        """Get list of users"""
        db_users = self.repository.get_multi(db, skip=skip, limit=limit)
        return [User.model_validate(user) for user in db_users]
    
    def create_user(self, db: Session, user: UserCreate) -> User:
        """Create new user"""
        db_user = self.repository.create(db, user.model_dump())
        return User.model_validate(db_user)
    
    def update_user(
        self, 
        db: Session, 
        user_id: int, 
        user: UserUpdate
    ) -> Optional[User]:
        """Update existing user"""
        db_user = self.repository.get(db, user_id)
        if not db_user:
            return None
        
        update_data = user.model_dump(exclude_unset=True)
        db_user = self.repository.update(db, db_user, update_data)
        return User.model_validate(db_user)
    
    def delete_user(self, db: Session, user_id: int) -> bool:
        """Delete user"""
        deleted = self.repository.delete(db, user_id)
        return deleted is not None
    
    def get_total_users(self, db: Session) -> int:
        """Get total count of users"""
        return self.repository.count(db)