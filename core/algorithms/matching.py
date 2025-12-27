"""
User matching and recommendation algorithms
"""

def calculate_match_score(user1, user2, friends_graph, hobbies_graph):
    """
    Calculate compatibility score between two users
    
    Uses:
    - Common hobbies (weight: 5)
    - Mutual friends (weight: 5)
    - Age similarity (exponential decay)
    
    Args:
        user1, user2: User objects
        friends_graph: dict of friendships
        hobbies_graph: dict of hobbies
    
    Returns:
        float: compatibility score
    """
    user_friends = set(friends_graph[user1.name])
    
    # Base scores
    hobby_score = len(
        set(hobbies_graph[user1.name]) & 
        set(hobbies_graph[user2.name])
    ) * 5
    
    friend_score = len(
        user_friends & 
        set(friends_graph[user2.name])
    ) * 5
    
    # Added age_decay as penalty, uses exponential decay, using 20% rn for each year as penalty, probably gonna use 0.05 instead of it
    #in future might work with that and for some hobbies my const is too much and age gap isnt that much of a big deal, might make it 0.01 or delete if user has for example hobby "fishing"
    #and for sport only for example to increase 0.2
    
    age_diff = abs(user1.age - user2.age)
    
    if age_diff <= 5:
        age_bonus = (6 - age_diff) * 2.5
        score = hobby_score + friend_score + age_bonus
    elif age_diff <= 10:
        score = hobby_score + friend_score
    else:
        age_decay = 1.0 / (1 + (age_diff - 10) * 0.2)
        score = (hobby_score + friend_score) * age_decay
    
    return score


def show_best_match(user, all_users, friends_graph, hobbies_graph):
    """
    Find and display best matches for a user
    
    Args:
        user: User object
        all_users: list of all User objects
        friends_graph: dict of friendships
        hobbies_graph: dict of hobbies
    
    Returns:
        list of (score, user_name) tuples, sorted by score
    """
    user_friends = set(friends_graph[user.name])
    candidates = []
    
    for other in all_users:
        if other == user or other.name in user_friends:
            continue
        
        score = calculate_match_score(user, other, friends_graph, hobbies_graph)
        candidates.append((score, other.name))
    
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    # Display results
    print("Могут быть вам интересны: ", end='')
    for match in candidates:
        print(match[1])
    
    return candidates