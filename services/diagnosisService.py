
from typing import List
from dao.diagnosisDAO import DiagnosisDAO
from dao.patientDAO import PatientDAO
from models.diagnosis import Diagnosis


class DiagnosisService:
    """
    Validate input and access DAO.

    Attributes:
        diagnosisDAO (```DiagnosisDAO```): Diagnosis DAO object to access diagnosis information.
        patientDAO (```PatientDAO```): Patient DAO object to access patient information.
    """

    def __init__(self, diagnosisDAO: DiagnosisDAO | None = None, patientDAO: PatientDAO | None = None) -> None:
        """
        Consturctor for DiagnosisService class.

        Attributes:
            diagnosisDAO (```DiagnosisDAO```): Diagnosis DAO object to access diagnosis information.
            patientDAO (```PatientDAO```): Patient DAO object to access patient information.
        """
        if diagnosisDAO is None:
            self.diagnosisDAO = DiagnosisDAO()
        else:
            self.diagnosisDAO = diagnosisDAO

        if patientDAO is None:
            self.patientDAO = PatientDAO()
        else:
            self.patientDAO = patientDAO

    def getAllDiagnoses(self) -> List[Diagnosis]:
        """
        Get a list of all diagnosies in the database.

        Returns:
            (```List```[```Diagnosis```]): A list of all diagnoses in database.
        """
        return self.diagnosisDAO.getAllDiagnosis()
    
    def getDiagnosesByPatientID(self, patientID: int) -> List[Diagnosis] | None:
        """
        Get a list of all diagnoses for patientID if patientID is for a real, existing patient, in the database.

        Parameters:
            patientID (```int```): Patient ID.

        Returns:
            (```List```[```Diagnosis```]): List of diagnoses for patientID.
        """
        if self.patientDAO.getPatientByID(patientID) is None:
            return None
        return self.diagnosisDAO.getDiagnosesByPatientID(patientID)
    
    def getDiagnosisByID(self, diagnosisID: int) -> Diagnosis | None:
        """
        Get a diagnosis by diagnosisID from the database.

        Parameters:
            diagnosisID (```int```): Diagnosis ID

        Returns:
            (```Diagnosis | None```): The diagnosis at diagnosis ID or None if no diagnosis is found.
        """
        return self.diagnosisDAO.getDiagnosisByID(diagnosisID)
    
    def createDiagnosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        """
        Create diagnosis in database if patient ID is for a real existing patient and diagnosis.diagnosis is not None and not "".

        Parameters:
            diagnosis (```Diagnosis```): Diagnosis to add to database.

        Returns:
            (```Diagnosis | None```): The newly created diagnosis with diagnosisID.
        """
        if self.patientDAO.getPatientByID(diagnosis.patientID) is None:
            return None
        if diagnosis.diagnosis == "" or diagnosis.diagnosis is None:
            return None
        return self.diagnosisDAO.addDignosis(diagnosis)
    
    def updateDiagnosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        """
        Update diagnosis in database if patient ID is for a real, existing patient, diangosis ID is for a real, existing diagnosis, and diagnosis.diagnosis

        Parameters:
            diagnosis (```Diagnosis```): Diagnosis to update in database.

        Returns:
            (```Diagnosis```): Updated diagnosis if update is successful, or None otherwise.
        """
        if self.patientDAO.getPatientByID(diagnosis.patientID) is None:
            return None
        if diagnosis.diagnosis == "" or diagnosis.diagnosis is None:
            return None
        if self.diagnosisDAO.getDiagnosisByID(diagnosis.diagnosisID) is None:
            return None
        return self.diagnosisDAO.updateDiagnosis(diagnosis)
    
    def deleteDiagnosis(self, diagnosisID: int) -> bool:
        """
        Delete diagnosis at diagnosis ID if diagnosis ID is for a real, existing diagnosis.

        Parameters:
            diangosisID (```int```): Diagnosis ID.

        Returns:
            (```bool```): True if delete is successful, False otherwise.
        """
        if self.diagnosisDAO.getDiagnosisByID(diagnosisID) is None:
            return False
        return self.diagnosisDAO.deleteDiagnosis(diagnosisID)