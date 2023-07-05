
from bots.medicalBot import MedicalBot

welcomePrompt = "Welcome doctor, what would you like to do?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

def main() -> None:
    medicalbot: MedicalBot = MedicalBot()
    while True:
        selection = input(welcomePrompt)
        if selection == "1":
            # List all patients
            medicalbot.listPatientsAndDiagnoses()
        elif selection == "2":
            # Start new diagnoses
            medicalbot.newDiagnosis()
        elif selection == "q":
            return

main()
