from pydantic import BaseModel


class Terraform(BaseModel):
    project_name: str


class UserVariables(BaseModel):
    terraform: Terraform