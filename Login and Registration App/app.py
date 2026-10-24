# from HandleConnection.connection import connect_to_database
import mysql.connector


def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Python_Database",
        port=3306
    )


if __name__ == "__main__":
    connection = None

    try:
        connection = connect_to_database()

        if connection.is_connected():
            print("Connected to MySQL successfully!")

    except mysql.connector.Error as error:
        print("Database connection failed:", error)

    finally:
        if connection and connection.is_connected():
            connection.close()
