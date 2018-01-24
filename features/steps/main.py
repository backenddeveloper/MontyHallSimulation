#!/usr/bin/env python

from behave import given, then, when
from src.Play import Play
from mock import MagicMock as mock


@given(u'a play')
def a_play(context):
    context.play = Play()


@when(u'a car is placed behind one of three doors')
def door_is_chosen(context):
    context.rng = mock(return_value=0)
    context.play.place_car(rng=context.rng)


@when(u'a player picks a door')
def player_picks_a_door(context):
    context.rng = mock(return_value=0)
    context.play.pick(rng=context.rng)

@then(u'this door is randomly chosen out of {number_of_doors:d} using a CSRNG')
def door_is_chosen_securely(context, number_of_doors):
    context.rng.assert_called_with(number_of_doors)
