"""
User and friendship generation for testing
"""
import random
from datetime import datetime, timedelta


# pool for generating users
FIRST_NAMES = [
    "Alex", "Maria", "John", "Emma", "Liam", "Olivia",
    "Noah", "Ava", "Ethan", "Sophia", "Mason", "Isabella",
    "James", "Mia", "Lucas", "Charlotte", "Henry", "Amelia",
    "Aiden", "Harper", "Sebastian", "Ella", "Jack", "Aria",
    "Michael", "Lily", "Daniel", "Grace", "Matthew", "Chloe",
    "David", "Zoe", "Joseph", "Scarlett", "Samuel", "Victoria",
    "Carter", "Madison", "Owen", "Riley", "Wyatt", "Layla",
    "Gabriel", "Nora", "Julian", "Ellie", "Leo", "Hannah",
    "Isaac", "Aubrey", "Nathan", "Addison", "Caleb", "Hazel",
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Martinez", "Davis", "Rodriguez", "Miller",
    "Anderson", "Taylor", "Thomas", "Moore", "Jackson",
    "White", "Harris", "Martin", "Thompson", "Lee",
    "Walker", "Hall", "Allen", "Young", "King",
    "Wright", "Lopez", "Hill", "Scott", "Green",
    "Adams", "Baker", "Nelson", "Carter", "Mitchell",
    "Perez", "Roberts", "Turner", "Phillips", "Campbell",
    "Parker", "Evans", "Edwards", "Collins", "Stewart",
    "Sanchez", "Morris", "Rogers", "Reed", "Cook",
]

COUNTRIES = [
    "Kazakhstan", "USA", "UK", "Germany", "France",
    "Spain", "Italy", "Japan", "China", "Brazil",
    "Canada", "Australia", "Russia", "India", "Mexico",
    "South Korea", "Netherlands", "Sweden", "Norway", "Poland",
    "Turkey", "Argentina", "Chile", "Vietnam", "Thailand",
]

HOBBIES = [
    "SPORTS", "MUSIC", "READING", "GAMING", "COOKING",
    "TRAVEL", "PHOTOGRAPHY", "CODING", "GYM", "YOGA",
    "MOVIES", "ANIME", "HIKING", "CYCLING", "SWIMMING",
    "DANCING", "PAINTING", "CHESS", "GUITAR", "PIANO",
    "FOOTBALL", "BASKETBALL", "TENNIS", "SKIING", "SURFING",
    "BAKING", "GARDENING", "WRITING", "DRAWING", "SINGING",
    "RUNNING", "BOXING", "MEDITATION", "TECH", "FASHION",
]

NATIONALITIES = {
    "Kazakhstan": "Kazakh",
    "USA": "American",
    "UK": "British",
    "Germany": "German",
    "France": "French",
    "Spain": "Spanish",
    "Italy": "Italian",
    "Japan": "Japanese",
    "China": "Chinese",
    "Brazil": "Brazilian",
    "Canada": "Canadian",
    "Australia": "Australian",
    "Russia": "Russian",
    "India": "Indian",
    "Mexico": "Mexican",
    "South Korea": "Korean",
    "Netherlands": "Dutch",
    "Sweden": "Swedish",
    "Norway": "Norwegian",
    "Poland": "Polish",
    "Turkey": "Turkish",
    "Argentina": "Argentinian",
    "Chile": "Chilean",
    "Vietnam": "Vietnamese",
    "Thailand": "Thai",
}


def generate_users(n=100, User_class=None):
    """
    Generate n random users with realistic data
    
    Args:
        n: number of users to generate
        User_class: User class to instantiate (if None, returns dicts)
    
    Returns:
        list of User objects or dicts
    """
    users = []
    used_names = set()
    
    for i in range(n):
        # Generate unique name
        while True:
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            name = f"{first} {last}"
            
            if name not in used_names:
                used_names.add(name)
                break
        
        # Random attributes
        age = random.randint(18, 35)
        country = random.choice(COUNTRIES)
        nationality = NATIONALITIES.get(country, country)
        
        # 2-5 hobbies per person
        num_hobbies = random.randint(2, 5)
        hobbies = random.sample(HOBBIES, num_hobbies)
        
        # Random join date (max age of accoutn 2 years)
        days_ago = random.randint(0, 730)
        joined = datetime.now() - timedelta(days=days_ago)
        
        # Create user
        if User_class:
            user = User_class(
                name=name,
                age=age,
                country=country,
                hobbies=hobbies,
                friends=[],  # Will be filled later
                joined=joined,
                nationality=nationality
            )
        else:
            user = {
                "name": name,
                "age": age,
                "country": country,
                "hobbies": hobbies,
                "friends": [],
                "joined": joined.isoformat(),
                "nationality": nationality
            }
        
        users.append(user)
    
    return users


