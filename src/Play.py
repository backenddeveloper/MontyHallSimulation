#!/usr/bin/env python

from random import SystemRandom


class Play:

    def __init__(self):
        self.available_doors = [0,1,2]

    def place_car(self, rng=SystemRandom.randrange):
        self.winning_door = rng(3)

    def pick_random(self, rng=SystemRandom.randrange):
        self.pick(rng(3))

    def pick(self, door):
        self.available_doors.remove(door)
