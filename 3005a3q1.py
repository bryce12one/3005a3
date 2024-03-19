import psycopg2

# database connection parameters
dbname = 'school'
user = 'brycei' # replace user value with your PostgreSQL username
password = 'postgres' # replace password value with your PostgreSQL password

host = 'localhost'

# establish connection to database
conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)

# creating cursor object
cur = conn.cursor()

def getAllStudents():
    # retrieves and displays all records from the students table
    cur.execute('SELECT * FROM students')
    rows = cur.fetchall()
    for row in rows:
        print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    # inserts a new student record into the students table
    cur.execute('INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)',
                (first_name, last_name, email, enrollment_date))
    conn.commit()
    print('Student added successfully.')

def updateStudentEmail(student_id, new_email):
    # updates the email address for a student with the specified student_id
    cur.execute('UPDATE students SET email = %s WHERE student_id = %s', (new_email, student_id))
    conn.commit()
    print('Email updated successfully.')

def deleteStudent(student_id):
    # deletes the record of the student with the specified student_id
    cur.execute('DELETE FROM students WHERE student_id = %s', (student_id,))
    conn.commit()
    print('Student deleted successfully.')

# examples
# getAllStudents()
# addStudent('Alice', 'Yin', 'alice.yin@email.com', '2023-05-27')
# updateStudentEmail(20, 'sam.samuel@email.com')
# deleteStudent(17)
getAllStudents()

# closing cursor and connection
cur.close()
conn.close()
