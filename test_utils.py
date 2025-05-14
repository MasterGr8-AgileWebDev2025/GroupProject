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

def test_generate_match_analysis_populates_keys():
    """
    Test if the generated match analysis data contains all keys.
    """
    statistics = {}
    result = generate_match_analysis(statistics)
    # Check top-level keys
    assert 'basic_stats' in result
    assert 'shot_analysis' in result
    assert 'player_movement' in result
    assert 'game_phases' in result
    assert 'strengths' in result
    assert 'areas_to_improve' in result

def test_generate_match_analysis_value_ranges():
    """
    Test if the function only contains values within expected ranges.
    """
    statistics = {}
    result = generate_match_analysis(statistics)
    bs = result['basic_stats']
    # Check value ranges for basic_stats
    assert 0 <= bs['aces'] <= 8
    assert 0 <= bs['double_faults'] <= 5
    assert 40 <= bs['first_serve_percentage'] <= 75
    assert 10 <= bs['first_serve_points_won'] <= 40
    assert 5 <= bs['second_serve_points_won'] <= 20
    assert 0 <= bs['break_points_saved'] <= 5
    assert bs['break_points_saved'] <= bs['break_points_faced'] <= bs['break_points_saved'] + 5
    assert 0 <= bs['break_points_converted'] <= bs['break_points_faced']
    assert 30 <= bs['total_points_won'] <= 70

def test_generate_match_analysis_strengths_and_areas():
    """
    Test if the strengths and areas to improve are non-empty strings.
    """
    statistics = {}
    result = generate_match_analysis(statistics)
    # Should always be non-empty strings
    assert isinstance(result['strengths'], str) and result['strengths'].strip()
    assert isinstance(result['areas_to_improve'], str) and result['areas_to_improve'].strip()
