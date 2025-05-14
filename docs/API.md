# API Reference

## Overview

The Tennis Analytics Platform provides a set of API endpoints for interacting with the frontend JavaScript. These APIs allow for fetching match statistics and support asynchronous page content updates.

## Authentication

All API endpoints require user authentication. Authentication is handled through Flask-Login using session cookies. Any unauthenticated request will receive an HTTP 401 (Unauthorized) response or be redirected to the login page.

## API Endpoints

### Get Match Statistics

Retrieve all statistics for a specific match.

**URL**: `/api/match/<match_id>/statistics`

**Method**: `GET`

**URL Parameters**:
- `match_id`: The unique identifier for the match

**Authorization**: Requires login, user must be the match owner or the match must be shared with the user

**Success Response**:
- **Code**: 200 OK
- **Content Example**:
```json
{
  "basic_stats": {
    "first_serve_percentage": 68,
    "first_serve_points_won": 75,
    "second_serve_points_won": 52,
    "aces": 8,
    "double_faults": 3
  },
  "shot_analysis": {
    "forehand": {
      "winners": 12,
      "errors": 8,
      "placement": {...}
    },
    "backhand": {
      "winners": 7,
      "errors": 10,
      "placement": {...}
    },
    "volley": {
      "winners": 5,
      "errors": 3,
      "placement": {...}
    }
  },
  "game_phases": {
    "preparation": {
      "score": 82,
      "details": {...}
    },
    "backswing": {
      "score": 75,
      "details": {...}
    },
    "contact": {
      "score": 68,
      "details": {...}
    },
    "follow_through": {
      "score": 78,
      "details": {...}
    }
  },
  "improvements": {
    "areas": [
      {
        "title": "Second Serve Stability",
        "description": "Improve second serve stability and confidence"
      },
      {
        "title": "Backhand Technique",
        "description": "Improve consistency and depth control on backhand shots"
      }
    ],
    "strengths": "Serve and forehand are your main weapons"
  }
}
```

**Error Responses**:
- **Code**: 404 Not Found
  - **Content**: Match with specified ID not found
- **Code**: 403 Forbidden
  - **Content**: User not authorized to access this match data

## Future API Extensions Planned

The following API endpoints are planned but not yet implemented:

### Get User Statistics Summary

Retrieve overall statistics summary for a user, displayed on the dashboard.

**URL**: `/api/user/statistics`

**Method**: `GET`

### Update Match Information

Update information for an existing match.

**URL**: `/api/match/<match_id>`

**Method**: `PUT`

### Delete Match

Delete a match and all its associated data.

**URL**: `/api/match/<match_id>`

**Method**: `DELETE`

### Filter Match History

Filter a user's match history by specified criteria.

**URL**: `/api/matches/filter`

**Method**: `GET`

**Query Parameters**:
- `date_range`: Date range (e.g., "this-month", "last-3-months")
- `opponent`: Opponent name
- `location`: Match location
- `result`: Match result (e.g., "win", "loss", "draw")

## Usage Guide

### Example: Fetching and Displaying Match Statistics

```javascript
// Fetch match statistics and update charts
function loadMatchStatistics(matchId) {
  fetch(`/api/match/${matchId}/statistics`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Unable to retrieve match statistics');
      }
      return response.json();
    })
    .then(data => {
      // Update charts with retrieved data
      renderShotDistributionChart(data.shot_analysis);
      renderPlayerMovementChart(data.movement_data);
      renderGamePhaseScores(data.game_phases);
      // ...other chart updates
    })
    .catch(error => {
      console.error('Error:', error);
      // Display error message
    });
}
```

## Tips and Best Practices

1. **Error Handling**: Always check API response status and handle errors appropriately
2. **Caching Strategy**: Consider caching frequently accessed data on the client side to reduce server load
3. **Batch Requests**: When possible, combine multiple small requests into a single larger request
4. **Pagination**: If returning large amounts of data, consider implementing pagination
5. **Security**: Don't store sensitive data on the client or trust client-side input