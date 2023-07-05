
from typing import List
from dao.diagnosisDAO import DiagnosisDAO
from dao.patientDAO import PatientDAO
from models.diagnosis import Diagnosis


class DiagnosisService:

    def __init__(self, diagnosisDAO: DiagnosisDAO | None = None, patientDAO: PatientDAO | None = None) -> None:
        if diagnosisDAO is None:
            self.diagnosisDAO = DiagnosisDAO()
        else:
            self.diagnosisDAO = diagnosisDAO

        if patientDAO is None:
            self.patientDAO = PatientDAO()
        else:
            self.patientDAO = patientDAO

    def getAllDiagnoses(self) -> List[Diagnosis]:
        return self.diagnosisDAO.getAllDiagnosis()
    
    def getDiagnosesByPatientID(self, patientID: int) -> List[Diagnosis] | None:
        if self.patientDAO.getPatientByID(patientID) is None:
            return None
        return self.diagnosisDAO.getDiagnosesByPatientID(patientID)
    
    def getDiagnosisByID(self, diagnosisID: int) -> Diagnosis | None:
        return self.diagnosisDAO.getDiagnosisByID(diagnosisID)
    
    def createDiagnosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        if self.patientDAO.getPatientByID(diagnosis.patientID) is None:
            return None
        if diagnosis.diagnosis == "" or diagnosis.diagnosis is None:
            return None
        return self.diagnosisDAO.addDignosis(diagnosis)
    
    def updateDiagnosis(self, diagnosis: Diagnosis) -> Diagnosis | None:
        if self.patientDAO.getPatientByID(diagnosis.patientID) is None:
            return None
        if diagnosis.diagnosis == "" or diagnosis.diagnosis is None:
            return None
        if self.diagnosisDAO.getDiagnosisByID(diagnosis.diagnosisID) is None:
            return None
        return self.diagnosisDAO.updateDiagnosis(diagnosis)
    
    def deleteDiagnosis(self, diagnosisID: int) -> bool:
        if self.diagnosisDAO.getDiagnosisByID(diagnosisID) is None:
            return False
        return self.diagnosisDAO.deleteDiagnosis(diagnosisID)