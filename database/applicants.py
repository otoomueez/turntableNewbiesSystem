import sqlite3

try:
    conn = sqlite3.connect("Applicants.db")
    # Create a cursor object
    getit = conn.cursor()
    query = """CREATE TABLE Applicants(
        id INTEGER NOT NULL,
        name TEXT,
        photo BLOB,
        resume BLOB
    )"""
    getit.execute("DROP TABLE IF EXISTS Applicants")
    getit.execute(query)
    print("Database successfully created.")
    
    # Create query to accept values
    # query = """INSERT INTO Applicants (f_name, m_name, l_name, email, telephone, year_of_graduation, school, application_type, upload_resume)
                            # VALUES (" Stephen", "Ato", "Akoto", "stephenakoto@gmail.com", "+233544000950", "2022", "UCC", "TLC", " ")"""
    # getit.execute(query)
    # Commit changes to database
    # conn.commit()
    # print("Successfully Updated")
except conn.Error as error:
    print("Error", error)

# Close database after query
finally:
    if conn:
        conn.close