import uuid
from dataclasses import dataclass
from typing import Collection, Callable, Any

from experta.conditionalelement import ConditionalElement as Condition


# class Condition(tuple):
#     def __new__(cls, *args):
#         return tuple.__new__(Condition, args)


# class Fact(dict):
#     def __new__(cls, *args):
#         return dict.__new__(Fact, args)

@dataclass
class Sai:
    selection: Any
    action: Any
    input: Any


@dataclass
class Skill:
    conditions: Collection[Condition]
    function_: Callable
    #name: str = "skill_" + str(uuid.uuid1())


@dataclass
class Activation:
    skill: Skill
    context: dict

    @property
    def fire(self) -> Any:
        raise NotImplementedError
