from dataclasses import dataclass

# Goal is to be able to compare race against race, performance against performance, and athlete against athlete.
# Race against race allows for comparison between conditions, thus providing a score to compare performances.
# Performance against performance allows for comparison between individual capabilities, thus providing a score to compare athletes.
# Athlete against athlete then is the goal to predict race performance between competitors.

@dataclass
class Race:
    name         : str
    distance     : int
    id           : int
    link         : list
    athletes     : list
    performances : list

@dataclass
class Performance:
    distance : int
    id       : int
    time     : int
    place    : int

@dataclass
class Athlete:
    name         : str
    id           : int
    link         : str
    performances : list