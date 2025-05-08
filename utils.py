import random

# TODO: should probably add unit test here?

def calculate_overall_score(statistics):
    """
    Calculate the overall score based on various metrics in the analysis.
    Returns a value between 0 and 10.
    """
    # If statistics is empty, return default score
    if not statistics:
        return 7.5
    
    # Define weights for different components
    weights = {
        'technique': 0.3,
        'serve': 0.2,
        'ground_strokes': 0.3,
        'movement': 0.2
    }
    
    score = 0
    
    # Calculate technique score if game_phases exists
    if 'game_phases' in statistics:
        phases = statistics['game_phases']
        technique_scores = []
        
        if 'preparation' in phases and 'score' in phases['preparation']:
            technique_scores.append(phases['preparation']['score'] / 10)
        if 'contact' in phases and 'score' in phases['contact']:
            technique_scores.append(phases['contact']['score'] / 10)
        if 'backswing' in phases and 'score' in phases['backswing']:
            technique_scores.append(phases['backswing']['score'] / 10)
        if 'follow_through' in phases and 'score' in phases['follow_through']:
            technique_scores.append(phases['follow_through']['score'] / 10)
        
        if technique_scores:
            technique_score = sum(technique_scores) / len(technique_scores)
            score += technique_score * weights['technique']
    
    # Calculate serve score if basic_stats and shot_analysis exist
    serve_score = 0
    serve_factors = 0
    if 'basic_stats' in statistics:
        basic_stats = statistics['basic_stats']
        if 'aces' in basic_stats:
            serve_score += min(1.0, basic_stats['aces'] / 10)
            serve_factors += 1
        if 'double_faults' in basic_stats:
            serve_score += max(0, 1 - (basic_stats['double_faults'] / 10))
            serve_factors += 1
        if 'first_serve_percentage' in basic_stats:
            serve_score += basic_stats['first_serve_percentage'] / 100
            serve_factors += 1
        if 'first_serve_points_won' in basic_stats:
            serve_score += basic_stats['first_serve_points_won'] / 100
            serve_factors += 1
    
    if serve_factors > 0:
        score += (serve_score / serve_factors) * weights['serve']
    
    # Calculate ground strokes score
    stroke_score = 0
    stroke_factors = 0
    if 'shot_analysis' in statistics:
        shots = statistics['shot_analysis']
        if 'forehand' in shots:
            forehand = shots['forehand']
            if 'winners' in forehand and 'errors' in forehand:
                total = forehand['winners'] + forehand['errors']
                if total > 0:
                    ratio = forehand['winners'] / total
                    stroke_score += min(1.0, ratio * 2)  # A 50% winner ratio is perfect
                    stroke_factors += 1
        
        if 'backhand' in shots:
            backhand = shots['backhand']
            if 'winners' in backhand and 'errors' in backhand:
                total = backhand['winners'] + backhand['errors']
                if total > 0:
                    ratio = backhand['winners'] / total
                    stroke_score += min(1.0, ratio * 2)  # A 50% winner ratio is perfect
                    stroke_factors += 1
    
    if stroke_factors > 0:
        score += (stroke_score / stroke_factors) * weights['ground_strokes']
    
    # Calculate movement score
    if 'player_movement' in statistics:
        movement = statistics['player_movement']
        movement_score = 0
        movement_factors = 0
        
        # Simple calculation based on available metrics
        if 'sprints' in movement:
            movement_score += min(1.0, movement['sprints'] / 40)  # Assuming 40 sprints is excellent
            movement_factors += 1
        
        if 'direction_changes' in movement:
            movement_score += min(1.0, movement['direction_changes'] / 300)  # Assuming 300 direction changes is excellent
            movement_factors += 1
        
        if movement_factors > 0:
            score += (movement_score / movement_factors) * weights['movement']
    
    # Convert to 0-10 scale and ensure the score is between 0 and 10
    final_score = min(10, max(0, score * 10))
    
    # Round to one decimal place
    return round(final_score, 1)

