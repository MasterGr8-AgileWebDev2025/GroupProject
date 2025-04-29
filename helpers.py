import json
from datetime import datetime
import logging
import random  # Just for generating sample data for the MVP
import pandas as pd
import os
from werkzeug.utils import secure_filename

# Helper functions for processing tennis match data
def process_match_data(files, match_id):
    """
    Process uploaded match data files and extract statistics.
    For the MVP, we'll generate sample data since we won't be processing actual files.
    
    Args:
        files: The uploaded files from the form
        match_id: The ID of the match
        
    Returns:
        Dictionary of statistics extracted from the files
    """
    # In a real implementation, this would parse files (CSV, videos, etc.)
    # For MVP, we'll generate sample data
    logging.debug(f"Processing match data for match_id: {match_id}")
    
    # Sample statistics data structure
    statistics = {
        "basic_stats": {
            "aces": random.randint(0, 10),
            "double_faults": random.randint(0, 8),
            "first_serve_percentage": random.randint(40, 80),
            "first_serve_points_won": random.randint(60, 90),
            "second_serve_points_won": random.randint(30, 60),
            "break_points_saved": random.randint(0, 5),
            "break_points_converted": random.randint(0, 5),
            "total_points_won": random.randint(50, 120)
        },
        "shot_analysis": {
            "forehand": {
                "winners": random.randint(5, 25),
                "errors": random.randint(5, 20),
                "placement": {
                    "cross_court": random.randint(10, 40),
                    "down_the_line": random.randint(5, 30),
                    "inside_out": random.randint(3, 15)
                },
                "speed": {
                    "avg": random.randint(70, 100),
                    "max": random.randint(100, 140),
                    "min": random.randint(50, 70)
                }
            },
            "backhand": {
                "winners": random.randint(3, 15),
                "errors": random.randint(5, 25),
                "placement": {
                    "cross_court": random.randint(10, 40),
                    "down_the_line": random.randint(5, 20),
                    "inside_out": random.randint(1, 10)
                },
                "speed": {
                    "avg": random.randint(60, 90),
                    "max": random.randint(90, 120),
                    "min": random.randint(40, 60)
                }
            },
            "serve": {
                "placement": {
                    "wide": random.randint(10, 30),
                    "body": random.randint(5, 20),
                    "t": random.randint(10, 30)
                },
                "speed": {
                    "avg": random.randint(100, 180),
                    "max": random.randint(180, 220),
                    "min": random.randint(80, 100)
                }
            },
            "volley": {
                "winners": random.randint(0, 10),
                "errors": random.randint(0, 10)
            }
        },
        "player_movement": {
            "distance_covered": random.randint(1000, 3000),
            "sprints": random.randint(10, 50),
            "direction_changes": random.randint(100, 300)
        },
        "game_phases": {
            "preparation": {
                "score": random.randint(60, 95),
                "grip_rating": random.choice(["Excellent", "Good", "Needs Improvement"]),
                "stance_rating": random.choice(["Excellent", "Good", "Needs Improvement"]),
                "shoulder_rotation": random.choice(["Excellent", "Good", "Needs Improvement"])
            },
            "backswing": {
                "score": random.randint(60, 95),
                "body_position": random.choice(["Excellent", "Good", "Needs Improvement"]),
                "racket_path": random.choice(["Excellent", "Good", "Needs Improvement"])
            },
            "contact": {
                "score": random.randint(60, 95),
                "accuracy": random.choice(["Excellent", "Good", "Needs Improvement"]),
                "timing": random.choice(["Excellent", "Good", "Needs Improvement"])
            },
            "follow_through": {
                "score": random.randint(60, 95),
                "completion": random.choice(["Excellent", "Good", "Needs Improvement"]),
                "balance": random.choice(["Excellent", "Good", "Needs Improvement"])
            }
        },
        "improvements": {
            "areas": [
                {
                    "title": random.choice([
                        "Serve Consistency", 
                        "Forehand Technique", 
                        "Backhand Technique",
                        "Volley Positioning",
                        "Return of Serve"
                    ]),
                    "description": random.choice([
                        "Focus on improving your first serve percentage to gain control of points.",
                        "Work on maintaining proper swing path for more consistent contact.",
                        "Practice follow-through to increase power and reduce errors.",
                        "Position yourself closer to the net for more effective volleys.",
                        "Improve anticipation and racket preparation for returns."
                    ])
                },
                {
                    "title": random.choice([
                        "Movement Efficiency", 
                        "Point Construction", 
                        "Net Game",
                        "Shot Selection",
                        "Recovery Position"
                    ]),
                    "description": random.choice([
                        "Improve split-step timing to enhance court coverage and response time.",
                        "Focus on strategic shot sequences to build pressure on opponent.",
                        "Develop better volley technique with proper racket positioning.",
                        "Make smarter choices based on court position and opponent location.",
                        "Work on returning to an optimal position after each shot."
                    ])
                }
            ],
            "strengths": random.choice([
                "Strong forehand and consistent first serve percentage. Good court coverage with effective movement patterns.",
                "Excellent backhand technique with minimal errors. Strong serving performance with good placement variety.",
                "Great net game with confident volleys. Solid mental approach with good point construction.",
                "Powerful serve with high first serve percentage. Strong baseline game with effective shot selection.",
                "Exceptional footwork and court positioning. Strong defensive skills and shot anticipation."
            ])
        }
    }
    
    return statistics

