"""
Graph traversal algorithms: BFS, DFS, community detection
Community - 2 people may not know each other, but they connected through 1 person that they both know
might add when everyone knows each other but only for small communities to avoid NP-HARD click problem
"""
from collections import deque
from typing import Tuple, List, Optional

def find_communities(friends_graph, all_users):
    """
    Find connected components in social network using BFS
    
    Args:
        friends_graph: dict mapping user names to friend lists
        all_users: list of user objects
    
    Returns:
        list of communities (each = list of user names)
    """



    communities = []
    visited = set()
    
    for user in all_users:
        if user.name in visited:
            continue
        
        friendCircle = deque()
        community = [user.name]
        visited.add(user.name)
        
        for friend in friends_graph[user.name]:
            if friend not in visited:
                visited.add(friend)
                friendCircle.append(friend)
                community.append(friend)
        
        while friendCircle:
            current = friendCircle.popleft()
            
            for friend in friends_graph[current]:
                if friend not in visited:
                    visited.add(friend)
                    community.append(friend)
                    friendCircle.append(friend)
        
        if community:
            communities.append(community)
    
    return communities


def separation_degree(user1, user2, friendsgraph: dict) -> Tuple[Optional[int], Optional[List[str]]]:
    """
    Finds shortest path between 2 users.
    If they are being friends directly, path = 1, for each node we add + 1

    To remember exact same path, we previous nodes in list, then if we didn't find our user2
    we add to previous nodes current node, [prev nodes] + [current node]
    In to check (array of checking friends friends), we keep people in format 
    ([path to person], person)

    """
    if user1 == user2:
        return (0, [user1.name])
    
    if user1.name in friendsgraph[user2.name]:
        return (1, [user1.name, user2.name])
    

    visited = set()
    path = (None, None)
    toCheck = deque([([user1.name], person) for person in friendsgraph[user1.name]])

    while toCheck:
        current_path, current_person = toCheck.popleft()
        
        if current_person not in visited:
            visited.add(current_person)
            personFriends = set(friendsgraph[current_person])
            personFriends = personFriends.difference(visited)

            if user2.name in personFriends:
                final_path = current_path + [current_person, user2.name]
                distance = len(final_path) - 1
                path = (distance, final_path)

                break
            else:
                friends = list(personFriends)
                s = current_path + [current_person]

                for friend in friends:
                    toCheck.append((s, friend))
                

    return path
    


            



