***Settings***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         MoveLibrary.py

*** Test Cases ***	               	x_position	y_position	S_Move_Count	Direction	E_Position_X	E_Position_Y	E_Move_Count
Move east from initial position	    5	            5	            0	    EAST	      6	            5	            1
Move north from (6,5)	            6	            5	            1	    NORTH         6	            6	            2
Move west from (6, 6)	            6	            6	            2	    WEST          5	            6	            3
Move south from (5, 6)	            5	            6	            3	    SOUTH	      5	            5	            4
Move east from (10, 10)	            10	            10	            50	    EAST          10	        10	            51
Move north from (5, 10)	            5	            10	            50	    NORTH	      5	            10	            51
Move west from (1, 1)	            1	            1	            40	    WEST	      1	            1	            41

*** Keywords ***
Move character
    [Arguments]     ${x_position}     ${y_position}     ${S_Move_Count}     ${Direction}        ${E_Position_X}     ${E_Position_Y}     ${E_Move_Count}
    Initialize character x position with    ${x_position}
    Initialize character y position with    ${y_position}
    #Initialize move count with  ${S_Move_Count}
    Move in direction   ${Direction}
    Character x position should be  ${E_Position_X}
    Character y position should be  ${E_Position_Y}
    Character move count should be  ${E_Move_Count}

    ***add pictures later***

