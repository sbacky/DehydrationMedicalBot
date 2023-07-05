
class Diagnosis:
    """
    Class to hold diagnosis information: patientID, diagnosis, diagnosisID
    
    Attributes:
        patientID (```int```): Patient ID referencing patient in patient database.
        diagnosis (```str```): Diagnosis of the patient.
        diagnosisID (```int```): ID given to diagnosis by database.
    """

    def __init__(self, diagnosis: str, patientID: int | None = None, diagnosisID: int | None = None) -> None:
        """
        Constructor for Diagnosis class.

        Attributes:
            patientID (```int```): Patient ID referencing patient in patient database.
            diagnosis (```str```): Diagnosis of the patient.
            diagnosisID (```int```): ID given to diagnosis by database.
        """
        if diagnosisID is not None:
            self.diagnosisID: int | None = diagnosisID
        else:
            self.diagnosisID = None
        self.patientID: int = patientID
        self.diagnosis: str = diagnosis

    def __str__(self) -> str:
        """
        String representation of Diagnosis class.

        Returns:
            str: String representation of this class.
        """
        return f'Diagnosis [diagnosisID = {self.diagnosisID}, patientID = {self.patientID}, diagnosis = {self.diagnosis}]'
    
    def __repr__(self) -> str:
        """
        String representation of Diagnosis class.

        Returns:
            str: String representation of this class.
        """
        return self.__str__()
    
    def __eq__(self, other: object) -> bool:
        """
        Tests for equality between this object, and another object.

        Returns:
            bool: True if the other object is not None, is an instance of this class, and all attributes are equal to this objects attributes. False otherwise.
        """
        if other is None:
            return False
        if not isinstance(other, Diagnosis):
            return False
        return (self.diagnosisID == other.diagnosisID and self.patientID == other.patientID and self.diagnosis == other.diagnosis)
    
    def __hash__(self) -> int:
        """
        Hash representation of this class.

        Returns:
            int: Hash of diagnosisID, patientID and diagnosis.
        """
        return hash((self.diagnosisID, self.patientID, self.diagnosis))