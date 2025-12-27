"""
User and SocialNetwork models
"""
from datetime import datetime


class User:
    """User in social network"""
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


class SocialNetwork:
    """Social network operations"""
    
    def add_friend(self, user_obj, friend_obj):
        """Add bidirectional friendship"""
        
        from __main__ import friendsGraph
        
        if friend_obj.name in friendsGraph[user_obj.name]:
            print(f"{friend_obj.name} уже в друзьях у {user_obj.name}\n")
            return False
        
        friendsGraph[user_obj.name].append(friend_obj.name)
        user_obj.friends = friendsGraph[user_obj.name]
        friendsGraph[friend_obj.name].append(user_obj.name)
        friend_obj.friends = friendsGraph[friend_obj.name]
        
        print(f"Пользователь {friend_obj.name} был успешно добавлен\n")
        return True
    
    def remove_friend(self, user_obj, friend_obj):
        """Remove bidirectional friendship(i.m making friendship mutual)"""
        from __main__ import friendsGraph
        
        if friend_obj.name not in friendsGraph[user_obj.name]:
            print(f"{friend_obj.name} не в друзьях у {user_obj.name}\n")
            return False
        
        #swap
        friendsGraph[user_obj.name].remove(friend_obj.name)
        friendsGraph[friend_obj.name].remove(user_obj.name)
        user_obj.friends = friendsGraph[user_obj.name]
        friend_obj.friends = friendsGraph[friend_obj.name]
        
        print(f"{friend_obj.name} был удален успешно из друзей у {user_obj.name}")
        return True