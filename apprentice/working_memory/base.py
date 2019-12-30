from abc import ABCMeta
from abc import abstractmethod
from typing import Any
from typing import Callable
from typing import Collection
from typing import Dict

import jsondiff
from apprentice.working_memory.representation import Activation
from apprentice.working_memory.representation import Skill


class WorkingMemory(metaclass=ABCMeta):
    """
    Abstract base class for working memory
    """

    def build_skill(self, _condition: Any,
                    _function: Callable) -> Skill:
        return self.skill_factory.build(_condition, _function)

    def update(self, diff: Dict) -> None:
        """
        Updates the working memory based on the provided diff.

        :param diff: a diff object generated by JSON diff

        """
        for k, v in diff.items():
            if k is jsondiff.symbols.replace:
                for f in self.facts.values():
                    self.remove_fact(f)
                for f in v.values():
                    self.add_fact(f)
            elif k is jsondiff.symbols.delete:
                for k2 in v.values():
                    self.remove_fact(k2)
            else:
                self.add_fact(k)

    @property
    @abstractmethod
    def facts(self) -> Collection[dict]:
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

    def add_facts(self, facts: Collection[dict]) -> None:
        for fact in facts:
            self.add_fact(fact)

    @abstractmethod
    def add_fact(self, fact: dict) -> None:
        """
        Add a fact to working memory

        :param fact: the fact to be added
        """
        pass

    @abstractmethod
    def remove_fact(self, fact: dict) -> bool:
        """
        Remove a fact from working memory

        :param fact: the fact to be added
        :returns false if fact does not exist, true if successfully removed
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
    def update_fact(self, fact: dict) -> None:
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
        Returns an object; what will ultimately get sent over back as an
        action.

        .. todo::
            
            Write a setter to set object.
        """
        pass

    @abstractmethod
    def run(self):
        """
            update KE/perform inference (under what conditions?)
        """
        pass

    @abstractmethod
    def step(self):
        """
            update KE/perform inference for one step (what is one step?)
        """
        pass