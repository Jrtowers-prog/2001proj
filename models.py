from pydantic import BaseModel, EmailStr
from typing import Optional

class ProfileInput(BaseModel):
    FirstName: str
    Surname: str
    Email: str
    Password: str
    UserID: int
    LanguageID: int
    Height: Optional[int] = None
    Weight: Optional[int] = None
    ActivityTimePref: str
    Bio: Optional[str] = None
    PhoneNumber: str

class ProfileUpdate(BaseModel):
    FirstName: str
    Surname: str
    Email: str
    Password: Optional[str] = None # Password optional on update
    LanguageID: int
    Height: Optional[int] = None
    Weight: Optional[int] = None
    ActivityTimePref: str
    Bio: Optional[str] = None
    PhoneNumber: str

class ProfileOutput(BaseModel):
    UserID: int
    FirstName: str
    Surname: str
    Email: str
    # Do not return the password hash for security reasons
