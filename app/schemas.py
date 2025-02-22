from pydantic import BaseModel, constr, field_validator
from typing import Optional, Annotated
from enum import Enum
import re


class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"


class StatusEnum(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    done = "done"


class TaskCreate(BaseModel):
    title: Annotated[str, constr(min_length=3, max_length=100)]
    description: Optional[str] = None
    priority: PriorityEnum

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    title: Optional[Annotated[str, constr(min_length=3, max_length=100)]] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None

    class Config:
        orm_mode = True


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: StatusEnum
    priority: PriorityEnum

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: Annotated[str, constr(min_length=3, max_length=20)] 
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if not re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$", value):
            raise ValueError(
                "Password must have at least 8 characters, 1 uppercase letter, 1 number, and 1 special character (@$!%*?&)"
            )
        return value


class UserLogin(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
