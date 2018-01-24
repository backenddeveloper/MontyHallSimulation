#!/usr/bin/env python

from behave import given, then, when
from src.Play import Play
from mock import MagicMock as mock


@given(u'a play')
def a_play(context):
    context.play = Play()


@when(u'one of three doors is chosen')
def door_is_chosen(context):
    context.rng = mock(return_value=0)
    context.play.choose_door(rng=context.rng)


@then(u'this door is randomly chosen using a CSRNG')
def door_is_chosen_securely(context):
    context.rng.assert_called_with(3)
