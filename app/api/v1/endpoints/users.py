from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.services.user import UserService
from app.schemas.user import User, UserCreate, UserUpdate
from app.schemas.common import DataResponse, PaginationResponse

router = APIRouter()
user_service = UserService()


@router.get("/", response_model=PaginationResponse[User])
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=1000),
    db: Session = Depends(get_db),
    # current_user: dict = Depends(require_auth)  # Uncomment untuk require auth
):
    """Get list of users with pagination"""
    users = user_service.get_users(db, skip=skip, limit=limit)
    total = user_service.get_total_users(db)
    
    return PaginationResponse(
        success=True,
        message="Users retrieved successfully",
        data=users,
        total=total,
        page=skip // limit + 1,
        size=limit,
        pages=(total + limit - 1) // limit
    )


@router.get("/{user_id}", response_model=DataResponse[User])
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Get single user by ID"""
    user = user_service.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return DataResponse(
        success=True,
        message="User retrieved successfully",
        data=user
    )


@router.post("/", response_model=DataResponse[User])
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    """Create new user"""
    new_user = user_service.create_user(db, user)
    
    return DataResponse(
        success=True,
        message="User created successfully",
        data=new_user
    )


@router.put("/{user_id}", response_model=DataResponse[User])
def update_user(
    user_id: int,
    user: UserUpdate,
    db: Session = Depends(get_db)
):
    """Update existing user"""
    updated_user = user_service.update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return DataResponse(
        success=True,
        message="User updated successfully",
        data=updated_user
    )


@router.delete("/{user_id}", response_model=DataResponse[None])
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    """Delete user"""
    deleted = user_service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    
    return DataResponse(
        success=True,
        message="User deleted successfully",
        data=None
    )