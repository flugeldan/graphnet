"""
GraphNet - Social Network Analysis Engine
Main entry point
"""
import os
from datetime import datetime

# Import core modules
from core.models import User, SocialNetwork
from core.algorithms import (
    find_communities,
    show_best_match,
    show_common_friends,
    show_common_hobbies,
    show_got_in_friends,
    age_of_account
)
from utils.json_utils import (
    load_from_json,
    make_bidirectional
)


#absolute path 
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(SCRIPT_DIR, "data", "mySocialNetwork.json")

print(f"Script directory: {SCRIPT_DIR}")
print(f"Data file path: {DATA_FILE}")
print(f"File exists: {os.path.exists(DATA_FILE)}")
print()




# === Load from JSON (generated data) === (u can change parameters of generating data for test cases in scripts and in generate_data in data)
print("Загружаю данные о сети")
data = load_from_json(filename="mySocialNetwork.json")
print(f"Загружена сеть с  {len(data)} юзерами")

#первый и крайний юзер
if data:
    print(f"Первый пользователь: {data[0]['name']}")
    print(f"Крайний пользователь: {data[-1]['name']}")
print()


# building graphs (need to add more graphs)
newUsers = []
friendsGraph = {}
hobbiesGraph = {}

for user_data in data:
    friendsGraph[user_data["name"]] = user_data["friends"]
    hobbiesGraph[user_data["name"]] = user_data["hobbies"]

# Make bidirectional (if someone isnt friended mutually, probably don't need it, created when had hardcoded 15 small unconnected test-users)
print("Fixing graph to be bidirectional...")
friendsGraph = make_bidirectional(friendsGraph)
print("Graph fixed!\n")


# === Create newUser objects ===
class newUser:
    id = 0 
    def __init__(self, name, age, country, hobbies, friends, joined, nationality):
        self.name = name
        self.age = age
        self.id = newUser.id
        newUser.id += 1 
        self.country = country
        self.hobbies = hobbiesGraph[self.name]
        self.friends = friendsGraph[self.name]
        self.joined = joined
        self.nationality = nationality



for user_data in data:
    user = newUser(
        user_data["name"],
        user_data["age"],
        user_data["country"],
        hobbiesGraph[user_data["name"]],
        friendsGraph[user_data["name"]],
        user_data["joined"],
        user_data["nationality"]
    )
    newUsers.append(user)


# Demo functions 
def main():
    """Main demo"""
    print("="*70)
    print("GraphNet - Social Network Analysis")
    print("="*70)
    print()
    
    print(f"Network size: {len(newUsers)} users")
    print(f"Total friendships: {sum(len(f) for f in friendsGraph.values()) // 2}")
    print()
    
    # Common hobbies (show people who have same hobbies as user)
    print("=== Common Hobbies Test ===")
    test_user = newUsers[0]  # First user
    show_common_hobbies(test_user, newUsers, hobbiesGraph)
    
    # Got in friends (reversed search of people who have user in friends, was created for fun)
    print("=== Got In Friends Test ===")
    show_got_in_friends(newUsers[5], newUsers, friendsGraph)
    
    # Account age
    print("=== Account Age Test ===")
    age_of_account(newUsers[1])
    print()
    
    # Find communities
    print("=== Community Detection ===")
    communities = find_communities(friendsGraph, newUsers)
    
    print(f"Найдено {len(communities)} комьюнити(ей):\n")
    for i, comm in enumerate(communities, 1):
        print(f"Комьюнити #{i} ({len(comm)} человек):")
        # Print first 10 names if community is large =
        if len(comm) > 10:
            print(", ".join(sorted(comm)[:10]) + f" ... (+{len(comm)-10} more)")
        else:
            print(", ".join(sorted(comm)))
        print()
    
    # Verification
    total_users = sum(len(c) for c in communities) #counting people who are in some communities
    print(f"Total users in communities: {total_users}")
    print(f"Total users in system: {len(newUsers)}")
    print(f"Match: {total_users == len(newUsers)} ✅")
    print()


if __name__ == "__main__":
    main()