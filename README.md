# Dehydration Medical Bot

Diagnose a users hydration with a quick questionnaire. Will be yes/no questions. Responses determine next question. Returns severe dehydration/some dehydration/no dehydration

Retrieve and add dehydration diagnoses. Display list of patients and diagnoses. Store new patients and diagnoses in database.

Fully functioning Deyhydration medical diagnosis bot with a complete backend in python. Uses Psycopg3+ to connect to a PostgreSQL database.

Add config.ini file under resources/ folder and add configurations for dbname, user, password, host, and port for your PostgreSQL database. utils.connectionUtil will use configurations set in config.ini file to connect to database.

Run sql code in sql files under resources/ to create tables and insert test data into tables. Easily modify number of fields, just need to modify DAO to accpet the modified number of fields. Changing Patient.name and Diagnosis.diagnosis will result in having to modify PatientService or DiagnosisService. The services check for those fields will creating and updating patients and diagnoses.
