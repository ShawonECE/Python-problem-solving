import random

file = open("goals.txt")
list_goal = []
scorers_list = []


for line in file:
    x = list(map(str, line.split(';')))
    x.pop()
    list_goal.append(x)
file.close()

def country_goals(country):
    count = 0
    for i in range(len(list_goal)):
        if list_goal[i][1] == country:
            count = count + 1
    print(country, "scores", count, "times")

def player_goals(player):
    count = 0
    for i in range(len(list_goal)):
        if list_goal[i][0] == player:
            count = count + 1
    print(player, "scores", count, "times")
    
def scorers(country):
    for i in range(len(list_goal)):
        if list_goal[i][1] == country:
            if list_goal[i][0] not in scorers_list:
                scorers_list.append(list_goal[i][0])
    scorers_list.remove("OG")            
    print("Scorer for", country, ": ", scorers_list)

def total_goals():
    print("Total goals: ", len(list_goal))

def first_half_goals():
    count = 0
    for i in range(len(list_goal)):
        if int(list_goal[i][2]) <= 45:
            count = count + 1
    print("First half goals: ", count)

def second_half_goals():
    count = 0
    for i in range(len(list_goal)):
        if int(list_goal[i][2]) in range(45, 91):
            count = count + 1
    print("Second half goals: ", count)

def extra_time_goals():
    count = 0
    for i in range(len(list_goal)):
        if int(list_goal[i][2]) > 90:
            count = count + 1
    print("Extra time goals: ", count)

def team_goals_list():
    teams = []
    goals = []
    for i in range(len(list_goal)):
        if list_goal[i][1] not in teams:
            teams.append(list_goal[i][1])
    for j in range(len(teams)):
        count = 0
        for k in range(len(list_goal)):
            if list_goal[k][1] == teams[j]:
                count = count + 1
        goals.append(count)
    
    print('Team goals list: ')
    print(dict(zip(teams, goals)))  

def top_scorer_team():
    teams = []
    goals = []
    max = 0
    ind = 0
    for i in range(len(list_goal)):
        if list_goal[i][1] not in teams:
            teams.append(list_goal[i][1])
    for j in range(len(teams)):
        count = 0
        for k in range(len(list_goal)):
            if list_goal[k][1] == teams[j]:
                count = count + 1
        goals.append(count)
    for m in range(len(goals)):
        if goals[m] > max:
            max = goals[m]
            ind = m
    print("Top scorer team: ", teams[ind])

def top_scorer_player():
    players = []
    per_goals = []
    max = 0
    ind = 0
    OG_ind = 0
    for i in range(len(list_goal)):
        if list_goal[i][0] not in players:
            players.append(list_goal[i][0])
    for j in range(len(players)):
        count = 0
        for k in range(len(list_goal)):
            if list_goal[k][0] == players[j]:
                count = count + 1
        per_goals.append(count)
    for n in players:
        if n == 'OG':
            OG_ind = players.index(n)
            players.pop(OG_ind)
    per_goals.pop(OG_ind)
    for m in range(len(per_goals)):
        if per_goals[m] > max:
            max = per_goals[m]
            ind = m
    print("Top scorer player: ", players[ind])

def quiz():
    teams = []
    goals = []
    max = 0
    ind = 0
    for i in range(len(list_goal)):
        if list_goal[i][1] not in teams:
            teams.append(list_goal[i][1])
    for j in range(len(teams)):
        count = 0
        for k in range(len(list_goal)):
            if list_goal[k][1] == teams[j]:
                count = count + 1
        goals.append(count)
    ran = random.sample(teams, k =2)
    for item in ran:
        for team in teams:
            if team == item:
                ind = teams.index(team)
                if goals[ind] > max:
                    max = goals[ind]
                    indx = ind
    more_goal = teams[indx]
            
    print("Which team scored more goals? ", ran)
    inp = input("Give your answer: ")
    if more_goal == inp:
        print("Your answer is correct")
    else:
        print("Your answer is incorrect.", more_goal, "scored more goals.")      


print("Enter A to get total number of goals scored by a given country ")
print("Enter B to get total number of goals scored by a given player")
print("Enter C to get list of the name of all the players who scored for a given country")
print("Enter D to get total number of goals by all countries")
print("Enter E to get total number of goals scored during the first half")   
print("Enter F to get total number of goals scored during the second half")
print("Enter G to get total number of goals scored during extra time")
print("Enter H to get list the total number of goals scored for each country")
print("Enter I to get which country scored the most goals")
print("Enter J to get which player scored the most goals")
print("Enter K to participate in quiz")

choice = input("Enter your choice: ")
if choice == 'A':
    country = input("Enter the country: ")
    country_goals(country)
elif choice == 'B':
    player = input("Enter the player: ")
    player_goals(player)
elif choice == 'C':
    country = input("Enter the country: ")
    scorers(country)
elif choice == 'D':
    total_goals()
elif choice == 'E':
    first_half_goals()
elif choice == 'F':
    second_half_goals()
elif choice == 'G':
    extra_time_goals()
elif choice == 'H':
    team_goals_list()
elif choice == 'I':
    top_scorer_team()
elif choice == 'J':
    top_scorer_player()
elif choice == 'K':
    quiz()
else:
    print("Invalid choice")
    
    
    
     




    
            
