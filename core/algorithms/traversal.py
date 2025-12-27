"""
Graph traversal algorithms: BFS, DFS, community detection
Community - 2 people may not know each other, but they connected through 1 person that they both know
might add when everyone knows each other but only for small communities to avoid NP-HARD click problem
"""
from collections import deque


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