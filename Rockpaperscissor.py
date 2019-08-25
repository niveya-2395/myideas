									
	def SPSgame():								
									
	    choice1 = raw_input("Stone, paper or scissor?")								
	    choice2 = raw_input("Stone, paper or scissor?")								
									
									
	    list1 = ['scissor','paper']								
	    list2 = ['stone','scissor']								
	    list3 = ['paper','stone']								
	    list =  [list1,list2,list3]								
	    choice = [choice1,choice2]								
	    choicerev = choice[::-1]								
									
	    for i in list:								
	        if choicerev == i:								
	            print "User 2 wins"								
	        elif choice == i:								
	            print "User 1 wins"								
	    if choice1==choice2:								
	        print "Tie"								
									
	    result = int(input("Do you want to continue? press 0 for yes and 1 for no"))								
	    if result == 0:								
	        SPSgame()								
									
									
	SPSgame()								
									
