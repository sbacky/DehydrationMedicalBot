
from typing import List
from dao.patientDAO import PatientDAO
from models.patient import Patient


class PatientService:
    """
    Validate input and access DAO.

    Attributes:
        patientDAO (```PatientDAO```): Patient DAO object to access patient information.
    """

    def __init__(self, patientDAO: PatientDAO | None = None):
        """
        Constructor for PatientService class.

        Attributes:
            patientDAO (```PatientDAO```): Patient DAO object to access patient information.
        """
        if patientDAO is None:
            self.patientDAO = PatientDAO()
        else:
            self.patientDAO = patientDAO

    def getAllPatients(self) -> List[Patient]:
        """
        Get a list of all patients in the database.

        Returns:
            (```List```[```Patient```]): A list of all patients in database
        """
        return self.patientDAO.getAllPatients()
    
    def getPatientByID(self, patientID: int) -> Patient | None:
        """
        Get a patient by patientID from the database.

        Parameters:
            patientID (```int```): Patient ID.

        Returns:
            (```Patient | int```): The patient at patient ID or None if no patient is found.
        """
        return self.patientDAO.getPatientByID(patientID)
    
    def createPatient(self, patient: Patient) -> Patient | None:
        """
        Create patient in database if patient.name is not None and patient.name is not "".

        Parameters:
            patient (```Patient``): Patient to add to database.

        Returns:
            (```Patient | None```): The newly created patient with patientID.
        """
        if patient.name is None or patient.name == "":
            return None
        return self.patientDAO.addPatient(patient)
    
    def updatePatient(self, patient: Patient) -> Patient | None:
        """
        Update patient in database if patientID is not None and is for a real, existing patient and patient.name is not None and patient.name is not "".

        Parameters:
            patient (```Patient```): Patient to update in database.

        Returns:
            (```Patient | None```): Updated patient if update is succusful, or None otherwise.
        """
        if self.patientDAO.getPatientByID(patient.patientID) is None:
            return None
        if patient.name is None or patient.name == "":
            return None
        return self.patientDAO.updatePatient(patient)
    
    def deletePatient(self, patientID: int) -> bool:
        """
        Delete patient at patient ID if patient ID is for a real, existing patient.

        Parameters:
            patientID (```int```): Patient ID.

        Returns:
            (```bool```): True if delete is successful, False otherwise.
        """

        if self.patientDAO.getPatientByID(patientID) is None:
            return False
        return self.patientDAO.deletePatient(patientID)