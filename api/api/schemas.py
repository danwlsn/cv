import abc
from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime


def _string_to_date(value: str) -> date:
    assert isinstance(value, str), "must be date as str 'YYYY-MM'"
    return datetime.strptime(value, "%Y-%m").date()

class TimeBounded(BaseModel, abc.ABC):
    startDate: date = Field(..., description="The start date")
    endDate: date | None = Field(default=None, description="The end date")

    @field_validator(
        "startDate", mode="before"
    )
    @classmethod
    def string_to_date(
        cls, value: str
    ) -> date:
        return _string_to_date(value)

    @field_validator(
        "endDate", mode="before"
    )
    @classmethod
    def string_to_date_or_none(
        cls, value: str
    ) -> date | None:
        if value == "":
            return None
        return _string_to_date(value)


class Info(BaseModel):
    name: str = Field(..., description="The name of the person")
    headline: str = Field(..., description="The headline of the person")
    phone: str = Field(..., description="The phone number of the person")
    email: str = Field(..., description="The email address of the person")
    summary: str = Field(..., description="A short summary about the person")

class Location(BaseModel):
    region: str = Field(..., description="The region or state")
    country: str = Field(..., description="The country")

class Profile(BaseModel):
    network: str = Field(..., description="The name of the social network")
    username: str = Field(..., description="The username on the social network")
    url: str = Field(..., description="The URL to the profile on the social network")

class Education(TimeBounded):
    institution: str = Field(..., description="The name of the educational institution")
    area: str = Field(..., description="The area of study")
    degree: str = Field(..., description="The type of degree obtained")
    score: str = Field(..., description="The GPA achieved")
    courses: list[str] = Field(..., description="List of relevant courses")

class Work(TimeBounded):
    name: str = Field(..., description="The name of the company")
    position: str = Field(..., description="The job title or position held")
    url: str = Field(..., description="The company's website")
    summary: str = Field(..., description="A brief summary of the job role and responsibilities")
    keywords: list[str] = Field(..., description="List of key achievements or highlights in the role")

class Skill(BaseModel):
    name: str = Field(..., description="The name of the skill category")
    level: str = Field(..., description="The proficiency level in the skill category")
    keywords: list[str] = Field(..., description="List of specific skills or technologies")

class Certificate(BaseModel):
    name: str = Field(..., description="The name of the certificate")
    date: str = Field(..., description="The date the certificate was obtained")
    issuer: str = Field(..., description="The organization that issued the certificate")
    url: str = Field(..., description="The URL to the certificate or issuing organization")

class Project(TimeBounded):
    name: str = Field(..., description="The name of the project")
    description: str = Field(..., description="A brief description of the project")
    keywords: list[str] = Field(..., description="List of technologies or skills used in the project")
    summary: str = Field(..., description="A short summary about the person")

class Interest(BaseModel):
    name: str = Field(..., description="The name of the interest or hobby")
    keywords: list[str] = Field(..., description="List of related keywords or activities")

class Volunteer(TimeBounded):
    organization: str = Field(..., description="The name of the volunteer organization")
    position: str = Field(..., description="The position held during volunteering")
    url: str = Field(..., description="The organization's website")
    summary: str = Field(..., description="A brief summary of the volunteer role and responsibilities")

class FullResume(BaseModel):
    basics: Info
    location: Location
    profiles: list[Profile]
    education: list[Education]
    work: list[Work]
    skills: list[Skill]
    certificates: list[Certificate]
    projects: list[Project]
    interests: list[Interest]
    volunteer: list[Volunteer]

class ErrorMessage(BaseModel):
    detail: str = Field(..., description="The error message detail")
