***Settings***
Documentation   I want to move my character. If they attempt to move past a boundary, the move results in no change in position.
Test Template   Move character
Library         Move.library.py

*** Test Cases ***	                Character	S_Position_X	S_Position_Y	S_Move_Count	Direction	E_Position_X	E_Position_Y	E_Move_Count
Move east from initial position	    Fred	    5	            5	            0	            D	        6	            5	            1
Move north from (6,5)	            Fred	    6	            5	            1	            W	        6	            6	            2
Move west from (6, 6)	            Fred	    6	            6	            2	            A	        5	            6	            3
Move south from (5, 6)	            Fred	    5	            6	            3	            S	        5	            5	            4
Move east from (10, 10)	            Anne	    10	            10	            50	            D	        10	            10	            51
Move north from (5, 10)	            Raja	    5	            10	            50	            W	        5	            10	            51
Move west from (1, 1)	            Amy	        1	            1	            40	            A	        1	            1	            41

*** Keywords ***
Move character
    [Arguments]     ${Character}     ${S_Position_X}     ${S_Position_Y}     ${S_Move_Count}     ${Direction}        ${E_Position_X}     ${E_Position_Y}     ${E_Move_Count}
    Initialize character name with ${Character}
    Initialize character x positon with ${S_Position_X}
    Initialize character y position with ${S_Position_Y}
    Initialize move count with ${S_Move_Count}
    Move in direction ${Direction}
    Character x position should be ${E_Position_X}
    Character y position should be ${E_Position_Y}
    Character move count should be ${E_Move_Count}

    ***add pictures later***

