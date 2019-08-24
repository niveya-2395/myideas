from decimal import Decimal

def quizgame():


    correct = 0
    incorrect = 0
    total = 0

    reply = raw_input('Are you ready to play the game? Y/N')

    if reply == 'Y':
        ans1 = raw_input('1.) I am an odd number. Take away one letter and I become even. What number am I??')
        total+=1
        if ans1 == 'seven' or ans1 == 'Seven' or ans1 == '7':
            print 'correct'
            correct+= 1
        else:
            print 'incorrect'
            incorrect += 1

        ans2 = raw_input('2.) A man said:The day before yesterday I was only 25 and next year I will turn 28.This is true only one day in a year - when was he born?')
        total += 1
        if ans2 == 'December31' or ans2 == 'December 31st' or ans2 == '31-12':
            print 'correct'
            correct += 1
        else:
            print 'incorrect'
            incorrect += 1

        ans3 = raw_input('3.) What comes in place of question mark (?) in the following series, WE SG PJ LN?')
        total += 1
        if ans3 == 'IS' or ans3 == 'IS':
            print 'correct'
            correct += 1
        else:
            print 'incorrect'
            incorrect += 1

        ans4 = raw_input('4.) In a certain code INKER is written as GLLGT and GLIDE is written as EJJFG. How will JINKS be written in that code?')
        total += 1
        if ans4 == 'HGOMU':
            print 'correct'
            correct += 1
        else:
            print 'incorrect'
            incorrect += 1

        ans5 = raw_input('5.) If AND is written as EQF and THE as XKG then how will COM be written?')
        total += 1
        if ans5 == 'GRO':
            print 'correct'
            correct += 1
        else:
            print 'incorrect'
            incorrect += 1

        score = Decimal(correct)/Decimal(total)
        print score
        if score>=0.5:
            result = 'pass'
        else:
            result = 'fail'

        print 'Your score = ',correct
        print 'You', result + 'ed','with a grade of',score*100,'%'
        print 'Thank you for playing, goodbye'

    else:
        print 'Thanks for choosing the quiz game, please come again'





quizgame()
