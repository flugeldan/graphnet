"""
Social network analysis functions
"""
from datetime import datetime


def show_common_friends(user, friends_graph):
    """
    Find and display common friends between user and their friends
    
    Args:
        user: User object
        friends_graph: dict of friendships
    
    Returns:
        dict: {friend_name: [common_friends]}
    """
    friend_and_commons = {}
    user_friends = set(friends_graph[user.name])
    
    for user_friend in friends_graph[user.name]:
        intersection = set(friends_graph[user_friend]) & user_friends
        friend_and_commons[user_friend] = list(intersection)
    
    # Display results
    for friend, commons in friend_and_commons.items():
        if commons:
            print(f'Общие друзья с {friend}: ', end='')
            print(*friend_and_commons[friend])
            print()
        else:
            print(f"Нету общих друзей с {friend}")
            print()
    
    return friend_and_commons


def show_common_hobbies(user, all_users, hobbies_graph):
    """
    Find and display users with common hobbies
    
    Args:
        user: User object
        all_users: list of all User objects
        hobbies_graph: dict of hobbies
    
    Returns:
        dict: {user_name: [common_hobbies]}
    """
    user_and_common_hobbies = {}
    user_hobbies = set(hobbies_graph[user.name])
    
    for other in all_users:
        if user != other:
            intersection = set(hobbies_graph[other.name]) & user_hobbies
            if intersection:
                user_and_common_hobbies[other.name] = list(intersection)
    
    if not user_and_common_hobbies:
        print("Пользователь не имеет общих хобби ни с кем другим")
        return user_and_common_hobbies
    
    # Display results
    print()
    for user_name, hobbies in user_and_common_hobbies.items():
        print(f'Пользователь {user.name} имеет общие хобби с {user_name}: ')
        print(*user_and_common_hobbies[user_name])
        print()
    
    return user_and_common_hobbies


def show_got_in_friends(user, all_users, friends_graph):
    """
    Find who has this user as friend (reverse lookup)
    
    Args:
        user: User object
        all_users: list of all User objects
        friends_graph: dict of friendships
    
    Returns:
        list of user names who have this user as friend
    """
    friended_users = []
    
    for other in all_users:
        if other != user and user.name in friends_graph[other.name]:
            friended_users.append(other.name)
    
    if not friended_users:
        print('Пользователь ни у кого не в друзьях')
        return friended_users
    
    # Display results
    print(friended_users)
    for friended in friended_users:
        print(f"{friended} Имеет в друзьях {user.name}")
        print()
    
    return friended_users


def age_of_account(user):
    """
    Calculate and display account age
    
    Args:
        user: User object
    
    Returns:
        int: age in days (or float: age in minutes if < 1 day)
    """
    age_days = (datetime.now() - datetime.fromisoformat(user.joined)).days
    total_seconds = (datetime.now() - datetime.fromisoformat(user.joined)).total_seconds()
    
    if age_days > 0:
        print(f'Account has been there for {age_days} days')
        return age_days
    else:
        minutes = total_seconds // 60
        print(f'Account has been there for {minutes} minutes')
        return minutes