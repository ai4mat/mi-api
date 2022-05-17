# generated by datamodel-codegen:
#   filename:  schema_db.json
#   timestamp: 2022-04-19T08:23:29+00:00

from __future__ import annotations
from datetime import date, datetime
from enum import Enum
from bson.objectid import ObjectId

from typing import Annotated, List, Union, Optional, Type
import inspect
import json
from pydantic import BaseModel, Field, validator
from pydantic.class_validators import root_validator
from fastapi import Form


class ObjectIdStr(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        try:
            return ObjectId(v)
        except Exception:
            raise ValueError(f"{v} is not a valid ObjectId")
        return str(v)


class UpdatedAt(BaseModel):
    _date: Optional[str] = datetime.now().utcnow()


class User(BaseModel):
    email: str
    affiliation: str


class Project(BaseModel):
    name: str
    description: str
    label: str


class Parameter(BaseModel):
    name: str
    type: str
    value: float


class SwAgent(BaseModel):
    name: str
    version: str


class Calculation(BaseModel):
    method: str
    swAgent: SwAgent


class SwAgent1(BaseModel):
    name: str
    version: str


class Experiment(BaseModel):
    method: str
    swAgent: SwAgent1


class ChemicalCompositionItem(BaseModel):
    element: str
    percentage: str


class Lattice(BaseModel):
    a: str
    b: str
    c: str
    alpha: str
    beta: str
    gamma: str


class Input(BaseModel):
    lattice: Lattice
    sites: str
    species: str


class Lattice1(BaseModel):
    a: str
    b: str
    c: str
    alpha: str
    beta: str
    gamma: str


class Output(BaseModel):
    lattice: Lattice1
    sites: str
    species: str


class Material(BaseModel):
    formula: str
    elements: List[Union[str, str]]
    chemicalComposition: List[ChemicalCompositionItem]
    input: Input
    output: Output


class Axis(BaseModel):
    labelX: str
    labelY: str


class Units(BaseModel):
    x: str
    y: str


class CreatedAt1(BaseModel):
    _date: str = Field(alias="$date")


class UpdatedAt1(BaseModel):
    _date: str = Field(alias="$date")


class PropertyFile(BaseModel):
    name: str = Field(default="")
    hash: Optional[str]
    extention: Optional[str]
    size: Optional[str]
    createdAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]
    updatedAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]


class Property(BaseModel):
    name: str
    type: str
    # axis: Axis
    value: float
    # units: Units
    file: Optional[PropertyFile]
    isCalculated: bool
    isPhysical: bool


class Process(BaseModel):
    isExperiment: bool
    isSimulation: bool
    parameters: List[Parameter]
    calculation: Calculation
    experiment: Experiment
    material: Material
    properties: List[Property]
    iemapID: str


class CreatedAt2(BaseModel):
    _date: str = Field(..., alias="$date")


class UpdatedAt2(BaseModel):
    _date: str = Field(..., alias="$date")


class Publication(BaseModel):
    name: str
    date: datetime
    url: Optional[str]

    class Config:
        validate_assignment = True

    @validator("date", pre=True, always=True)
    def _set_publication_date_type(cls, date: datetime):
        result = datetime.strptime(date, "%Y-%M-%d") or date
        return result


class fileType(Enum):
    Code = "Code"
    Tabular = "Tabular"
    Image = "Image"
    Raw_Inst_Data = "Raw Instrument Data"

    @staticmethod
    def from_str(label):
        if label in "code":
            return fileType.Code
        if label in "tabular":
            return fileType.Tabular
        if label in "image":
            return fileType.Image
        if label in "raw inst data":
            return fileType.Raw_Inst_Data
        else:
            raise NotImplementedError


class FileProject(BaseModel):
    hash: str
    description: str
    name: str
    extention: str
    type: fileType
    isProcessed: bool
    size: Optional[str]
    createdAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]
    updatedAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]
    publication: Optional[Publication]

    class Config:
        use_enum_values = True


def validate_datetime(cls, values):
    """
    Reusable validator for pydantic models
    """
    return values or datetime.now().utcnow()


class newProject(BaseModel):

    createdAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]
    updatedAt: Annotated[
        datetime, Field(default_factory=lambda: datetime.now().utcnow())
    ]
    user: User
    project: Project
    projectWP: str
    process: Process
    files: Optional[List[FileProject]] = None
    _v: Optional[str] = Field(default="1_0")

    class Config:
        validate_assignment = True


# def as_form(cls: Type[BaseModel]):
#     new_parameters = []

#     for field_name, model_field in cls.__fields__.items():
#         model_field: ModelField  # type: ignore

#         new_parameters.append(
#             inspect.Parameter(
#                 model_field.alias,
#                 inspect.Parameter.POSITIONAL_ONLY,
#                 default=Form(...)
#                 if not model_field.required
#                 else Form(model_field.default),
#                 annotation=model_field.outer_type_,
#             )
#         )

#     async def as_form_func(**data):
#         return cls(**data)

#     sig = inspect.signature(as_form_func)
#     sig = sig.replace(parameters=new_parameters)
#     as_form_func.__signature__ = sig  # type: ignore
#     setattr(cls, "as_form", as_form_func)
#     return cls


def as_form(cls: Type[BaseModel]):
    new_parameters = []

    for field_name, model_field in cls.__fields__.items():
        model_field: ModelField  # type: ignore

        if not model_field.required:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(model_field.default),
                    annotation=model_field.outer_type_,
                )
            )
        else:
            new_parameters.append(
                inspect.Parameter(
                    model_field.alias,
                    inspect.Parameter.POSITIONAL_ONLY,
                    default=Form(...),
                    annotation=model_field.outer_type_,
                )
            )

    async def as_form_func(**data):
        return cls(**data)

    sig = inspect.signature(as_form_func)
    sig = sig.replace(parameters=new_parameters)
    as_form_func.__signature__ = sig  # type: ignore
    setattr(cls, "as_form", as_form_func)
    return cls


@as_form
class PropertyForm(BaseModel):
    name: str
    type: str
    axis_labelX: str
    axis_labelY: str
    value: float
    units_x: str
    units_y: str
    isCalculated: bool
    isPhysical: bool


@as_form
class ProjectFileForm(BaseModel):
    name: str
    description: str
    type: str
    isProcessed: str
    publication_name: Optional[str] = ""
    publication_date: Optional[str] = None
    publication_url: Optional[str] = ""

    # class Config:
    #     validate_assignment = True

    # @validator("publication_date", pre=True, always=True)
    # def _set_publication_date_type(cls, publication_date: datetime):
    #     return publication_date.to or datetime(publication_date)


# https://stackoverflow.com/questions/63616798/pydantic-how-to-pass-the-default-value-to-a-variable-if-none-was-passed
# https://github.com/samuelcolvin/pydantic/issues/1593
