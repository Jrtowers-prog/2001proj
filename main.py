from fastapi import FastAPI, HTTPException #FastAPI framework and HTTPException is used for throwing errors
import models #Used to check the models set up in models.py
import crud #Used to call the CRUD operations set up in crud.py

app = FastAPI(title="Profile Microservice") #Starts application and sets the title

@app.post("/profiles/", response_model=models.ProfileOutput) #POST endpoints (if someone sends a POST request to /profiles/ run the below function, also check if it fits the ProfileOutput model)
def api_create_profile(profile: models.ProfileInput): 
    if crud.get_user(profile.UserID): #Check if urer already exists
        raise HTTPException(status_code=400, detail="UserID already exists")
    return crud.create_user(profile) #If doesn't exist, calls create user from crud.py

@app.get("/profiles/{user_id}", response_model=models.ProfileOutput) #GET endpoint is /profile/userID, then checks for valid format again 
def api_read_profile(user_id: int): #Checks user id is an integer
    user = crud.get_user(user_id) #Calls crud function to pull user
    if not user:
        raise HTTPException(status_code=404, detail="User not found") #Throws error if not found
    
    if "Role" not in user: #Assign Admin role to ID 6 if it isn't in the database
        user["Role"] = "Admin" if user_id == 6 else "User"
    
    if "Password" in user: #Gets rid of password from output, just in case model set up in models.py doesn't work, extra precaution
        user.pop("Password")
        
    return user

@app.put("/profiles/{user_id}", response_model=models.ProfileOutput) #PUT endpoint to update profile
def api_update_profile(user_id: int, profile: models.ProfileUpdate): #Checks user id is an int and input matches the update model
    if not crud.get_user(user_id): #Checks if user exists
        raise HTTPException(status_code=404, detail="User not found") #Throws error if not
    return crud.update_user(user_id, profile) #Calls crud function if found

@app.delete("/profiles/{user_id}") #DELETE endpoint is /profile/userID
def api_delete_profile(user_id: int, admin_id: int): #Checks if user id is an int, also checks admin id for being int, both need to be true
    performer = crud.get_user(admin_id)
    role = "User" #Set default role to user
    if admin_id == 6: #If admin ID is 6, role = admin
        role = "Admin"
    if performer and "Role" in performer: #If person doing action (performer) is in database and has a role, use that role instead
        role = performer["Role"]
    if role != "Admin":
        raise HTTPException(status_code=403, detail="Access denied: Admin role required") #If not admin making request, throw access denied error
    crud.delete_user(user_id) #Else, call delete function and give success response
    return {"message": "User deleted successfully"}
