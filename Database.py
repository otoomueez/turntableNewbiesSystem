import sqlite3


class Database:
    def __init__(self):
        self.query = """CREATE TABLE IF NOT EXISTS Applicants(
                f_name TEXT NOT NULL,
                m_name TEXT,
                l_name TEXT NOT NULL,
                gender TEXT NOT NULL,
                email TEXT PRIMARY KEY NOT NULL,
                telephone TEXT,
                year_of_graduation INTEGER,
                school TEXT,
                application_type TEXT NOT NULL,
                upload_resume BLOB NOT NULL
            )"""

        self.insert_query = """INSERT INTO Applicants 
                (f_name, m_name, l_name, 
                gender, email, telephone, year_of_graduation, 
                school, application_type, upload_resume)

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

        self.clear_all_query = """DELETE FROM Applicants"""

        self.get_data_query = """SELECT f_name, m_name, l_name, gender, 
                                        email, telephone, year_of_graduation, 
                                        school, application_type, upload_resume 
                                        FROM Applicants"""

    def create_table(self):
        self.open_connection()
        self.cursor.execute(self.query)
        self.close_connection()
        return 0

    def search_data(self, field, value):
        self.open_connection()
        self.cursor.execute('SELECT * FROM Applicants WHERE %s LIKE "%s" ' % (field, value))
        result = self.cursor.fetchall()
        self.close_connection()
        return result

    def insert_data_to_db(self, data):
        self.open_connection()
        self.cursor.execute(self.insert_query, data)
        self.connection.commit()
        self.close_connection()
        return 0

    def get_data(self):
        self.open_connection()
        self.cursor.execute(self.get_data_query)
        result = self.cursor.fetchall()
        self.close_connection()
        return result

    def clear_db(self):
        self.open_connection()
        self.cursor.execute(self.clear_all_query)
        self.connection.commit()
        self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def open_connection(self):
        self.connection = sqlite3.connect("Applicants.db")
        self.cursor = self.connection.cursor()


