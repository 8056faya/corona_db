
import mysql.connector

# Connect to the MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    #password="fayaz22@",  # Enter your MySQL password here if required
    database="corona_db"
)

cursor = db.cursor()

try:
    # Create a new patient record
    insert_query = "INSERT INTO patients (name, age) VALUES (%s, %s)"
    data = ("abu", 85)
    cursor.execute(insert_query, data)
    db.commit()

    # Read patient records
    select_query = "SELECT * FROM patients"
    cursor.execute(select_query)
    patients = cursor.fetchall()
    for patient in patients:
        print(patient)

    # Update a patient's record
    update_query = "UPDATE patients SET age = %s WHERE name = %s"
    data = (40, "John Doe")
    cursor.execute(update_query, data)
    db.commit()

    # Delete a patient's record
    delete_query = "DELETE FROM patients WHERE name = %s"
    data = ("John Doe",)
    cursor.execute(delete_query, data)
    db.commit()

except mysql.connector.Error as err:
    print("MySQL Error: {}".format(err))

finally:
    # Close the database connection
    db.close()
