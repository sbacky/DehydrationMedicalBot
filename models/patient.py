
class Patient:
    """
    Class to hold patient information: name, age, gender, height, weight, patientID.

    Attributes:
        name (```str```): Name of the patient.
        age (```int```): Age of the patient.
        gender (```str```): Gender of the patient.
        height (```int```): Height of the patient in inches.
        weight (```int```): Weight of the patient in lbs.
        patientID (```int | None```): ID given to patient by database.
    """

    def __init__(self, name: str, age: int, gender: str, height: int, weight: int, patientID: int | None = None) -> None:
        """
        Constructor for Patient class.

        Parameters:
            name (```str```): Name of the patient.
            age (```int```): Age of the patient.
            gender (```str```): Gender of the patient.
            height (```int```): Height of the patient in inches.
            weight (```int```): Weight of the patient in lbs.
            patientID (```int | None```): ID given to patient by database.
        """
        if patientID is not None:    
            self.patientID: int | None = patientID
        else:
            self.patientID = None
        self.name: str = name
        self.age: int = age
        self.gender: str = gender
        self.height: int = height
        self.weight: int = weight
    
    def __str__(self) -> str:
        """
        String representation of Patient class.

        Returns:
            str: The string representation of this class.
        """
        return f'{self.name} [patientID = {self.patientID}, age = {self.age}, gender = {self.gender}, height = {self.height}, weight = {self.weight}]'
    
    def __repr__(self) -> str:
        """
        String representation of Patient class.

        Returns:
            str: The string representation of this class.
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
        if not isinstance(other, Patient):
            return False
        return (self.patientID == other.patientID and self.name == other.name and self.age == other.age and self.gender == other.gender and self.height == other.height and self.weight == other.weight)
    
    def __hash__(self) -> int:
        """
        Hash representation of this class.

        Returns:
            int: Hash of name, age, gender, height, and weight.
        """
        return hash((self.name, self.age, self.gender, self.height, self.weight))
    
