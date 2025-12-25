import database

def create_user(data):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    cursor.execute(
        "EXEC CW2.UserTableCreate ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?",
        data.FirstName, data.Surname, data.Email, data.Password,
        data.UserID, data.LanguageID, data.Height, data.Weight,
        data.ActivityTimePref, data.Bio, data.PhoneNumber
    )
    conn.commit()
    return get_user(data.UserID)

def get_user(user_id: int):
    conn = database.get_database_connection()
    cursor = conn.cursor()
    cursor.execute("EXEC CW2.UserTableRead ?", user_id)
    row = cursor.fetchone()
    if row:
        columns = [column[0] for column in cursor.description]
        user_dict = dict(zip(columns, row))
        return user_dict
    return None

# ... (update_user and delete_user remain the same)
