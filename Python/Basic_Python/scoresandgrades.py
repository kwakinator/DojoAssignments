import random

def scores_grades(num):
    print "Scores and Grades"
    for i in range(0,num):
        score = random.randint(60,101)
        if score <=69 and score >=60:
            result = "D"
        elif score <=79 and score >=70:
            result = "C"
        elif score <=89 and score >=80:
            result = "B"
        else:
            result = "A"
        print "Score: {}; Your grade is {}".format(score,result)
    print "End of program. Bye!"

scores_grades(10)
