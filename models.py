from pydantic import BaseModel, EmailStr #Pydantic used to create data models
from typing import Optional #Optional used to create fields that are not mandatory

class ProfileInput(BaseModel): #Input model for creating user profile, must fit this model
    FirstName: str
    Surname: str
    Email: str
    Password: str
    UserID: int
    LanguageID: int
    Height: Optional[int] = None #Optional fields set to none if not given
    Weight: Optional[int] = None
    ActivityTimePref: str
    Bio: Optional[str] = None
    PhoneNumber: str

class ProfileUpdate(BaseModel): #Input model for updating user profile, must fit this model
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

class ProfileOutput(BaseModel): #Output model for pulling and displaying a user profile, must fit this model
    UserID: int #Password not returned as is not necessary and is sensitive data, same goes for height, weight and other personal details
    FirstName: str
    Surname: str
    Email: str
    # Do not return the password hash for security reasons
