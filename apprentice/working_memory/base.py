from abc import ABCMeta
from abc import abstractmethod
from typing import Collection
from typing import List
from typing import Dict

from apprentice.working_memory.representation import Skill
from apprentice.working_memory.representation import Activation
from apprentice.working_memory.representation import Fact


class WorkingMemory(metaclass=ABCMeta):
    """
    Abstract base class for working memory
    """

    @abstractmethod
    def update(self, diff: Dict) -> None:
        """
        Updates the working memory based on the provided diff.

        :param diff: a diff object generated by JSON diff
        """
        pass

    @property
    @abstractmethod
    def facts(self) -> Collection[Fact]:
        """
        Get the facts currently in working memory.
        """
        pass

    @property
    @abstractmethod
    def skills(self) -> Collection[Skill]:
        """
        Get the skills currently in working memory.
        """
        pass

    @abstractmethod
    def add_fact(self, fact: Fact) -> None:
        """
        Add a fact to working memory

        :param fact: the fact to be added
        """
        pass

    def add_skills(self, skills: Collection[Skill]) -> None:
        """
        Adds a collection of skills to working memory
        :param skills: skills to be added
        """
        for skill in skills:
            self.add_skill(skill)

    @abstractmethod
    def add_skill(self, skill: Skill) -> None:
        """
        Add a skill to working memory

        :param skill: skill to be added
        """
        pass

    @abstractmethod
    def update_fact(self, fact: Fact) -> None:
        """
        Update a fact in working memory

        :param fact: the updated fact
        """
        pass

    @abstractmethod
    def update_skill(self, skill: Skill) -> None:
        """
        Update a skill in working memory

        :param skill: the updated skill
        """
        pass

    @property
    @abstractmethod
    def activations(self) -> Collection[Activation]:
        """
        Returns the matching rule activations that are being considered.
        """
        pass

    @property
    @abstractmethod
    def output(self) -> object:
        """
        Returns an object; what will ultimately get sent over back as an action.

        .. todo::
            
            Write a setter to set object.
        """
        pass
