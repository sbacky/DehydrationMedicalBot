
from typing import Any, ClassVar, List
import psycopg
from models.patient import Patient

from utils import connectionUtil


class PatientDAO:
    """
    Access patient information in the database and return as a patient object. Save patient information in the database by passing in patient object.

    Attributes:
        (```class```) conn (```psycopg.Connection | None```): Connection to the database or None if no connection or connection was closed.
        (```class```) cursor (```psycopg.Cursor | None```): Cursor to perform actions on database and return data from database or None if no cursor or cursor was closed.
    """

    conn: ClassVar[psycopg.Connection | None] = None
    cursor: ClassVar[psycopg.Cursor | None] = None

    def __init__(self) -> None:
        """
        Constructor for PatientDAO class.
        """
        pass

    def getAllPatients(self) -> List[Patient]:
        """
        Get all patient information from the database.

        Returns:
            (```List```[```Patient```]): List of all patients and their information as patient objects. If database is empty, return empty list.
        """
        patientList: List[Patient] = []

        try:
            PatientDAO.conn = connectionUtil.getConnection()
            PatientDAO.cursor = PatientDAO.conn.cursor()

            sql: str = """SELECT * FROM patient;"""
            PatientDAO.cursor.execute(sql)

            rs: List[tuple[Any, ...]] = PatientDAO.cursor.fetchall()
            for tup in rs:
                patientID: int; patientName: str; patientAge: int; patientGender: str; patientHeight: int; patientWeight: int
                patientID, patientName, patientAge, patientGender, patientHeight, patientWeight = tup

                patient: Patient = Patient(patientName, patientAge, patientGender, patientHeight, patientWeight, patientID)

                patientList.append(patient)
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()

        return patientList

    def getPatientByID(self, patientID: int) -> Patient | None:
        """
        Get paitient by patientID.

        Parameters:
            patientID (```int```): Patient ID.

        Returns:
            (```Patient | None```): patient object or None
        """
        patient: Patient | None = None

        try:
            PatientDAO.conn = connectionUtil.getConnection()
            PatientDAO.cursor = PatientDAO.conn.cursor()

            sql: str = """SELECT * FROM patient WHERE patient_id = %s;"""
            PatientDAO.cursor.execute(sql, (patientID,))

            rs: List[tuple[Any, ...]] = PatientDAO.cursor.fetchall()
            if len(rs) > 1:
                return patient
            for tuple in rs:
                patient_ID: int; patientName: str; patientAge: int; patientGender: str; patientHeight: int; patientWeight: int
                patient_ID, patientName, patientAge, patientGender, patientHeight, patientWeight = tuple
                patient = Patient(patientName, patientAge, patientGender, patientHeight, patientWeight, patient_ID)

        except Exception as e:
            print(e)
        finally:
            self.__closeResources()

        return patient
    
    def addPatient(self, patient: Patient) -> Patient | None:
        """
        Add patient to database.

        Parameters:
            patient (```Patient```): Patient object (No patientID!) to add to database.
            
        Returns:
            (```Patient```): Patient object with patientID from database.
        """
        patientName: str = patient.name
        patientAge: int = patient.age
        patientGender: str = patient.gender
        patientHeight: int = patient.height
        patientWeight: int = patient.weight

        try:
            PatientDAO.conn = connectionUtil.getConnection()
            PatientDAO.cursor = PatientDAO.conn.cursor()

            sql: str = """INSERT INTO patient(name, age, gender, height, weight) VALUES (%s, %s, %s, %s, %s) RETURNING *;"""
            PatientDAO.cursor.execute(sql, (patientName, patientAge, patientGender, patientHeight, patientWeight))

            if PatientDAO.cursor.rowcount > 0:
                patientID: int = PatientDAO.cursor.fetchone()[0]
                patient.patientID = patientID
                print(patient)
                return patient
            else:
                return None

        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        
        return None

    def updatePatient(self, patient: Patient) -> Patient | None:
        """
        Update patient in database.

        Parameters:
            patient (```Patient```): Patient and their information to update in database.

        Returns:
            (```Patient | None```): Updated patient if update was successful or None otherwise.
        """
        patientName: str = patient.name
        patientAge: int = patient.age
        patientGender: str = patient.gender
        patientHeight: int = patient.height
        patientWeight: int = patient.weight
        patientID: int = patient.patientID

        try:
            PatientDAO.conn = connectionUtil.getConnection()
            PatientDAO.cursor = PatientDAO.conn.cursor()

            sql: str = """UPDATE patient SET name = %s, age = %s, gender = %s, height = %s, weight = %s WHERE patient_id = %s RETURNING *;"""
            PatientDAO.cursor.execute(sql, (patientName, patientAge, patientGender, patientHeight, patientWeight, patientID))

            checkPatient: tuple[Any, ...] | None = PatientDAO.cursor.fetchone()
            
            if checkPatient is not None:
                patient.patientID, patient.name, patient.age, patient.gender, patient.height, patient.weight = checkPatient
                return patient
            else:
                return None
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        
        return None

    def deletePatient(self, patientID: int) -> bool:
        """
        Delete patient at patientID in database.

        Parameters:
            patientID (```int```): Patient ID.

        Returns:
            (```bool```): True if patient at patient ID was deleted, False otherwise.
        """
        try:
            PatientDAO.conn = connectionUtil.getConnection()
            PatientDAO.cursor = PatientDAO.conn.cursor()

            sql: str = """DELETE FROM patient WHERE patient_id = %s;"""
            PatientDAO.cursor.execute(sql, (patientID,))

            rowCount: int = PatientDAO.cursor.rowcount
            if rowCount > 0:
                return True
            else:
                return False
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        return False

    def __closeResources(self) -> None:
        """
        Close cursor and conn resources if they are open.
        """
        try:
            if PatientDAO.cursor is not None:
                PatientDAO.cursor.close()
        except Exception as e:
            print(e)

        try:
            if PatientDAO.conn is not None:
                PatientDAO.conn.close()
        except Exception as e:
            print(e)

