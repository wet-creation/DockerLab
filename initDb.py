import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.environ["MYSQL_ROOT_PASSWORD"]
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=db_password,
    database="clinic"
)

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS Stays")
cursor.execute("DROP TABLE IF EXISTS Doctors")
cursor.execute("DROP TABLE IF EXISTS Patients")


cursor.execute("""
CREATE TABLE IF NOT EXISTS Doctors (
    doctor_id INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    specialization ENUM('ent', 'therapist', 'surgeon') NOT NULL,
    experience_years INT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Patients (
    patient_card_number INT AUTO_INCREMENT PRIMARY KEY,
    last_name VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    middle_name VARCHAR(255),
    address TEXT,
    phone_number VARCHAR(15),
    birth_year INT,
    category ENUM('child', 'adult')
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Stays (
    stay_id INT AUTO_INCREMENT PRIMARY KEY,
    patient_card_number INT,
    admission_date DATE,
    stay_days INT,
    daily_cost DECIMAL(10, 2),
    discount_percent DECIMAL(3, 2),
    doctor_id INT,
    FOREIGN KEY (patient_card_number) REFERENCES Patients(patient_card_number),
    FOREIGN KEY (doctor_id) REFERENCES Doctors(doctor_id)
)
""")


cursor.execute("""
INSERT INTO Doctors (last_name, first_name, middle_name, specialization, experience_years)
VALUES 
    ('Smith', 'John', 'Edward', 'ent', 10),
    ('Doe', 'Jane', 'Marie', 'therapist', 7),
    ('Brown', 'Michael', 'James', 'surgeon', 15),
    ('Johnson', 'Emily', 'Louise', 'therapist', 5)
""")

cursor.execute("""
INSERT INTO Patients (last_name, first_name, middle_name, address, phone_number, birth_year, category)
VALUES 
    ('Anderson', 'Alice', 'Patricia', '123 Main St', '1234567890', 2001, 'child'),
    ('White', 'Chris', 'Thomas', '456 Elm St', '2345678901', 1995, 'adult'),
    ('Davis', 'Sophia', 'Maria', '789 Oak St', '3456789012', 1988, 'adult'),
    ('Harris', 'James', 'Charles', '101 Pine St', '4567890123', 2010, 'child'),
    ('Martin', 'Olivia', 'Grace', '102 Maple St', '5678901234', 2003, 'child'),
    ('Clark', 'William', 'Anthony', '103 Cedar St', '6789012345', 1992, 'adult'),
    ('Lewis', 'Ava', 'Elizabeth', '104 Birch St', '7890123456', 1985, 'adult'),
    ('Walker', 'Noah', 'Alexander', '105 Spruce St', '8901234567', 2012, 'child'),
    ('Young', 'Emma', 'Charlotte', '106 Redwood St', '9012345678', 1999, 'adult')
""")

cursor.execute("""
INSERT INTO Stays (patient_card_number, admission_date, stay_days, daily_cost, discount_percent, doctor_id)
VALUES 
    (1, '2023-09-15', 5, 100.00, 0.10, 1),
    (2, '2023-09-16', 3, 80.00, 0.00, 2),
    (3, '2023-09-17', 7, 90.00, 0.15, 3),
    (4, '2023-09-18', 4, 85.00, 0.05, 2),
    (5, '2023-09-19', 6, 75.00, 0.20, 1),
    (6, '2023-09-20', 2, 110.00, 0.00, 3),
    (7, '2023-09-21', 3, 95.00, 0.00, 1),
    (8, '2023-09-22', 5, 120.00, 0.10, 2),
    (9, '2023-09-23', 4, 130.00, 0.05, 3),
    (1, '2023-09-24', 3, 115.00, 0.00, 1),
    (2, '2023-09-25', 2, 125.00, 0.00, 3),
    (3, '2023-09-26', 5, 85.00, 0.10, 2),
    (4, '2023-09-27', 7, 90.00, 0.15, 1),
    (5, '2023-09-28', 4, 100.00, 0.20, 3),
    (6, '2023-09-29', 6, 105.00, 0.05, 2),
    (7, '2023-09-30', 2, 95.00, 0.00, 1),
    (8, '2023-10-01', 3, 80.00, 0.00, 3)
""")



conn.commit()
cursor.close()
conn.close()
