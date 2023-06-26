import enum
import pydantic


class StatementEnum(enum.Enum):
    SELECT = enum.auto()
    INSERT = enum.auto()
    UPDATE = enum.auto()
    DELETE = enum.auto()
    UNKNOWN = enum.auto()


class Statement(pydantic.BaseModel):
    type_: StatementEnum = StatementEnum.UNKNOWN


class Expression(pydantic.BaseModel):
    pass
