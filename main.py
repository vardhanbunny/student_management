import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")
conn.commit()

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    cursor.execute(
        "INSERT INTO students (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )
    conn.commit()
    print("✅ Student added successfully!")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("⚠️ No records found.")
    else:
        print("\nID | Name | Age | Course")
        print("-" * 30)
        for row in rows:
            print(row[0], "|", row[1], "|", row[2], "|", row[3])

# Update student
def update_student():
    id = int(input("Enter student ID to update: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    if cursor.fetchone() is None:
        print("❌ Student not found.")
        return

    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    course = input("Enter new course: ")

    cursor.execute(
        "UPDATE students SET name=?, age=?, course=? WHERE id=?",
        (name, age, course, id)
    )
    conn.commit()
    print("✅ Student updated successfully!")


def delete_student():
    id = int(input("Enter student ID to delete: "))

    cursor.execute("SELECT * FROM students WHERE id=?", (id,))
    if cursor.fetchone() is None:
        print("❌ Student not found.")
        return

    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    print("✅ Student deleted successfully!")


def search_student():
    name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("⚠️ No matching records.")
    else:
        for row in rows:
            print(row)

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        search_student()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")

conn.close()
