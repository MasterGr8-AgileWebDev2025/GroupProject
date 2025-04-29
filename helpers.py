import json
from datetime import datetime
import logging
import random  # Just for generating sample data for the MVP
import pandas as pd
import os
from werkzeug.utils import secure_filename

def get_user_statistics(user_id):
    """
    Calculate aggregated statistics for a user based on their match history.
    
    Args:
        user_id: The ID of the user
        
    Returns:
        Dictionary of aggregated statistics
    """
    # In a real implementation, this would query the database for actual statistics
    # For MVP, we'll generate sample data
    return {
        "matches_played": random.randint(5, 50),
        "win_percentage": random.randint(40, 80),
        "avg_aces_per_match": round(random.uniform(2.0, 8.0), 1),
        "avg_double_faults": round(random.uniform(1.0, 6.0), 1),
        "first_serve_percentage_avg": random.randint(50, 75),
        "forehand_winners_avg": round(random.uniform(5.0, 20.0), 1),
        "backhand_winners_avg": round(random.uniform(3.0, 15.0), 1)
    }
