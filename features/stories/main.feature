Feature: A simulation of the Monty Hall problem
    This repeats the game over and over repeatedly
    And returns statistics on the outcome
    In order to settle a bet with a cute but wrong young lady

Scenario: It chooses A cryptographically secure random number
    Given a play
    When a car is placed behind one of three doors
    Then this door is randomly chosen out of 3 using a CSRNG

Scenario: When a first door is chosen it is chosen randomly
    Given a play
    When a player picks a random door
    Then this door is randomly chosen out of 3 using a CSRNG

Scenario Outline: When a first door is chosen it is removed from the pool
    Given a play
    When a player picks door number <door>
    Then door <door> is removed from the available doors

    Examples: Door numbers to test
    | door |
    | 0    |
    | 1    |
    | 2    |
