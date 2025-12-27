"""
JSON serialization/deserialization utilities
"""
import json
from datetime import datetime
import os


def serialize_user(user_obj):
    """
    Serialize User object to dict for JSON
    
    Handles User objects and datetime objects
    """
    if isinstance(user_obj, datetime):
        return user_obj.isoformat()
    
    # Assume it's a User object
    friends = []
    hobbies = []
    
    for friend in user_obj.friends:
        # Handle both User objects and strings
        if hasattr(friend, 'name'):
            friends.append(friend.name)
        else:
            friends.append(friend)
    
    for hobby in user_obj.hobbies:
        hobbies.append(hobby)
    
    return {
        "name": user_obj.name,
        "age": user_obj.age,
        "country": user_obj.country,
        "hobbies": hobbies,
        "friends": friends,
        "joined": user_obj.joined if isinstance(user_obj.joined, str) else user_obj.joined.isoformat(),
        "nationality": user_obj.nationality
    }


def save_to_json(data, filename="mySocialNetwork.json"):
    """
    Save users list to JSON file
    
    Args:
        data: list of User objects OR already serialized dicts
        filename: name of JSON file (default: mySocialNetwork.json)
    """
    try:
        # Get project root (graphnet/)
        # This works whether called from main.py or scripts/
        current_file = os.path.abspath(__file__)
        utils_dir = os.path.dirname(current_file)
        project_root = os.path.dirname(utils_dir)
        data_dir = os.path.join(project_root, "data")
        filepath = os.path.join(data_dir, filename)
        
        # Create data/ directory if doesn't exist
        os.makedirs(data_dir, exist_ok=True)
        
        # Auto-serialize User objects if needed
        serialized_data = []
        for item in data:
            if isinstance(item, dict):
                # Already serialized
                serialized_data.append(item)
            else:
                # Assume it's a User object - serialize it
                serialized_data.append(serialize_user(item))
        
        # Save to file
        with open(filepath, "w", encoding='utf-8') as f:
            json.dump(serialized_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Saved {len(serialized_data)} users to: {filepath}")
        return filepath
        
    except Exception as e:
        print(f"❌ Error saving: {e}")
        import traceback
        traceback.print_exc()
        return None


def load_from_json(filename="mySocialNetwork.json"):
    """
    Load users from JSON file
    
    Args:
        filename: name of JSON file (default: mySocialNetwork.json)
    
    Returns:
        list of user dicts, or None if file not found
    """
    # Get project root (graphnet/)
    current_file = os.path.abspath(__file__)
    utils_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(utils_dir)
    filepath = os.path.join(project_root, "data", filename)
    
    try:
        with open(filepath, "r", encoding='utf-8') as f:
            data = json.load(f)
        print(f"✅ Loaded {len(data)} users from: {filepath}")
        return data
    except FileNotFoundError:
        print(f"⚠️  File not found: {filepath}")
        print(f"⚠️  Looking at: {filepath}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON in {filepath}: {e}")
        return None







def make_bidirectional(friends_graph):
    """
    Ensure friendship graph is bidirectional
    
    Args:
        friends_graph: dict mapping user names to friend lists
    
    Returns:
        dict: bidirectional friendship graph
    """
    bidirectional = {}
    
    # Converting to sets for faster efficiency
    for user_name in friends_graph:
        bidirectional[user_name] = set(friends_graph[user_name])
    
    # Adding reverse edges
    for user_name, friends in friends_graph.items():
        for friend_name in friends:
            if friend_name in bidirectional:
                bidirectional[friend_name].add(user_name)
            else:
                # Friend exists but wasn't in original graph
                bidirectional[friend_name] = {user_name}
    
    # Converting back to lists 
    for user_name in bidirectional:
        bidirectional[user_name] = list(bidirectional[user_name])
    
    return bidirectional