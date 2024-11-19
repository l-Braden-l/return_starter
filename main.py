#Braden Leach
#Nov 19 2024
#Return Statement Practice



    #Project 1 
def describe_vacation(destination,activity,season='Summer'):
#first function call
    description1 = f'The place you are travling is {destination}, during the {season} season. You are going to {activity} while you are there.' 
    return description1
print(describe_vacation('Germany','ride your bike'))  

#second function call
def describe_vacation(destination,activity,season='summer'):
#first function call
    description2 = f'The place you are travling is {destination}, during the {season} season. You are going to {activity} while you are there.\n' 
    return description2
print(describe_vacation('Paris','go out to eat',season='Spring'))  


    #Project 2 
def show_major(first_name,university,major='Sports Medicine'):
    return f'{first_name} attends the {university} and is majoring in {major}'
print(show_major('Carl','Michigan Tech University',major='Computer Science'))
print(show_major('Carl','Michigan Tech University'))


