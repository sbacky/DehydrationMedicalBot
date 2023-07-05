
from typing import List
from dao.patientDAO import PatientDAO
from models.patient import Patient


class PatientService:

    def __init__(self, patientDAO: PatientDAO | None = None):
        if patientDAO is None:
            self.patientDAO = PatientDAO()
        else:
            self.patientDAO = patientDAO

    def getAllPatients(self) -> List[Patient]:
        return self.patientDAO.getAllPatients()
    
    def getPatientByID(self, patientID: int) -> Patient | None:
        return self.patientDAO.getPatientByID(patientID)
    
    def createPatient(self, patient: Patient) -> Patient | None:
        if patient.name is None or patient.name == "":
            return None
        return self.patientDAO.addPatient(patient)
    
    def updatePatient(self, patient: Patient) -> Patient | None:
        if self.patientDAO.getPatientByID(patient.patientID) is None:
            return None
        if patient.name is None or patient.name == "":
            return None
        return self.patientDAO.updatePatient(patient)
    
    def deletePatient(self, patientID: int) -> bool:
        if self.patientDAO.getPatientByID(patientID) is None:
            return False
        return self.patientDAO.deletePatient(patientID)