def process_excel_data(file, match_id):
    """
    Process Excel file and extract tennis match statistics.
    
    Args:
        file: The uploaded Excel file
        match_id: The ID of the match
        
    Returns:
        Dictionary of statistics extracted from Excel
    """
    logging.debug(f"Processing Excel data for match_id: {match_id}")
    
    # Save the file temporarily to read it with pandas
    filename = secure_filename(file.filename)
    temp_path = os.path.join('/tmp', filename)
    file.save(temp_path)
    
    try:
        # Read the Excel file
        df = pd.read_excel(temp_path)
        logging.debug(f"Excel file loaded, shape: {df.shape}")
        
        # Expected Excel format:
        # The Excel sheet should have different sections with statistics
        # Try to extract data from various sheets or sections
        
        # For MVP purpose, we'll use the file but still generate sample data
        # In production, this would parse the actual Excel data
        
        # Check if this is a recognized tennis stats template
        # Basic validation: check for expected column names or sheet structure
        has_basic_stats = False
        has_shot_analysis = False
        has_movement_data = False
        
        # Look for common header names in tennis statistics
        if set(['Aces', 'Double Faults', 'First Serve %']).issubset(set(df.columns)):
            has_basic_stats = True
            logging.debug("Found basic statistics columns")
        
        if set(['Forehand Winners', 'Backhand Winners', 'Forehand Errors']).issubset(set(df.columns)):
            has_shot_analysis = True
            logging.debug("Found shot analysis columns")
            
        if set(['Distance', 'Sprints', 'Direction Changes']).issubset(set(df.columns)):
            has_movement_data = True
            logging.debug("Found movement data columns")
        
        # In a real implementation, we would extract actual values from the Excel file
        # For this MVP, we'll generate sample data but acknowledge the Excel upload
        
        # Same sample statistics structure as in process_match_data, with slight enhancements
        statistics = {
            "basic_stats": {
                "aces": random.randint(0, 10),
                "double_faults": random.randint(0, 8),
                "first_serve_percentage": random.randint(40, 80),
                "first_serve_points_won": random.randint(60, 90),
                "second_serve_points_won": random.randint(30, 60),
                "break_points_saved": random.randint(0, 5),
                "break_points_converted": random.randint(0, 5),
                "total_points_won": random.randint(50, 120)
            },
            "shot_analysis": {
                "forehand": {
                    "winners": random.randint(5, 25),
                    "errors": random.randint(5, 20),
                    "placement": {
                        "cross_court": random.randint(10, 40),
                        "down_the_line": random.randint(5, 30),
                        "inside_out": random.randint(3, 15)
                    },
                    "speed": {
                        "avg": random.randint(70, 100),
                        "max": random.randint(100, 140),
                        "min": random.randint(50, 70)
                    }
                },
                "backhand": {
                    "winners": random.randint(3, 15),
                    "errors": random.randint(5, 25),
                    "placement": {
                        "cross_court": random.randint(10, 40),
                        "down_the_line": random.randint(5, 20),
                        "inside_out": random.randint(1, 10)
                    },
                    "speed": {
                        "avg": random.randint(60, 90),
                        "max": random.randint(90, 120),
                        "min": random.randint(40, 60)
                    }
                },
                "serve": {
                    "placement": {
                        "wide": random.randint(10, 30),
                        "body": random.randint(5, 20),
                        "t": random.randint(10, 30)
                    },
                    "speed": {
                        "avg": random.randint(100, 180),
                        "max": random.randint(180, 220),
                        "min": random.randint(80, 100)
                    }
                },
                "volley": {
                    "winners": random.randint(0, 10),
                    "errors": random.randint(0, 10)
                }
            },
            "player_movement": {
                "distance_covered": random.randint(1000, 3000),
                "sprints": random.randint(10, 50),
                "direction_changes": random.randint(100, 300)
            },
            "game_phases": {
                "preparation": {
                    "score": random.randint(60, 95),
                    "grip_rating": random.choice(["Excellent", "Good", "Needs Improvement"]),
                    "stance_rating": random.choice(["Excellent", "Good", "Needs Improvement"]),
                    "shoulder_rotation": random.choice(["Excellent", "Good", "Needs Improvement"])
                },
                "backswing": {
                    "score": random.randint(60, 95),
                    "body_position": random.choice(["Excellent", "Good", "Needs Improvement"]),
                    "racket_path": random.choice(["Excellent", "Good", "Needs Improvement"])
                },
                "contact": {
                    "score": random.randint(60, 95),
                    "accuracy": random.choice(["Excellent", "Good", "Needs Improvement"]),
                    "timing": random.choice(["Excellent", "Good", "Needs Improvement"])
                },
                "follow_through": {
                    "score": random.randint(60, 95),
                    "completion": random.choice(["Excellent", "Good", "Needs Improvement"]),
                    "balance": random.choice(["Excellent", "Good", "Needs Improvement"])
                }
            },
            "improvements": {
                "areas": [
                    {
                        "title": random.choice([
                            "Serve Consistency", 
                            "Forehand Technique", 
                            "Backhand Technique",
                            "Volley Positioning",
                            "Return of Serve"
                        ]),
                        "description": random.choice([
                            "Focus on improving your first serve percentage to gain control of points.",
                            "Work on maintaining proper swing path for more consistent contact.",
                            "Practice follow-through to increase power and reduce errors.",
                            "Position yourself closer to the net for more effective volleys.",
                            "Improve anticipation and racket preparation for returns."
                        ])
                    },
                    {
                        "title": random.choice([
                            "Movement Efficiency", 
                            "Point Construction", 
                            "Net Game",
                            "Shot Selection",
                            "Recovery Position"
                        ]),
                        "description": random.choice([
                            "Improve split-step timing to enhance court coverage and response time.",
                            "Focus on strategic shot sequences to build pressure on opponent.",
                            "Develop better volley technique with proper racket positioning.",
                            "Make smarter choices based on court position and opponent location.",
                            "Work on returning to an optimal position after each shot."
                        ])
                    }
                ],
                "strengths": random.choice([
                    "Strong forehand and consistent first serve percentage. Good court coverage with effective movement patterns.",
                    "Excellent backhand technique with minimal errors. Strong serving performance with good placement variety.",
                    "Great net game with confident volleys. Solid mental approach with good point construction.",
                    "Powerful serve with high first serve percentage. Strong baseline game with effective shot selection.",
                    "Exceptional footwork and court positioning. Strong defensive skills and shot anticipation."
                ])
            },
            "data_source": {
                "type": "excel_file",
                "filename": filename,
                "has_basic_stats": has_basic_stats,
                "has_shot_analysis": has_shot_analysis,
                "has_movement_data": has_movement_data
            }
        }
        
    except Exception as e:
        logging.error(f"Error processing Excel file: {e}")
        # If there's an error, we still return sample data but note the error
        statistics = process_match_data([], match_id)
        statistics["data_source"] = {
            "type": "excel_file",
            "error": str(e),
            "filename": filename
        }
    
    finally:
        # Clean up temporary file
        if os.path.exists(temp_path):
            os.remove(temp_path)
    
    return statistics

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