def generate_match_analysis(statistics):
    """
    Generate match analysis data using AI (simulated for MVP).
    This would be replaced with actual AI analysis in production.
    """
    # Initialize basic stats if not present
    if 'basic_stats' not in statistics:
        statistics['basic_stats'] = {}
    
    # Simulate AI generating serve statistics
    statistics['basic_stats']['aces'] = random.randint(0, 8)
    statistics['basic_stats']['double_faults'] = random.randint(0, 5)
    statistics['basic_stats']['first_serve_percentage'] = round(random.uniform(40, 75), 1)
    statistics['basic_stats']['first_serve_points_won'] = random.randint(10, 40)
    statistics['basic_stats']['second_serve_points_won'] = random.randint(5, 20)
    statistics['basic_stats']['break_points_saved'] = random.randint(0, 5)
    statistics['basic_stats']['break_points_faced'] = random.randint(
        statistics['basic_stats']['break_points_saved'],
        statistics['basic_stats']['break_points_saved'] + 5
    )
    statistics['basic_stats']['break_points_converted'] = random.randint(0, statistics['basic_stats']['break_points_faced'])
    statistics['basic_stats']['total_points_won'] = random.randint(30, 70)
    
    # Initialize shot analysis if not present
    if 'shot_analysis' not in statistics:
        statistics['shot_analysis'] = {}
    
    # Add serve statistics to shot_analysis
    statistics['shot_analysis']['serve'] = {
        'speed': {
            'avg': round(random.uniform(90, 130), 1),
            'max': round(random.uniform(120, 150), 1),
            'min': round(random.uniform(70, 100), 1),
            'first_serve_avg': round(random.uniform(100, 140), 1),
            'second_serve_avg': round(random.uniform(80, 110), 1)
        },
        'placement': {
            'wide': random.randint(20, 40),
            'body': random.randint(20, 40),
            'tee': random.randint(20, 40)
        },
        'spin': {
            'flat': random.randint(30, 50),
            'slice': random.randint(20, 40),
            'kick': random.randint(20, 40)
        }
    }
    
    # Add volley statistics
    statistics['shot_analysis']['volley'] = {
        'winners': random.randint(2, 10),
        'errors': random.randint(1, 8),
        'placement': {
            'cross_court': random.randint(30, 50),
            'down_the_line': random.randint(20, 40),
            'middle': random.randint(10, 30)
        }
    }
    
    # Simulate AI generating stroke analysis
    statistics['shot_analysis']['forehand'] = {
        'winners': random.randint(5, 20),
        'errors': random.randint(5, 20),
        'speed': {
            'avg': round(random.uniform(60, 90), 1),
            'max': round(random.uniform(80, 110), 1)
        },
        'placement': {
            'cross_court': random.randint(40, 60),
            'down_the_line': random.randint(20, 40),
            'inside_out': random.randint(10, 30),
            'middle': random.randint(10, 30)
        }
    }
    
    statistics['shot_analysis']['backhand'] = {
        'winners': random.randint(2, 15),
        'errors': random.randint(5, 20),
        'speed': {
            'avg': round(random.uniform(50, 80), 1),
            'max': round(random.uniform(70, 100), 1)
        },
        'placement': {
            'cross_court': random.randint(40, 60),
            'down_the_line': random.randint(20, 40),
            'inside_out': random.randint(10, 30),
            'middle': random.randint(10, 30)
        }
    }
    
    # Initialize player movement if not present
    if 'player_movement' not in statistics:
        statistics['player_movement'] = {}
    
    # Simulate AI generating movement analysis
    statistics['player_movement']['distance_covered'] = round(random.uniform(1000, 5000), 1)
    statistics['player_movement']['sprints'] = random.randint(20, 50)
    statistics['player_movement']['direction_changes'] = random.randint(200, 400)
    
    # Initialize game phases if not present
    if 'game_phases' not in statistics:
        statistics['game_phases'] = {}
    
    # Simulate AI generating technical scores
    statistics['game_phases']['preparation'] = {
        'score': round(random.uniform(4, 9), 1),
        'body_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'racket_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'footwork': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'timing': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'grip_rating': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'stance_rating': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'shoulder_rotation': random.choice(['Excellent', 'Good', 'Needs Improvement'])
    }
    
    statistics['game_phases']['backswing'] = {
        'score': round(random.uniform(4, 9), 1),
        'body_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'racket_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'shoulder_rotation': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'timing': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'racket_path': random.choice(['Excellent', 'Good', 'Needs Improvement'])
    }
    
    statistics['game_phases']['contact'] = {
        'score': round(random.uniform(4, 9), 1),
        'body_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'racket_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'ball_contact': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'timing': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'accuracy': random.choice(['Excellent', 'Good', 'Needs Improvement'])
    }
    
    statistics['game_phases']['follow_through'] = {
        'score': round(random.uniform(4, 9), 1),
        'body_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'racket_position': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'recovery': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'timing': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'completion': random.choice(['Excellent', 'Good', 'Needs Improvement']),
        'balance': random.choice(['Excellent', 'Good', 'Needs Improvement'])
    }
    
    # Strengths and areas to improve based on scores
    strengths = []
    areas_to_improve = []
    
    # Check serve metrics
    if statistics['basic_stats']['aces'] > 5:
        strengths.append("Excellent serving power, generating a high number of aces.")
    elif statistics['basic_stats']['aces'] < 2:
        areas_to_improve.append("Work on serve placement and power to increase ace count.")
    
    if statistics['basic_stats']['double_faults'] > 4:
        areas_to_improve.append("Reduce double faults by focusing on consistent second serve technique.")
    elif statistics['basic_stats']['double_faults'] < 2:
        strengths.append("Consistent serving with minimal double faults.")
    
    if statistics['basic_stats']['first_serve_percentage'] > 65:
        strengths.append("Strong first serve percentage, giving you an advantage in points.")
    elif statistics['basic_stats']['first_serve_percentage'] < 50:
        areas_to_improve.append("Improve first serve consistency to gain more control in service games.")
    
    # Check stroke metrics
    if statistics['shot_analysis']['forehand']['winners'] > 15:
        strengths.append("Powerful forehand producing many winners.")
    if statistics['shot_analysis']['backhand']['winners'] > 10:
        strengths.append("Effective backhand generating consistent winners.")
    
    if statistics['shot_analysis']['forehand']['errors'] > 15:
        areas_to_improve.append("Reduce forehand unforced errors by improving technique and shot selection.")
    if statistics['shot_analysis']['backhand']['errors'] > 15:
        areas_to_improve.append("Focus on backhand consistency to reduce errors.")
    
    # Check technical scores
    if statistics['game_phases']['preparation']['score'] < 6:
        areas_to_improve.append("Improve preparation phase of your strokes.")
    if statistics['game_phases']['contact']['score'] < 6:
        areas_to_improve.append("Work on contact point consistency.")
    if statistics['game_phases']['follow_through']['score'] < 6:
        areas_to_improve.append("Focus on complete follow-through to improve shot power and control.")
    
    # Ensure we have at least one strength and one area to improve
    if not strengths:
        strengths.append("Good overall technique with balanced performance across different aspects of the game.")
    
    if not areas_to_improve:
        areas_to_improve.append("Continue refining your technique and tactical approach to elevate your game further.")
    
    # Add strengths and areas to improve to the statistics
    statistics['strengths'] = "\n".join(strengths)
    statistics['areas_to_improve'] = "\n".join(areas_to_improve)
    
    return statistics

