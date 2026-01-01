import json
from datetime import datetime
from collections import deque
import math
from core.models import User, SocialNetwork
from core.algorithms.traversal import find_communities as find_communities_new
## Соцсеть, инициализация юзера
class User():
    id = 0
    def __init__(self, name, age, country, hobbies, friends, joined, nationality):
        self.id = User.id
        User.id += 1 
        self.name = name
        self.joined = joined
        self.age = age
        self.nationality = nationality
        self.country = country
        self.hobbies = hobbies
        self.friends = friends



u1 = User("Alex Aguerro", 20, "Brazil", ["MMA", "SPORTS", "COOKING"], [], datetime.now(), "Portuguese")
u2 = User("Alex Maj", 35, "Mongolia", ["SPORTS", "MOVIES"], [u1], datetime.now(), "Mongolian")
u3 = User("Sakura Ito", 27, "Japan", ["ANIME", "TECH", "MUSIC"], [u1, u2], datetime.now(), "Japanese")
u4 = User("Daniel Fischer", 31, "Germany", ["CYCLING", "BEER", "SOCCER"], [u1], datetime.now(), "German")
u5 = User("Mila Petrova", 24, "Bulgaria", ["READING", "DANCING"], [u3], datetime.now(), "Bulgarian")
u6 = User("Zhang Wei", 29, "China", ["GAMING", "ESPRESSO", "PHOTOGRAPHY"], [u2, u4], datetime.now(), "Chinese")
u7 = User("Ayan Aitzhan", 22, "Kazakhstan", ["BOXING", "GYM", "TEA"], [u1, u5], datetime.now(), "Kazakh")
u8 = User("Nora Lund", 33, "Sweden", ["YOGA", "TRAVEL", "BAKING"], [u3, u6, u7], datetime.now(), "Swedish")
u9 = User("Carlos Mendes", 26, "Portugal", ["SURFING", "FOOTBALL", "WINE"], [u4, u8], datetime.now(), "Portuguese")
u10 = User("Fatima Al-Hariri", 28, "Jordan", ["PAINTING", "HIKING"], [u7, u9], datetime.now(), "Arabic")
u11 = User("Liam O'Connell", 30, "Ireland", ["PUB QUIZZES", "HURLING"], [u2, u9], datetime.now(), "English")
u12 = User("Helena Santos", 19, "Spain", ["K-POP", "SOCIAL MEDIA"], [u1, u3, u10], datetime.now(), "Spanish")
u13 = User("Armin Reza", 34, "Iran", ["FITNESS", "CARS"], [u4, u6, u12], datetime.now(), "Persian")
u14 = User("Tarek Abdallah", 21, "Egypt", ["FOOTBALL", "COMEDY"], [u5, u9, u13], datetime.now(), "Arabic")
u15 = User("Maya Singh", 25, "India", ["SITAR", "MOVIES", "TECH"], [u8, u10, u14], datetime.now(), "Hindi")

allUsers = [u1, u2, u3, u4, u5, u6, u7, u8, u9, u10, u11, u12, u13, u14, u15]

#инициализируем все в json

def my_default(object):
    if isinstance(object, datetime):
        return object.isoformat()
    if isinstance(object, User):
        friends = []
        hobbies = []
        for friend in object.friends:
            friends.append(friend.name)
        for hobby in object.hobbies:
            hobbies.append(hobby)
        return {"name": object.name, "age": object.age, "country": object.country, "hobbies": hobbies, "friends": friends, 
                "joined": object.joined, "nationality": object.nationality}

with open("data/mySocialNetwork.json", "w", encoding='utf-8') as f:
    json.dump(allUsers, f, indent=4, default=my_default)

with open("data/mySocialNetwork.json", "r", encoding='utf-8') as f:
    data = json.load(f)


newUsers = [0] * len(data)
friendsGraph = {}

for user in data:
    friendsGraph[user["name"]] = [] #создаем человека для запоминания его друзей
    for friend in user["friends"]:
        friendsGraph[user["name"]].append(friend)
#запомнили всех их друзей
hobbiesGraph = {}
for user in data:
    hobbiesGraph[user["name"]] = [] #creating user and then its hobbies in hobbiesgraph
    for hobby in user["hobbies"]:
        hobbiesGraph[user["name"]].append(hobby)
        
class newUser():
    def __init__(self, name, age, country, hobbies, friends, joined, nationality):
        self.name = name
        self.age = age
        self.country = country
        self.hobbies = hobbiesGraph[self.name]
        self.friends = friendsGraph[self.name]
        self.joined = joined
        self.nationality = nationality
newUsers = [0] * len(data)

for i in range(len(newUsers)):
    user = data[i]

    newUsers[i] = newUser(user["name"], user["age"], user["country"], hobbiesGraph[user["name"]],
                          friendsGraph[user["name"]], user["joined"], user["nationality"])



