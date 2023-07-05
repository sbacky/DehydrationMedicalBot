
from bots.medicalBot import MedicalBot

welcomePrompt: str = "Welcome doctor, what would you like to do?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"
patientTypePrompt: str = "Is this a new patient or returning patient?\n - New patient, press 1\n - Returning patient, press 2\n"
patientIDPrompt: str = "Please enter patient ID:\n"

def main() -> None:
    medicalbot: MedicalBot = MedicalBot()
    while True:
        selection: str = input(welcomePrompt)
        if selection == "1":
            # List all patients
            medicalbot.listPatientsAndDiagnoses()
        elif selection == "2":
            patientType = input(patientTypePrompt)
            if patientType == "1":
                # Start new diagnoses
                medicalbot.newDiagnosis()
            elif patientType == "2":
                patientID: int = int(input(patientIDPrompt))
                medicalbot.newDiagnosis(patientID)
        elif selection == "q":
            return

main()
