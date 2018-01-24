#!/usr/bin/env python

from random import SystemRandom


class Play:

    def choose_door(self, rng=SystemRandom.randrange):
        self.door = rng(3)
