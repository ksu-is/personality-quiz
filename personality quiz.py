print('Hi player,Welcome to your very own personality quiz!')
print('Let\'s do a quiz to know your personality!!')
print('Answer with (yes, no, sometimes)')
per = 0
persona = ['Why do you keep pushing the no word ', 'You are a rebel who likes to try new things',
           'You are an adventurer who don\'t fear death', 'You have a courageous character', 'You don\'t follow the herd',
           'You like living but want to change your life', 'You are great at loyal to everyone but yourself',
           'You don\'t care about what people say about you', 'You never stop helping your friends, which is your problem',
           'You care about what people say too much', 'You have potiental to suceed',
           'You do not fear darkness']


def ask():
    global per
    per = 0
    Q = ('Do you easliy get mad?', 'Would you say your a out-going person?', 'Do you thrive in high-pressure situations?', 'DO you wake up early?',
         'Are you good at keeping secrets?', 'Do you like following rules ','Are you most likely to be loyal to the ones you love?', 'Are you most likely to standup for your beliefs?',
         'I take care of other people before taking care of myself','I am life of the party','I am skilled on handling awkward situations')
    for i in Q:
        UInp = (input(i))
        if UInp == 'yes':
            per += 2
        elif UInp == 'no':
            per += 0
        else:
            per += 1
    print(persona[per])
    UInp = input('Do you want to play again?')
    if UInp == 'yes':
        ask()
    else:
        quit()


ask()