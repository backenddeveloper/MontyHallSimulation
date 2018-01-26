#!/usr/bin/env python

from behave import given, then, when
from src.Play import Play
from mock import MagicMock as mock


@given(u'a play')
def a_play(context):
    context.play = Play()


@when(u'a car is placed behind one of three doors')
def winning_door_is_chosen(context):
    context.rng = mock(return_value=0)
    context.play.place_car(rng=context.rng)


@when(u'a player picks a random door')
def player_picks_a_random_door(context):
    context.rng = mock(return_value=0)
    context.play.pick_random(rng=context.rng)


@when(u'a player picks door number {door:d}')
def player_picks_a_particular_door(context, door):
    context.play.pick(door)


@when(u'a car is placed behind {door:d}')
def car_is_placed_behind_door(context, door):
    context.rng = mock(return_value=door)
    context.play.pick_random(rng=context.rng)


@when(u'a non winning door is revealed')
def non_winning_door_is_revealed(context):
    raise NotImplementedError


@then(u'this door is randomly chosen out of {number_of_doors:d} using a CSRNG')
def door_is_chosen_securely(context, number_of_doors):
    context.rng.assert_called_with(number_of_doors)


@then(u'door {door:d} is saved as the chosen door')
def door_is_chosen(context, door):
    assert context.play.chosen_door == door


@then(u'a {door:d} will be revealed')
def other_door_is_opened(context, door):
    context.play.reveal(door)
    assert door not in context.play.available_doors
