from typing import ClassVar, Dict, List
from models.diagnosis import Diagnosis
from models.patient import Patient
from services.diagnosisService import DiagnosisService
from services.patientService import PatientService


class MedicalBot:
    """
    Assess a patients dehydration level: No Dehydration, Some Dehydaration and Severe Dehydration.
    List all patients and their diagnosis.
    Store patients and their diagnosis as a (key, value) pair.

    ```
    def __init__(self) -> None
    ```
    """

    namePrompt: ClassVar[str] = "What is the patient's name?\n"
    agePrompt: ClassVar[str] = "What is the patient's age?\n"
    genderPrompt: ClassVar[str] = "What is the patient's gender?\n"
    heightPrompt: ClassVar[str] = "What is the patient's height?\n"
    weightPrompt: ClassVar[str] = "What is the patient's weight?\n"
    appearancePrompt: ClassVar[str] = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"

    eyePrompt: ClassVar[str] = "How are the patient's eyes?\n - 1: Eyes normal or slightly sunken\n - 2: Eyes very sunken\n"
    skinPrompt: ClassVar[str] = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"

    patientErrorMessage: ClassVar[str] = "Could not save patient information due to invalid input"
    saveErrorMessage: ClassVar[str] = "Could not get patient information at patient ID: "
    diagnosisErrorMessage: ClassVar[str] = "Could not get new diagnosis information"

    severeDehydration: ClassVar[str] = "Severe dehydration"
    someDehydration: ClassVar[str] = "Some dehydration"
    noDehydration: ClassVar[str]= "No dehydration"

    def __init__(self, patientService: PatientService | None = None, diagnosisService: DiagnosisService | None = None) -> None:
        if patientService is None:
            self.patientService: PatientService | None = PatientService()
        else:
            self.patientService = patientService
        
        if diagnosisService is None:
            self.diagnosisService: DiagnosisService | None = DiagnosisService()
        else:
            self.diagnosisService = diagnosisService

    def __assessSkin(self, skin: str) -> str:
        diagnosis: str = ""
        if skin == "1":
            diagnosis = self.someDehydration
        elif skin == "2":
            diagnosis = self.severeDehydration
        return diagnosis

    def __assessEyes(self, eyes: str) -> str:
        diagnosis: str = ""
        if eyes == "1":
            diagnosis = self.noDehydration
        elif eyes == "2":
            diagnosis = self.severeDehydration
        return diagnosis

    def __assessAppearance(self) -> str:
        diagnosis: str = ""
        appearance = input(self.appearancePrompt)
        if appearance == "1":
            eyes = input(self.eyePrompt)
            diagnosis = self.__assessEyes(eyes)
        elif appearance == "2":
            skin = input(self.skinPrompt)
            diagnosis = self.__assessSkin(skin)
        return diagnosis
    
    def __getPatientInfo(self) -> Patient:
        name: str = input(self.namePrompt)
        age: int = int(input(self.agePrompt))
        gender: str = input(self.genderPrompt)
        height: int = int(input(self.heightPrompt))
        weight: int = int(input(self.weightPrompt))
        return Patient(name, age, gender, height, weight)
    
    def __patientCheckIn(self, patientID: int | None) -> Patient:
        patient: Patient | None = None
        if patientID is None:
            patient = self.__getPatientInfo()
        else:
            checkPatient: Patient | None = self.patientService.getPatientByID(patientID)
            if checkPatient is not None:
                patient = checkPatient
            else:
                print(self.patientErrorMessage, patientID)
        return patient
    
    def savePatientAndDiagnosis(self, patient: Patient, diagnosis: Diagnosis) -> bool:
        checkPatient: Patient | None = self.patientService.createPatient(patient)
        if checkPatient is None:
            return False
        diagnosis.patientID = checkPatient.patientID
        checkDiagnosis: Diagnosis = self.diagnosisService.createDiagnosis(diagnosis)
        if checkDiagnosis is None:
            return False
        return True
    
    def listPatientsAndDiagnoses(self) -> None:
        patients: List[Patient] = self.patientService.getAllPatients()
        print("----------")
        print()
        for patient in patients:
            diagnoses: List[Diagnosis] = self.diagnosisService.getDiagnosesByPatientID(patient.patientID)
            print(patient)
            for diagnosis in diagnoses:
                print(diagnosis)
            print()
            print("----------")
            print()

    def newDiagnosis(self, patientID: int | None = None) -> None:
        patient: Patient = self.__patientCheckIn(patientID)
        if patient is None:
            print(self.diagnosisErrorMessage)
            return
        finalDiagnosis: str = self.__assessAppearance()
        diagnosis: Diagnosis = Diagnosis(finalDiagnosis)
        isSaved: bool = self.savePatientAndDiagnosis(patient, diagnosis)
        if isSaved:
            print("Saved!")
        else:
            print(self.saveErrorMessage)