class SocialNetwork():

    #добавление
    def add_friend(object, toAdd):
        if toAdd.name in friendsGraph[object.name]:
            print(toAdd.name + " " + "уже в друзьях у " + object.name)
            print()
            return False
        friendsGraph[object.name].append(toAdd.name)
        object.friends = friendsGraph[object.name]
        friendsGraph[toAdd.name].append(object.name)
        toAdd.friends = friendsGraph[toAdd.name]
        print("Пользователь " + toAdd.name + " " + "был успешно добавлен")
        print()
        return
    #удаление

    def remove_friend(object, toRemove):
        if toRemove.name not in friendsGraph[object.name]:
            print(toRemove.name + " " + "не в друзьях у " + object.name)
            print()
            return False
        for i in range(len(friendsGraph[object.name])):
            if friendsGraph[object.name][i] == toRemove.name:
                friendsGraph[object.name][i], friendsGraph[object.name][-1] = friendsGraph[object.name][-1], friendsGraph[object.name][i]
                friendsGraph[object.name].pop()
                object.friends = friendsGraph[object.name]
                for j in range(len(friendsGraph[toRemove.name])):
                    if friendsGraph[toRemove.name][j] == object.name:
                        friendsGraph[toRemove.name][j], friendsGraph[toRemove.name][-1] = friendsGraph[toRemove.name][-1], friendsGraph[toRemove.name][j]
                        friendsGraph[toRemove.name].pop()
        print(toRemove.name + " " + "был удален успешно из друзей у " + object.name)
                    





#time for bfs, dfs, и фич соцсети (функций)


#общие друзья (так же с кем у тебя общий список друзей (сколько обших )
# общие хобби (так же с кем и сколько), 
# а так же поиск у кого в друзьях определенный юзер
# так же вычислитель сколько времени прошло от момента регистрации до нынешнего времени (возраст анкеты)
#имплементация dfs/bfs до какой то глубины

#общие друзья со своими друзьями
def show_common_friends(object):
    friendAndCommons = {}
    userFriends = set(friendsGraph[object.name])

    for userFriend in friendsGraph[object.name]:
        interSection = set(friendsGraph[userFriend]) & userFriends #пересечение общих друзей
        friendAndCommons[userFriend] = list(interSection)
    
    for friend, friends in friendAndCommons.items():
        if friends:
            print('Общие друзья с ' + friend + ': ', end ='')
            print(*friendAndCommons[friend])
            print()
        else:
            print("Нету общих друзей с " + friend)
            print()
    

    


#общие хобби
def show_common_hobbies(object):
    userAndCommonHobbies = {}
    userHobbies = set(hobbiesGraph[object.name])

    for user in newUsers:
        if object != user:
            interSection = set(hobbiesGraph[user.name]) & userHobbies
            if interSection:
                userAndCommonHobbies[user.name] = list(interSection)
    if not userAndCommonHobbies:
        print("Пользователь не имеет общих хобби ни с кем другим")
        return
    print()
    for userName, hobbies in userAndCommonHobbies.items():
        print('Пользователь ' + object.name + ' ' + 'имеет общие хобби с ' + userName + ": " )
        print(*userAndCommonHobbies[userName])
        print()

        

show_common_hobbies(newUsers[14])


#у кого данный пользователь в друзьях (обратная проверка) (возможно надо добавить еще список в классе newUser типо вишлист друзей где будет список кого пользователь желает добавить в друщья)

def show_got_in_friends(object):
    friendedUsers = []
    for user in newUsers:
        if object != user and object.name in friendsGraph[user.name]:
            friendedUsers.append(user.name)
    if not friendedUsers:
        print('Пользователь ни у кого не в друзьях')
        return
    print(friendedUsers)
    for friended in friendedUsers:
        print(friended + " " + "Имеет в друзьях " + object.name)
        print()

show_got_in_friends(newUsers[5])



def age_of_account(object):
    ageOfAccount = (datetime.now() - datetime.fromisoformat(object.joined)).days 
    totalSeconds = (datetime.now() - datetime.fromisoformat(object.joined)).total_seconds()
    if ageOfAccount > 0:
        print(f'Account has been there for {ageOfAccount} days')
        return
    else:
        print(f'Account has been there for  {totalSeconds // 60} minutes')
        return


age_of_account(newUsers[1])


def friends_in_one_depth(object, toCheck, notCount):
    friends = deque(friendsGraph[object.name])
    added = set()
    toCheckFriends = set(friendsGraph[toCheck.name])
    for i in range(len(friends)):
        friendOneDepth = friends[i]

        for friend in friendsGraph[friendOneDepth]:
            if friend not in added:
                added.add(friend)
                friends.append(friend)
        friends.popleft()

        

    

        


