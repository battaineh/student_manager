import sqlite3

def connect_db():
    try:
        return sqlite3.connect("students.db")
    except sqlite3.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            age INTEGER,
                            grade TEXT)''')
        conn.commit()
        print("Table created successfully.")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        conn.close()

def add_student(name, age, grade):
    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO students (name, age, grade) VALUES (?, ?, ?)''', (name, age, grade))
        conn.commit()
        print("Student added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding student: {e}")
    finally:
        conn.close()

def view_students():
    conn = connect_db()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        students = cursor.fetchall()
        return students
    except sqlite3.Error as e:
        print(f"Error viewing students: {e}")
        return []
    finally:
        conn.close()

def update_student(id, name, age, grade):
    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
        student = cursor.fetchone()

        if student:
            cursor.execute('''UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?''', (name, age, grade, id))
            conn.commit()
            print(f"Student with ID {id} updated successfully.")
        else:
            print(f"Student with ID {id} not found. Update not performed.")
    except sqlite3.Error as e:
        print(f"Error updating student: {e}")
    finally:
        conn.close()

def delete_student(id):
    conn = connect_db()
    if conn is None:
        return
    
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students WHERE id = ?", (id,))
        student = cursor.fetchone()

        if student:
            cursor.execute("DELETE FROM students WHERE id = ?", (id,))
            conn.commit()
            print(f"Student with ID {id} deleted successfully.")
        else:
            print(f"Student with ID {id} not found. No student was deleted.")
    except sqlite3.Error as e:
        print(f"Error deleting student: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    create_table()  # Create the table if it doesn't exist
