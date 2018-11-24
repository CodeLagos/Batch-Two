#Business Twist
#A business simulation game
#Created and developed by Ahmed Hassan

#Welcome player
print ('Welcome to Business Twist!')
print ('Business Twist is a business simulation game.')
print ('Experience business life in dialogue form.')
print ('Do you want to play?')
print ('You will need to create a character first.')
char_name=str(input('Enter a character name: '))
print ('Your character name is',char_name)
print ('And throughout this game, you will be called',char_name)


#Start game
#Day #1
#Event #1
def event_1():
 print ('--------DAY #1--------')
 print (char_name+', '+'Liquid Consulting says it is hiring.')
 print ('They are looking for a Python developer.')
 print ('And they think you are a good match for the job.')

#Action #1
def action_1():
 decision_1=str(input('Would you take the job?: '))
 if decision_1.lower()=='yes':
    print ('Great! Your application and resume has been sent to the hiring manager.')
 elif decision_1.lower()=='no':
    print ('Sad! You should take the job to gather some income which you can use to start up your own business.')
    return action_1()
 else:
    print ('Wrong response! Enter Yes or No')
    return action_1()
   

event_1()
action_1()

#Day #2
#Event #2
def event_2():
 print ('--------DAY #2--------')
 print ('The hiring manager at Liquid Consulting finds your resume impressive.')
 print ('One of their clients wants to develop a game for kids.')
 print ('They want you to show up for a meeting at their head office in Yaba by 2pm tomorrow.')

#Action #1
def action_2():
 decision_2=str(input('Would you be able to make it?: '))
 if decision_2.lower()=='yes':
    print ('Nice! Your meeting has been scheduled for 2pm.')
    print ('Liquid Consulting will send you the meeting details later today.')
 elif decision_2.lower()=='no':
    def action_2a():
     decision_2a=str(input('Oh! So unfortunate. What day will be fine for you?: '))
     meeting_days=['MONDAY', 'TUESDAY', 'WEDNESDAY','THURSDAY','FRIDAY', 'SATURDAY', 'SUNDAY']
     if decision_2a.lower()==meeting_days[0].lower() or decision_2a.lower()==meeting_days[1].lower() or decision_2a.lower()==meeting_days[2].lower() or decision_2a.lower()==meeting_days[3].lower() or decision_2a.lower()==meeting_days[4].lower() or decision_2a.lower()==meeting_days[5].lower() or decision_2a.lower()==meeting_days[6].lower():
         print ('Nice! We will schedule your meeting for ',decision_2a+','+'same time.')
     else:
         print ('Wrong response! Enter a valid day.')
         return action_2a()
    action_2a()
 else:
    print ('Wrong response! Enter Yes or No')
    return action_2()
   

event_2()
action_2()

#Game Message
print ('------Get full version to continue game!--------')
print ('Contact developer with info below.')

#Developer info
print ("--------Developer Info--------")
print ('For support, enquiry or sponsorship:')
print ('Call Ahmed Hassan: 09071235558')
print ('Visit website: http://ahmedhassan.com.ng')