def generate_friendships(users, avg_friends=8, min_friends=3, max_friends=15):
    """
    Generate realistic friendships based on compatibility
    
    Uses:
    - Common hobbies (most important)
    - Similar age
    - Same country (bonus)
    
    Args:
        users: list of User objects
        avg_friends: target average number of friends
        min_friends: minimum friends per user
        max_friends: maximum friends per user
    
    Returns:
        dict: friendship graph {name: [friend_names]}
    """
    friends_graph = {u.name: [] for u in users}
    
    for user in users:
        # Calculate compatibility with all others
        candidates = []
        toCheck = set(friends_graph[user.name])
        
        for other in users:
            if user == other:
                continue
            
            # Skip if already friends
            if other.name in friends_graph[user.name]:
                continue
            
            # Calculate compatibility score
            score = 0
            
            # Common hobbies (most important!)
            common_hobbies = len(set(user.hobbies) & set(other.hobbies))
            score += common_hobbies * 3
            
            # Age similarity
            age_diff = abs(user.age - other.age)
            if age_diff <= 3:
                score += 2
            elif age_diff <= 7:
                score += 1
            
            # Same country
            if user.country == other.country:
                score += 1
            
            if score > 0:
                candidates.append((other, score))
        
        if not candidates:
            continue
        
        # Sort by compatibility
        candidates.sort(key=lambda x: x[1], reverse=True)
        
        # Determine number of friends for this user
        current_friends = len(friends_graph[user.name])
        target_friends = random.randint(
            max(min_friends - current_friends, 0),
            max_friends - current_friends
        )
        
        if target_friends <= 0:
            continue
        
        # Select friends (with some randomness)
        # Take top portion but randomize within it
        top_portion = min(target_friends * 3, len(candidates))
        pool = candidates[:top_portion]
        
        num_to_add = min(target_friends, len(pool))
        selected = random.sample(pool, num_to_add)
        
        # Add bidirectional friendships
        for friend, _ in selected:
            if friend.name not in friends_graph[user.name]:
                friends_graph[user.name].append(friend.name)
                friends_graph[friend.name].append(user.name)
    
    return friends_graph


def apply_friendships_to_users(users, friends_graph):
    """
    Update User objects with friendship data
    
    Args:
        users: list of User objects
        friends_graph: dict of friendships
    """
    for user in users:
        user.friends = friends_graph.get(user.name, [])


def print_generation_stats(users, friends_graph):
    """Print statistics about generated network"""
    total_friendships = sum(len(friends) for friends in friends_graph.values()) // 2
    avg_friends = total_friendships * 2 / len(users)
    
    # Find min/max friends
    friend_counts = [len(friends) for friends in friends_graph.values()]
    min_friends = min(friend_counts)
    max_friends = max(friend_counts)
    
    print("="*70)
    print("GENERATION STATISTICS")
    print("="*70)
    print(f"Total users: {len(users)}")
    print(f"Total friendships: {total_friendships}")
    print(f"Average friends per user: {avg_friends:.1f}")
    print(f"Min friends: {min_friends}")
    print(f"Max friends: {max_friends}")
    print()
    
    # Age distribution
    ages = [u.age for u in users]
    print(f"Age range: {min(ages)}-{max(ages)}")
    print(f"Average age: {sum(ages)/len(ages):.1f}")
    print()
    
    # Country distribution (top 5)
    from collections import Counter
    country_counts = Counter(u.country for u in users)
    print("Top 5 countries:")
    for country, count in country_counts.most_common(5):
        print(f"  {country}: {count} users")
    print()
    
    # Hobby distribution (top 10)
    hobby_counts = Counter()
    for u in users:
        hobby_counts.update(u.hobbies)
    
    print("Top 10 hobbies:")
    for hobby, count in hobby_counts.most_common(10):
        print(f"  {hobby}: {count} users")
    print("="*70)
    print()