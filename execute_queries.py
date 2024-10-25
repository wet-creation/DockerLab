from queries import *

con = connect_to_db()

cursor = con.cursor()

tables = ["Doctors", "Patients", "Stays"]

for table in tables:
    get_table_structure(cursor, table)
    get_table_data(cursor, table)

queries = [
        {
            "query": """
                SELECT last_name, first_name, birth_year 
                FROM Patients 
                WHERE birth_year > 1998 
                ORDER BY last_name;
            """,
            "description": "Пацієнти, народжені після 1998 року"
        },
        {
            "query": """
                SELECT category, COUNT(*) AS patient_count 
                FROM Patients 
                GROUP BY category;
            """,
            "description": "Кількість пацієнтів за категоріями"
        },
        {
            "query": """
                SELECT 
                    p.last_name, p.first_name, s.stay_days, 
                    s.stay_days * s.daily_cost AS total_cost,
                    s.stay_days * s.daily_cost * (1 - s.discount_percent) AS discounted_cost
                FROM Stays s
                JOIN Patients p ON s.patient_card_number = p.patient_card_number;
            """,
            "description": "Сума лікування і сума з урахуванням пільги"
        },
        {
            "query": """
                SELECT 
                    p.last_name AS patient_last_name, 
                    d.last_name AS doctor_last_name, 
                    s.admission_date, s.stay_days
                FROM Stays s
                JOIN Doctors d ON s.doctor_id = d.doctor_id
                JOIN Patients p ON s.patient_card_number = p.patient_card_number
                WHERE d.specialization = 'therapist';
            """,
            "description": "Звернення до лікаря-терапевта"
        },
        {
            "query": """
                SELECT 
                    d.last_name, 
                    COUNT(s.stay_id) AS total_visits
                FROM Stays s
                JOIN Doctors d ON s.doctor_id = d.doctor_id
                GROUP BY d.doctor_id;
            """,
            "description": "Кількість звернень пацієнтів до кожного лікаря"
        },
        {
            "query": """
                SELECT 
                    d.specialization, 
                    p.category, 
                    COUNT(s.stay_id) AS patient_count
                FROM Stays s
                JOIN Doctors d ON s.doctor_id = d.doctor_id
                JOIN Patients p ON s.patient_card_number = p.patient_card_number
                GROUP BY d.specialization, p.category;
            """,
            "description": "Кількість пацієнтів за категоріями і спеціалізаціями лікарів"
        }
    ]

for query in queries:
    execute_query(cursor, query["query"], query["description"])

cursor.close()
con.close()