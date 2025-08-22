from typing import Optional
from datetime import datetime
from pydantic import BaseModel, ConfigDict


class UserBase(BaseModel):
    u_name: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    pass


class UserInDB(UserBase):
    model_config = ConfigDict(from_attributes=True)
    
    u_id: int
    u_created_at: datetime
    u_updated_at: Optional[datetime] = None


class User(UserInDB):
    pass