from abc import ABCMeta, abstractmethod
from typing import Collection
from typing import Dict

from apprentice.working_memory.representation import Skill
from apprentice.working_memory.representation import Sai
from jsondiff import diff


class BaseAgent(metaclass=ABCMeta):
    prior_state = {}

    def __init__(self):
        """
        Creates an agent with the provided skills.
        """
        pass

    def request(self, state: Dict) -> Dict:
        """
        Returns a dict containing a Selection, Action, Input.

        :param state: a state represented as a dict (parsed from JSON)
        """
        d = diff(self.prior_state, state)
        self.prior_state = state
        return self.request_diff(d)

    @abstractmethod
    def request_diff(self, state_diff: Dict) -> Dict:
        """
        :param diff: a diff object that is the output of JSON diff
        """
        pass

    def train(self, state: Dict, next_state: Dict, sai: Sai, reward: float,
              skill_label: str, foci_of_attention: Collection[str]):
        """
        Accepts a JSON/Dict object representing the state,
        a JSON/Dict object representing the state after the SAI is invoked,
        a string representing the skill label,
        a list of strings representing the foas,
        a string representation the selection action and inputs,
        a reward
        """
        state_diff = diff(self.prior_state, state)
        next_state_diff = diff(state, next_state)
        self.prior_state = next_state
        return self.train_diff(state_diff, next_state_diff,
                               sai, reward, skill_label, foci_of_attention)

    @abstractmethod
    def train_diff(self, state_diff, next_state_diff, sai, reward,
                   skill_label, foci_of_attention):
        """
        Updates the state by some provided diff, then trains on the provided
        demonstration in this state.
        """
        pass

    @abstractmethod
    def train_last_state(self, sai, reward, skill_label,
                         foci_of_attention):
        """
        Trains on the provided demonstration in the last / current state.
        """
        pass


if __name__ == "__main__":
    pass