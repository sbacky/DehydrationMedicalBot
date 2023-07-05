-- Create patient table
CREATE TABLE Patient(
	patient_id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	age INT,
	gender VARCHAR(10),
	height INT,
	weight INT
);

-- Create diagnosis table
CREATE TABLE Diagnosis(
	diagnosis_id SERIAL PRIMARY KEY,
	patient_id INT,
	diagnosis VARCHAR(255) NOT NULL,
	FOREIGN KEY (patient_id) REFERENCES Patient(patient_id)
);