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

Scenario Outline: When a first door is chosen it is noted
    Given a play
    When a player picks door number <door>
    Then door <door> is saved as the chosen door

    Examples: Door numbers to test
    | door |
    | 0    |
    | 1    |
    | 2    |

Scenario Outline: Another door will be opened
    Given a play
    When a car is placed behind <winning_door>
    And a player picks door number <chosen_door>
    Then a <non_winning_door> will be revealed

    Examples:
    | winning_door | chosen_door | non_winning_door |
    | 0            | 0           | 1                |
    | 0            | 1           | 2                |
    | 0            | 2           | 1                |
    | 1            | 0           | 2                |
    | 1            | 1           | 0                |
    | 1            | 2           | 0                |
    | 2            | 0           | 1                |
    | 2            | 1           | 0                |
    | 2            | 2           | 0                |
