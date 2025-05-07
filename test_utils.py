from utils import *


def test_empty_statistics():
    """
    Test the calculate_overall_score function with empty statistics
    """
    result = calculate_overall_score({})
    assert result == 7.5, "Expected default score of 7.5 for empty statistics"


def test_calculate_overall_score_partial_technique():
    """
    Test with partial technique data
    """
    statistics = {
        'game_phases': {
            'preparation': {'score': 8},
            'contact': {'score': 6}
        }
    }
    result = calculate_overall_score(statistics)
    assert result == 2.1, "Score should be 2.1 and reflect partial technique data"


def test_calculate_overall_score_full_data():
    """
    Test with full data
    """ 
    statistics = {
        'game_phases': {
            'preparation': {'score': 8},
            'contact': {'score': 7},
            'backswing': {'score': 9},
            'follow_through': {'score': 6}
        },
        'basic_stats': {
            'aces': 5,
            'double_faults': 2,
            'first_serve_percentage': 70,
            'first_serve_points_won': 60
        },
        'shot_analysis': {
            'forehand': {'winners': 10, 'errors': 5},
            'backhand': {'winners': 8, 'errors': 4}
        },
        'player_movement': {
            'sprints': 30,
            'direction_changes': 200
        }
    }
    result = calculate_overall_score(statistics)
    assert 0 <= result <= 10, "Score should be within the range of 0 to 10"


def test_calculate_overall_score_no_basic_stats():
    # Test with no basic stats
    statistics = {
        'game_phases': {
            'preparation': {'score': 7},
            'contact': {'score': 8}
        },
        'shot_analysis': {
            'forehand': {'winners': 5, 'errors': 3},
            'backhand': {'winners': 4, 'errors': 2}
        }
    }
    result = calculate_overall_score(statistics)
    assert result == 5.2, "The result without basic stats should be 5.2"


class MockAnalysis:
    """
    A mock class to simulate the analysis object.
    """
    def __init__(self):
        self.aces = 0
        self.double_faults = 0
        self.first_serve_percentage = 0.0
        self.first_serve_points_won = 0
        self.second_serve_points_won = 0
        self.break_points_saved = 0
        self.break_points_faced = 0
        self.forehand_winners = 0
        self.backhand_winners = 0
        self.forehand_errors = 0
        self.backhand_errors = 0
        self.distance_covered = 0.0
        self.preparation_score = 0.0
        self.contact_score = 0.0
        self.follow_through_score = 0.0
        self.strengths = ""
        self.areas_to_improve = ""

def test_generate_match_analysis():
    """
    Test if the AI simulated algorithm generates match analysis data within the bounds.
    """
    # Arrange
    analysis = MockAnalysis()
    
    # Act
    result = generate_match_analysis(analysis)
    
    # Assert
    assert 0 <= result.aces <= 8, "Aces should be between 0 and 8"
    assert 0 <= result.double_faults <= 5, "Double faults should be between 0 and 5"
    assert 40 <= result.first_serve_percentage <= 75, "First serve percentage should be between 40 and 75"
    assert 5 <= result.second_serve_points_won <= 20, "Second serve points won should be between 5 and 20"
    assert 0 <= result.break_points_saved <= 5, "Break points saved should be between 0 and 5"
    assert 5 <= result.forehand_winners <= 20, "Forehand winners should be between 5 and 20"
    assert 2 <= result.backhand_winners <= 15, "Backhand winners should be between 2 and 15"
    assert 5 <= result.forehand_errors <= 20, "Forehand errors should be between 5 and 20"
    assert 5 <= result.backhand_errors <= 20, "Backhand errors should be between 5 and 20"
    assert 1000 <= result.distance_covered <= 5000, "Distance covered should be between 1000 and 5000"
    assert 4 <= result.preparation_score <= 9, "Preparation score should be between 4 and 9"
    assert 4 <= result.contact_score <= 9, "Contact score should be between 4 and 9"
    assert 4 <= result.follow_through_score <= 9, "Follow-through score should be between 4 and 9"
    assert result.strengths, "Strengths should not be empty"
    assert result.areas_to_improve, "Areas to improve should not be empty"
