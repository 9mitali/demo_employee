class EmployeeModel:
    def __init__(self, Department, Name, Designation, Email, Address, location, DOB, DOJ, id_proof_type, id_proof, Gender, Phone, Country, Salary):
        self.Department = Department
        self.Name = Name
        self.Designation = Designation
        self.Email = Email
        self.Address = Address
        self.location = location
        self.DOB = DOB
        self.DOJ = DOJ
        self.id_proof_type = id_proof_type
        self.id_proof = id_proof
        self.Gender = Gender
        self.Phone = Phone
        self.Country = Country
        self.Salary = Salary

    @classmethod
    def from_dict(cls, data):
        return cls(
            Department=data.get('Department'),
            Name=data.get('Name'),
            Designation=data.get('Designation'),
            Email=data.get('Email'),
            Address=data.get('Address'),
            location=data.get('location'),
            DOB=data.get('DOB'),
            DOJ=data.get('DOJ'),
            id_proof_type=data.get('id_proof_type'),
            id_proof=data.get('id_proof'),
            Gender=data.get('Gender'),
            Phone=data.get('Phone'),
            Country=data.get('Country'),
            Salary=data.get('Salary')
        )
