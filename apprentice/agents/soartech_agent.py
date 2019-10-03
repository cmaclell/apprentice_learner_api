from typing import Collection
from typing import Dict
from random import random

from apprentice.working_memory.representation import Skill
from apprentice.agents.base import BaseAgent


class SoarTechAgent(BaseAgent):
    """
    A SoarTech version of an Apprentice Agent.
    """

    def __init__(self, prior_skills: Collection[Skill]):
        # Just track the state as a set of Facts?
        # initialize to None, so gets replaced on first state.
        self.last_state = None

        # Need a working memory class
        self.working_memory = None
        self.working_memory.add_skills(prior_skills)

    def select_skill(self, candidate_skills: Collection[Skill]) -> Skill:
        """
        Given a list of candidate skills evaluate them and determines which one
        has the highest expected rewared in the current state.

        .. todo::

            Not sure what a state looks like here? Is it just a collection of
                facts?
            Are candidate skills a collection of skills or skill activations?
            Might also need some kind of strategy for choosing, currently just
                choosing best.

        :param candidate_skills: Skills being considered for activation
        """
        # just passing in the working memory facts to each skill, where the
        # facts is just the current state representation.
        skills = [(skill.expected_reward(self.working_memory.facts), random(),
                   skill) for skill in candidate_skills]
        skills.sort(reverse=True)
        expected_reward, _, best_skill = skills[0]
        return best_skill

    def request_diff(self, state_diff: Dict):
        """
        Queries the agent to get an action to execute in the world given the
        diff from the last state.

        :param state_diff: a state diff output from JSON Diff.
        """
        # Just loads in the differences from the state diff
        self.working_memory.update(state_diff)

        # This should do essentially what `engine.run` is doing from
        # PyKnow. Pyknow currently uses salience to choose rule order, but
        # we want to essentially set salience using the when learning.
        while not self.working_memory.output:
            candidate_activations = [activation for activation in
                                     self.working_memory.activations]
            if len(candidate_activations) == 0:
                return {}
            best_activation = self.select_activation(candidate_activations)
            best_activation.fire()

        return self.working_memory.output

    def train(self, state, selection, action, inputs, reward, skill_label,
              foci_of_attention):
        """
        Accepts a JSON object representing the state, a string representing the
        skill label, a list of strings representing the foas, a string
        representing the selection, a string representing the action, list of
        strings representing the inputs, and a boolean correctness.
        """
        if self.last_state is None:
            return self.request_diff(state, [])

        pos_diff = state - self.last_state
        neg_diff = self.last_state - state

        return self.train_diff(pos_diff, neg_diff, selection, action, inputs,
                               reward, skill_label, foci_of_attention)

    def train_diff(self, state_diff, next_state_diff, selection, action,
                   inputs, reward, skill_label, foci_of_attention):
        """
        Need the diff for the current state as well as the state diff for
        computing the state that results from taking the action. This is
        needed for performing Q learning.

        Accepts a JSON object representing the state, a string representing the
        skill label, a list of strings representing the foas, a string
        representing the selection, a string representing the action, list of
        strings representing the inputs, and a boolean correctness.
        """
        # relational inference step?
        self.working_memory.update(state_diff)

        # explain gets access to current state through self.working_memory
        activation_sequence = self.explain(selection, action, inputs)

        if len(activation_sequence) == 1:
            activation = activation_sequence[0]
        else:
            # compile discovered activation seq into new skill and return
            # activation of it
            activation = self.how_learning(activation_sequence)

        # activation has pointers to skill, state context, and match
        # information; still working out what this interface looks like.
        activation.update_where(self.working_memory, reward)
        activation.update_when(self.working_memory, reward, next_state_diff)