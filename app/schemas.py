from pydantic import BaseModel

class SubjectBase(BaseModel):
    name: str
    description: str

class EgePreparation(SubjectBase):
    pass

class AdvancedStudy(SubjectBase):
    pass