def show_best_match(object):
    userFriends = set(friendsGraph[object.name])
    commonInterests = []
    moreThanFive = 0
    for user in newUsers:
        
        if user == object or user.name in userFriends:
            continue

        score = 0
        hobbyIntersection = len(set(hobbiesGraph[user.name]) & set(hobbiesGraph[object.name])) * 5
        friendInterestection = len(userFriends & set(friendsGraph[user.name])) * 5
        ageNear = abs(object.age - user.age) 
        if ageNear <= 5:
             #максимальная разница в возрасте = 5, за 5 даю 1 как за самую дальную, за 1 даю 5, ровесники или почти одногодки некритичная разница поэтому и за одногодок из а старше/младше на 1 год я даю по 1
            ageBonus = 6 - ageNear
            score = hobbyIntersection + friendInterestection + ageBonus * 2.5
        elif ageNear <= 10:
            score = hobbyIntersection + friendInterestection
        else:
            
            age_decay = 1.0 / (1 + (ageNear - 10) * 0.2) #возможно сделаю константу 0,05 чтобы отнимать по 5 процентов за лишний год
            score = (hobbyIntersection + friendInterestection) * age_decay #за каждый 1 год от 10 лет я отнимаю по 5 процентов, от того сколько у них могло бы быть если не > 10 лет разницы
        

        commonInterests.append((score, user.name))
    commonInterests.sort(key = lambda x: x[0], reverse=True)
    print("Могут быть вам интересны: ", end='')
    for match in commonInterests:
        print(match[1])
        


def test_scoring():
    print("="*70)
    print("ТЕСТ SCORING СИСТЕМЫ")
    print("="*70)
    
    base_score = 20  # допустим 4 общих хобби
    
    print("\nБазовый score (хобби + друзья): 20")
    print("\nВозрастная корректировка:\n")
    
    test_cases = [0, 2, 5, 8, 10, 15, 20, 30, 50]
    
    for age_diff in test_cases:
        if age_diff <= 5:
            age_bonus = 6 - age_diff
            final = base_score + age_bonus * 2.5
            print(f"Разница {age_diff:2d} лет → bonus +{age_bonus*2.5:.1f} → "
                  f"Final: {final:.1f} ({final/base_score*100:.0f}%)")
            
        elif age_diff <= 10:
            final = base_score
            print(f"Разница {age_diff:2d} лет → neutral    → "
                  f"Final: {final:.1f} ({final/base_score*100:.0f}%)")
            
        else:
            factor = 1.0 / (1 + (age_diff - 10) * 0.2)
            final = base_score * factor
            print(f"Разница {age_diff:2d} лет → factor {factor:.2f} → "
                  f"Final: {final:.1f} ({final/base_score*100:.0f}%)")

#если он ни с кем не знаком выкидываем его, если он с кем то знаком, выкидываем тех кто не знаком с ним, найдем их дружбу с юзером закрытую в друггом коммьюнити
print("Fixing graph to be bidirectional...")

bidirectional_graph = {}
for user_name in friendsGraph:
    bidirectional_graph[user_name] = set(friendsGraph[user_name])

for user_name, friends in friendsGraph.items():
    for friend_name in friends:
        if friend_name in bidirectional_graph:
            bidirectional_graph[friend_name].add(user_name)

for user_name in bidirectional_graph:
    friendsGraph[user_name] = list(bidirectional_graph[user_name])

print("Graph fixed!")
print()

# Debug check
print("Alex Aguerro friends now:", friendsGraph['Alex Aguerro'])
print()

def find_communities(): 
    communities = []
    visited = set()
    for user in newUsers:
        if user.name in visited:
            continue
        friendCircle = deque()
        community = [user.name]
        visited.add(user.name)
        for friend in friendsGraph[user.name]:
            if friend not in visited:
                visited.add(friend)
                friendCircle.append(friend)
                community.append(friend)

        
        while friendCircle:
            current = friendCircle.popleft()
            
            for friend in friendsGraph[current]:
                if friend not in visited:
                    visited.add(friend)
                    community.append(friend)
                    friendCircle.append(friend)

        if community:
            communities.append(community)
    return communities        


        
        


            




communities = find_communities_new(friendsGraph, newUsers)

print(f"Найдено {len(communities)} комьюнити(ей):")
print()

for i, comm in enumerate(communities, 1):
    print(f"Комьюнити #{i} ({len(comm)} человек):")
    print(", ".join(sorted(comm)))
    print()
total_users = sum(len(c) for c in communities)
print(f"\nTotal users in communities: {total_users}")
print(f"Total users in system: {len(newUsers)}")
print(f"Match: {total_users == len(newUsers)} ✅")





