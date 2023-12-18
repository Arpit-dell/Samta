import mysql.connector


def setup_database():
    try:
        
        connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="admin"
        )

        # Create a database
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS school")
        cursor.execute("USE school")

        # Create a table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                age INT,
                grade FLOAT
            )
        """)

        
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES ('Alice', 'Smith', 18, 95.5)
        """)

       
        connection.commit()

       
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error setting up database: {e}")

# Function to perform database operations
def perform_database_operations():
    try:
        
        connection = mysql.connector.connect(
            host="your_host",
            user="your_username",
            password="your_password",
            database="school"
        )

        
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO students (first_name, last_name, age, grade)
            VALUES ('Alice', 'Smith', 18, 95.5)
        """)

        
        cursor.execute("""
            UPDATE students
            SET grade = 97.0
            WHERE first_name = 'Alice'
        """)

        
        cursor.execute("""
            DELETE FROM students
            WHERE last_name = 'Smith'
        """)

       
        connection.commit()

       
        cursor.execute("SELECT * FROM students")
        records = cursor.fetchall()
        for record in records:
            print(record)

        
        cursor.close()
        connection.close()

    except Exception as e:
        print(f"Error performing database operations: {e}")


if __name__ == "__main__":
    setup_database()
    perform_database_operations()


