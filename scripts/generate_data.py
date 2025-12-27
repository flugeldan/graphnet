"""
Generate test data for GraphNet

Run from project root: python3 scripts/generate_data.py
"""
import sys
import os

# Add parent directory to Python path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)
sys.path.insert(0, PROJECT_ROOT)

from core.models import User
from data.generators.user_generator import (
    generate_users,
    generate_friendships,
    apply_friendships_to_users,
    print_generation_stats
)
from utils.json_utils import save_to_json


def main():
    """Generate 100-150 users with realistic friendships"""
    
    print("="*70)
    print("GRAPHNET DATA GENERATOR")
    print("="*70)
    print()
    
    print("Generating users...")
    num_users = 120  # Can change this: 100-150
    
    # Generate users
    users = generate_users(n=num_users, User_class=User)
    print(f"✅ Generated {len(users)} users!")
    print()
    
    # Generate friendships
    print("Generating friendships...")
    friends_graph = generate_friendships(
        users,
        avg_friends=8,
        min_friends=3,
        max_friends=15
    )
    print("✅ Friendships generated!")
    print()
    
    # Apply to users
    apply_friendships_to_users(users, friends_graph)
    
    # Print stats
    print_generation_stats(users, friends_graph)
    
    # Save to JSON (будет автоматически в data/mySocialNetwork.json)
    save_to_json(users)
    
    print()
    print("="*70)
    print("✅ DATA GENERATION COMPLETE!")
    print("="*70)
    print(f"✅ {len(users)} users with realistic friendships")
    print("✅ Saved to: data/mySocialNetwork.json")
    print("✅ Ready to test GraphNet algorithms!")
    print()


if __name__ == "__main__":
    main()