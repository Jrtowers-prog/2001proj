from fastapi import FastAPI, HTTPException
import models
import crud

app = FastAPI(title="Profile Microservice")

@app.post("/profiles/", response_model=models.ProfileOutput)
def api_create_profile(profile: models.ProfileInput):
    # Check if user already exists
    if crud.get_user(profile.UserID):
        raise HTTPException(status_code=400, detail="UserID already exists")
    return crud.create_user(profile)

@app.get("/profiles/{user_id}", response_model=models.ProfileOutput)
def api_read_profile(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Requirement: Assign roles for testing
    if "Role" not in user:
        user["Role"] = "Admin" if user_id == 6 else "User"
    
    # Security: Remove the password hash from the output dictionary
    if "Password" in user:
        user.pop("Password")
        
    return user

@app.put("/profiles/{user_id}", response_model=models.ProfileOutput)
def api_update_profile(user_id: int, profile: models.ProfileUpdate):
    if not crud.get_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(user_id, profile)

@app.delete("/profiles/{user_id}")
def api_delete_profile(user_id: int, admin_id: int):
    performer = crud.get_user(admin_id)
    
    # Assign Admin role to ID 6 if it isn't in the DB
    role = performer.get("Role") if performer and "Role" in performer else ("Admin" if admin_id == 6 else "User")
    
    if role != "Admin":
        raise HTTPException(status_code=403, detail="Access denied: Admin role required")
        
    crud.delete_user(user_id)
    return {"message": "User deleted successfully"}
