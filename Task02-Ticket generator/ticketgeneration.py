while True:
    try:
        age=int(input('What is your age?: '))          #Asking user for age
        if age<1 or age>150:                           
            print('Write your age between 1 and 150')  #asking user to enter age between 1 and 150 
            continue
    except ValueError:                                 #if user enters age in string literals
        print('Write your age in wholenumbers')        #asking user to enter age in wholenumbers
        continue
    else:
        break
while True:
    student=input('Are you a student? Yes/No: ').strip().lower()       #asking whether user is student or not and cleaning the input like removing the capitalization and accidental spaces
    is_student = (student=='yes')
    if student !='yes' and student != 'no':                     #if user enters answer other than yes or no
        print('Write your Answer in Yes or No')               #asking user to enter answer in yes or no 
        continue
    else:
        break
if age>=1 and age<=17:                                     #Ticket generation for child group
    if is_student:                                   #if child is student
        print('Your Ticket price is 200')
    else:                                                   #if child is non student
        print('Your Ticket price is 300')

elif age>=18 and age<=59:                                     #Ticket generation for adult group
    if is_student:                                    #if adult is student
        print('Your Ticket price is 400')
    else:                                                   #if adult is non student
        print('Your Ticket price is 500')

elif age>=60:                                                 #Ticket generation for Senior
    if is_student:                                    #if senior is student
        print('Your Ticket price is 600')
    else:                                                   #if senior is non student
        print('Your Ticket price is 700')


while True:
    try:
        score=int(input('Enter Your Score: '))              #asking user for scores
        if score<0 or score>100:                             
            print('Write your score between 0 and 100')      #asking user to enter scores between 0 and 100
            continue
    except ValueError:
        print('Write your score in wholenumbers')            #asking user to enter scores in wholenumbers
        continue
    else:
        break
if score>=90 and score<=100:              #grade calculation in range of 90 and 100
    print('Your Grade is A')
elif score>=80 and score<=89:             #grade calculation in range of 80 and 89
    print('Your Grade is B')
elif score>=70 and score<=79:             #grade calculation in range of 70 and 79
    print('Your Grade is C')
elif score>=60 and score<=69:             #grade calculation in range of 60 and 69
    print('Your Grade is D')
elif score>=50 and score<=59:             #grade calculation in range of 50 and 59
    print('Your Grade is E')
else:                                     #grade calculation for 49 or less scores
    print('Your Grade is F')
   
   

