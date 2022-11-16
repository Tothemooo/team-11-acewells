#****Settings****
Documentation:  Move character.  Verify between bountry 
Test_Template:  Move character
Library:  movelibrary.py
test case	                    position-x	position-y	direction_key	eposition-x	eposition-y	move count
move on edge of board east	        5	5	d	6	5	1
Move in middle of board North	    6	5	w	6	6	2
move on edge of board west	        6	6	a	5	6	3
move on edge of board south     	5	6	s	5	5	4
X for Exit 			x	
*** keywords ****
[Arguments]	   {position-x}	{position-y}	{direction_key}	{eposition-x}	{eposition-y}	{move count}
Initialize character position-x with ${position-x}
Initialize character position-y with ${position-y}
Move in direction_key                ${direction_key}
Character xposition should be        ${eposition-x}
Character yposition should be        ${eposition-y}


