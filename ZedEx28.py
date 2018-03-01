#!/bin/env/python

#Exercise 28

print """
My Answers:
1. True and True				 ==> the and makes this logical phrase TRUE
2. False and True 				==> the and makes this logical phrase FALSE
3. 1 == 1 and 2 == 1 				==> 1==1 returns TRUE but 2==1 returns FALSE, with and, logical phrase is FALSE
4. "test" == "test" 				==> two terms are equivalent, therefore TRUE
5. 1 == 1 or 2 != 1 				==> 1 is 1; 2 is not 1, since both are TRUE, logical phrase is TRUE
6. True and 1 == 1 				==> 1==1 is TRUE, therefore TRUE and TRUE are TRUE
7. False and 0 != 0 				==> 0!=0 is FALSE, therefore FALSE and FALSE are FALSE
8. True or 1 == 1				==> 1 == 1 is TRUE, therefore TRUE or TRUE is TRUE
9. "test" == "testing"				==> "test" is not the same as "testing" therefore FALSE
10. 1 != 0 and 2 == 1				==> 1!=0 is TRUE, but 2==1 is FALSE, therefore TRUE and FALSE are FALSE 
11. "test" != "testing"				==>"test" is not the same as "testing" therefore TRUE
12. "test" == 1					==> I'm not sure with this one off the bat...methinks b/c test is not 1 FALSE?
13. not (True and False)			==> True and False is FALSE, so not is returning the opposite; TRUE
14. not (1 == 1 and 0 != 1)			==> 1==1 is TRUE, 0!=1 is TRUE, but not is returning the opposite; FALSE
15. not (10 == 1 or 1000 == 1000)		==> 10==1 is FALSE, and 1000==1000 is TRUE, and even though the or returns TRUE, the not returns FALSE
16. not (1 != 10 or 3 == 4)			==> 1!=10 is TRUE, and 3==4 is FALSE, and even though the or returns TRUE, the not returns FALSE

   
17. not ("testing" == "testing" and "Zed" == "Cool Guy")		==> "testing" == "testing" TRUE; "Zed" == "Cool Guy"; FALSE; not(TRUE and FALSE); TRUE
18. 1 == 1 and not ("testing" == 1 or 1 == 0)				==> 1 == 1 TRUE and not ("testing" == 1 or 1 == 0); TRUE and not(FALSE or FALSE); TRUE
19. "chunky" == "bacon" and not (3 == 4 or 3 == 3)			==>"chunky" == "bacon" FALSE and not (3 == 4 or 3 == 3); FALSE and not(FALSE or TRUE);FALSE 
20. 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")	==>3 == 3 and not ("testing" == "testing" or "Python" == "Fun");T and not(T or F);FALSE  
"""
