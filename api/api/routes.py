from datetime import date as Date
from typing import Annotated

from fastapi import APIRouter, Depends

from api import schemas, models, utils

ROUTER = APIRouter()


CV = Annotated[schemas.FullResume, Depends(models.load_cv)]

@ROUTER.get("/")
async def full(cv: CV) -> schemas.FullResume:
    """
    Return all the content from the CV
    """
    return cv

@ROUTER.get("/info")
async def info(cv: CV) -> schemas.Info:
    """
    Return the basic information from the CV
    """
    return cv.basics

@ROUTER.get("/location")
async def location(cv: CV) -> schemas.Location:
    """
    Return location information from the CV
    """
    return cv.location

@ROUTER.get("/profile")
async def profile_list(cv: CV) -> list[schemas.Profile]:
    """
    Return a list of profiles from the CV
    """
    return cv.profiles

@ROUTER.get("/profile/{network}", responses={404: {"model":schemas.ErrorMessage}})
async def profile_detail(network: str, cv: CV) -> schemas.Profile:
    """
    Return a specific profile from the CV based on the network name
    """
    for profile in cv.profiles:
        if profile.network.lower() == network.lower():
            return profile

    raise HTTPException(status_code=404, detail="Profile not found")

@ROUTER.get("/project")
async def project_list(cv: CV) -> list[schemas.Project]:
    """
    Return a list of projects from the CV
    """
    return cv.projects

@ROUTER.get("/education")
async def education_list(cv: CV) -> list[schemas.Education]:
    """
    Return a list of education entries from the CV
    """
    return cv.education

@ROUTER.get("/work", responses={404: {"model":schemas.ErrorMessage}})
async def work_list(cv: CV, date: Date | None = None) -> list[schemas.Work]:
    """
    Return a list of places worked at from the CV
    """
    works = cv.work
    if date is None:
        return works

    output = []
    for work in works:
        if utils.date_between_dates(date, work.startDate, work.endDate):
            output.append(work)

    if output:
        return output

    raise HTTPException(status_code=404, detail="Work not found for date")

@ROUTER.get("/skill", responses={404: {"model":schemas.ErrorMessage}})
async def skill_list(cv: CV, q: str | None = None) -> list[schemas.Skill]:
    """
    Return a list of skills from the CV. Optional q query paramater to search for a specific skill
    """
    skills = cv.skills
    if q is None:
        return skills

    output = []

    for skill in skills:
        if q.lower() in [kw.lower() for kw in skill.keywords]:
            output.append(skill)

    if output:
        return output

    raise HTTPException(status_code=404, detail="Skill not found")


@ROUTER.get("/interest")
async def interest_list(cv: CV) -> list[schemas.Interest]:
    """
    Return a list of interests from the CV
    """
    return cv.interests

@ROUTER.get("/volunteer")
async def volutneer_list(cv: CV) -> list[schemas.Volunteer]:
    """
    Return a list of volunteering opportunities from the CV
    """
    return cv.volunteer
