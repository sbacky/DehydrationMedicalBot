
from typing import Any, ClassVar, List
import psycopg
from dao.patientDAO import PatientDAO

from models.diagnosis import Diagnosis
from utils import connectionUtil


class DiagnosisDAO:

    conn: ClassVar[psycopg.Connection | None] = None
    cursor: ClassVar[psycopg.Cursor | None] = None

    def __init__(self) -> None:
        pass

    def getAllDiagnosis(self) -> List[Diagnosis]:
        diagnosisList: List[Diagnosis] = []
        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """SELECT * FROM diagnosis;"""
            DiagnosisDAO.cursor.execute(sql)

            rs: List[tuple[Any, ...]] = DiagnosisDAO.cursor.fetchall()
            for tup in rs:
                diagnosisID: int; patientID: int; finalDiagnosis: str
                diagnosisID, patientID, finalDiagnosis = tup

                diagnosis: Diagnosis = Diagnosis(finalDiagnosis, patientID, diagnosisID)

                diagnosisList.append(diagnosis)

        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        return diagnosisList

    def getDiagnosesByPatientID(self, patientID: int) -> List[Diagnosis]:
        diagnosisList: List[Diagnosis] = []
        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """SELECT * FROM diagnosis WHERE patient_id = %s;"""
            DiagnosisDAO.cursor.execute(sql, (patientID,))

            rs: List[tuple[Any, ...]] = DiagnosisDAO.cursor.fetchall()
            for tup in rs:
                diagnosisID: int; patient_ID: int; finalDiagnosis: str
                diagnosisID, patient_ID, finalDiagnosis = tup

                diagnosis: Diagnosis = Diagnosis(finalDiagnosis, patient_ID, diagnosisID)

                diagnosisList.append(diagnosis)

        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        return diagnosisList

    def getDiagnosisByID(self, diagnosisID: int) -> Diagnosis | None:
        diagnosis: Diagnosis | None = None
        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """SELECT * FROM diagnosis WHERE diagnosis_id = %s;"""
            DiagnosisDAO.cursor.execute(sql, (diagnosisID,))

            rs: List[tuple[Any, ...]] = DiagnosisDAO.cursor.fetchall()
            if len(rs) > 1:
                return diagnosis
            for tup in rs:
                diagnosis_ID: int; patient_ID: int; finalDiagnosis: str
                diagnosis_ID, patient_ID, finalDiagnosis = tup

                diagnosis = Diagnosis(finalDiagnosis, patient_ID, diagnosis_ID)
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()

        return diagnosis

    def addDignosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        patientID: int = diagnosis.patientID
        finalDiagnosis: str = diagnosis.diagnosis

        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """INSERT INTO diagnosis(patient_id, diagnosis) VALUES (%s, %s) RETURNING *;"""
            DiagnosisDAO.cursor.execute(sql, (patientID, finalDiagnosis))

            if DiagnosisDAO.cursor.rowcount > 0:
                diagnosisID: int = DiagnosisDAO.cursor.fetchone()[0]
                diagnosis.diagnosisID = diagnosisID
                return diagnosis
            else:
                return None
            
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()
        
        return None

    def updateDiagnosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        patientID: int = diagnosis.patientID
        finalDiagnosis: str = diagnosis.diagnosis
        diagnosisID: int = diagnosis.diagnosisID

        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """UPDATE diagnosis SET patient_id = %s, diagnosis = %s WHERE diagnosis_id = %s RETURNING *;"""
            DiagnosisDAO.cursor.execute(sql, (patientID, finalDiagnosis, diagnosisID))

            checkDiagnosis: tuple[Any, ...] | None = DiagnosisDAO.cursor.fetchone()

            if checkDiagnosis is not None:
                diagnosis.diagnosisID, diagnosis.patientID, diagnosis.diagnosis = checkDiagnosis
                return diagnosis
            else:
                return None
        except Exception as e:
            print(e)
        finally:
            self.__closeResources()

        return None

    def deleteDiagnosis(self, diagnosisID: int) -> bool:
        try:
            DiagnosisDAO.conn = connectionUtil.getConnection()
            DiagnosisDAO.cursor = DiagnosisDAO.conn.cursor()

            sql: str = """DELETE FROM diagnosis WHERE diagnosis_id = %s;"""
            DiagnosisDAO.cursor.execute(sql, (diagnosisID,))

            rowCount: int = DiagnosisDAO.cursor.rowcount
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
        try:
            if DiagnosisDAO.cursor is not None:
                DiagnosisDAO.cursor.close()
        except Exception as e:
            print(e)

        try:
            if DiagnosisDAO.conn is not None:
                DiagnosisDAO.conn.close()
        except Exception as e:
            print(e)