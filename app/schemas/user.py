from dataclasses import dataclass

# Use Case Inputs/Outputs

@dataclass
class UserCreateUseCaseInput:
    email: str
    password: str


@dataclass
class UserCreateUseCaseOutput:
    id: str
    email: str
    is_active: bool

# Repository Inputs

@dataclass
class UserCreateInput:
    email: str
    password_hash: str


@dataclass
class UserUpdateInput:
    email: str
    is_active: bool
