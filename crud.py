import database #Uses database.py to connect to the database

def create_user(data): #Create procedure 
    conn = database.get_database_connection() #
    cursor = conn.cursor() #Cursor used to execute SQL commands
    cursor.execute( 
        "EXEC CW2.UserTableCreate ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?", #Pulls from create procedure in the database along with the necessary parameters to be entered
        data.FirstName, data.Surname, data.Email, data.Password,
        data.UserID, data.LanguageID, data.Height, data.Weight,
        data.ActivityTimePref, data.Bio, data.PhoneNumber
    )
    conn.commit() #Pushes to database
    return get_user(data.UserID) #Returns the created user, using the new user ID and get function

def get_user(user_id: int): #Read procedure
    conn = database.get_database_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CW2.UserTableRead ?", user_id) #Pulls from read procedure uses userid as parameter
    row = cursor.fetchone() #Gets row of the result set
    if row:
        columns = [column[0] for column in cursor.description] #gets name of column
        user_dict = dict(zip(columns, row)) #
        return user_dict
    return None

def update_user(user_id: int, data): #Update procedure
    conn = database.get_database_connection()
    cursor = conn.cursor()
    cursor.execute( 
        "EXEC CW2.UserTableUpdate ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?", #Pulls from update procedure in the database and forces use of necessary parameters to update a user profile
        user_id, data.FirstName, data.Surname, data.Email, data.Password,
        data.LanguageID, data.Height, data.Weight,
        data.ActivityTimePref, data.Bio, data.PhoneNumber
    )
    conn.commit()
    return get_user(user_id) #Commits to database and pulls new user to display 

def delete_user(user_id: int): #Delete procedure
    conn = database.get_database_connection() #Gets connection to database
    cursor = conn.cursor()
    cursor.execute("EXEC CW2.UserTableDelete ?", user_id) #Pulls from delete procedure in database and uses userid as parameter
    conn.commit()
    return True #If deleted, return true
        columns = [column[0] for column in cursor.description]
        user_dict = dict(zip(columns, row))
        return user_dict
    return None

# ... (update_user and delete_user remain the same)
