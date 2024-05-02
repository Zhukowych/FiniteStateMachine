"""Finite State machine of my life implementation"""
from random import random


class State:
    """State"""

    SLEEP = 0
    AWAKE = 1
    EAT = 2
    DRINK_COFFEE = 3
    STUDY = 4
    READ = 5
    WALK = 6



def handler(fsm) -> State:
    """Force change state if hungry or sleepy"""

    if fsm.state != State.SLEEP:
        fsm.sleep_level -= 1
        fsm.food_level -= 0.8

    if fsm.sleep_level < -20 and fsm.state != State.SLEEP:
        return State.SLEEP

    if fsm.food_level < 3:
        return State.EAT


def sleep_handler(fsm) -> State:
    """Handle sleep state""" 
    print('ZzZzZzZ...zZ')

    fsm.sleep_level += 3
    if random() > fsm.sleep_level / 8:
        return State.SLEEP
    else:
        return State.AWAKE

def awake_handler(fsm) -> State:
    """Handle awake state"""
    print("Oh! what to do?")
    return State.DRINK_COFFEE

def eat_handler(fsm) -> State:
    """Handle eat state"""
    print("Eat in trapezna")
    fsm.food_level = 10

    if random() > 0.6:
        return State.READ

    if random() > 0.5:
        return State.WALK

    return State.STUDY


def drink_coffee_handler(fsm) -> State:
    """Handle drink coffee state"""
    print("Drinking coffee!!!")

    if random() > 0.7:
        return State.WALK

    if random() > 0.4:
        return State.STUDY

    return State.READ


def study_handler(fsm) -> State:
    """Handle study state"""

    print("Studying...")
    fsm.exhausting_level += 1

    if fsm.exhausting_level > 10 * random():
        return State.WALK
    else:
        return State.STUDY


def read_handler(fsm) -> State:
    """Handle read state"""
    fsm.exhausting_level = 0
    print("Reading...")

    if random() > 0.2:
        return State.WALK
    elif random() > 0.5:
        return State.SLEEP
    else:
        return State.DRINK_COFFEE


def walk_handler(fsm) -> State:
    """Handle walk state"""
    print("Walking in Stryiskyi Park")
    fsm.exhausting_level = max(0, fsm.exhausting_level - 1)
    return State.STUDY


class FiniteStateMachine:
    """Finite state machine"""

    HANDLERS = {
        State.SLEEP: sleep_handler,
        State.AWAKE: awake_handler,
        State.EAT: eat_handler,
        State.DRINK_COFFEE: drink_coffee_handler,
        State.STUDY: study_handler,
        State.READ: read_handler,
        State.WALK: walk_handler,
    }

    def __init__(self) -> None:
        """Initialize FiniteStateMachine"""

        self.hour = 0
        self.state = State.SLEEP

        self.sleep_level = 0
        self.food_level = 10
        self.exhausting_level = 0


    def next_state(self):
        """Get the next state """

        self.hour += 1
        self.hour %= 24

        forced_state = handler(self)

        if forced_state is not None:
            self.state = forced_state
        self.state = self.HANDLERS[self.state](self)


if __name__ == "__main__":
    fsm = FiniteStateMachine()

    for _ in range(48):
        fsm.next_state()
