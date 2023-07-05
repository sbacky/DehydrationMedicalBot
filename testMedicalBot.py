
from bots.medicalBot import MedicalBot
from models.patient import Patient
from models.diagnosis import Diagnosis


mb: MedicalBot = MedicalBot()

def test_assess_skin() -> None:
    print(mb.__assessSkin("1") == mb.someDehydration)
    print(mb.__assessSkin("2") == mb.severeDehydration)
    print(mb.__assessSkin("3") == "")

def test_assess_eyes() -> None:
    print(mb.__assessEyes("1") == mb.noDehydration)
    print(mb.__assessEyes("2") == mb.severeDehydration)
    print(mb.__assessEyes("3") == "")

def test_assess_appearance() -> None:
    print(mb.__assessAppearance())

def test_save_new_diagnosis() -> None:
    pass

test_assess_skin()
test_assess_eyes()
#test_assess_appearance()
test_save_new_diagnosis()