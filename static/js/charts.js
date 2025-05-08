/**
 * Charts.js - Tennis Analytics Data Visualization
 * This file contains functions for rendering tennis match data visualizations
 * using Chart.js library.
 */

// Initialize charts when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on an analysis page
    if (document.getElementById('shotDistributionChart')) {
        initializeCharts();
    }
});

// Function to initialize all charts
function initializeCharts() {
    // Get match ID from the data attribute
    const matchId = document.getElementById('match-data').dataset.matchId;
    
    // Fetch match statistics data
    fetch(`/api/match/${matchId}/statistics`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to fetch match data');
            }
            return response.json();
        })
        .then(data => {
            console.log('Match data loaded:', data);
            
            // Render each chart with the data
            renderShotDistributionChart(data);
            renderShotPlacementChart(data);
            renderPlayerMovementChart(data);
            renderGamePhaseScores(data);
            renderStatsComparisonChart(data);
            renderServeAnalysisChart(data);
        })
        .catch(error => {
            console.error('Error loading match data:', error);
            // Display error message to user
            document.getElementById('charts-container').innerHTML = `
                <div class="alert alert-danger">
                    <i class="fas fa-exclamation-triangle me-2"></i>
                    Failed to load match data. Please try refreshing the page.
                </div>
            `;
        });
}

// Render shot distribution pie chart
function renderShotDistributionChart(data) {
    const chartElement = document.getElementById('shotDistributionChart');
    if (!chartElement) return;
    
    try {
        // Extract shot data
        const shotData = {
            forehand: data.shot_analysis.forehand.winners + data.shot_analysis.forehand.errors,
            backhand: data.shot_analysis.backhand.winners + data.shot_analysis.backhand.errors,
            serve: Object.values(data.shot_analysis.serve.placement).reduce((a, b) => a + b, 0),
            volley: data.shot_analysis.volley.winners + data.shot_analysis.volley.errors
        };
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Forehand', 'Backhand', 'Serve', 'Volley'],
                datasets: [{
                    data: Object.values(shotData),
                    backgroundColor: [
                        '#17B169', // Tennis court green
                        '#2C5282', // Deep blue
                        '#F6AD55', // Orange
                        '#805AD5'  // Purple
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'right',
                    },
                    title: {
                        display: true,
                        text: 'Shot Distribution',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.label || '';
                                const value = context.raw || 0;
                                const total = context.dataset.data.reduce((a, b) => a + b, 0);
                                const percentage = Math.round((value / total) * 100);
                                return `${label}: ${value} (${percentage}%)`;
                            }
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering shot distribution chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display shot distribution chart</div>';
    }
}

// Render shot placement visualization
function renderShotPlacementChart(data) {
    const chartElement = document.getElementById('shotPlacementChart');
    if (!chartElement) return;
    
    try {
        // Extract placement data for forehand
        const forehandPlacement = data.shot_analysis.forehand.placement;
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: ['Cross Court', 'Down The Line', 'Inside Out'],
                datasets: [
                    {
                        label: 'Forehand',
                        data: [
                            forehandPlacement.cross_court,
                            forehandPlacement.down_the_line,
                            forehandPlacement.inside_out
                        ],
                        backgroundColor: 'rgba(23, 177, 105, 0.2)',
                        borderColor: '#17B169',
                        pointBackgroundColor: '#17B169',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#17B169'
                    },
                    {
                        label: 'Backhand',
                        data: [
                            data.shot_analysis.backhand.placement.cross_court,
                            data.shot_analysis.backhand.placement.down_the_line,
                            data.shot_analysis.backhand.placement.inside_out
                        ],
                        backgroundColor: 'rgba(44, 82, 130, 0.2)',
                        borderColor: '#2C5282',
                        pointBackgroundColor: '#2C5282',
                        pointBorderColor: '#fff',
                        pointHoverBackgroundColor: '#fff',
                        pointHoverBorderColor: '#2C5282'
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: {
                            display: true
                        },
                        suggestedMin: 0
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Shot Placement Analysis',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering shot placement chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display shot placement chart</div>';
    }
}

// Render player movement chart
function renderPlayerMovementChart(data) {
    const chartElement = document.getElementById('playerMovementChart');
    if (!chartElement) return;
    
    try {
        const movementData = data.player_movement;
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Distance Covered (m)', 'Sprints', 'Direction Changes'],
                datasets: [{
                    label: 'Movement Statistics',
                    data: [
                        movementData.distance_covered / 100, // Scale down for display
                        movementData.sprints,
                        movementData.direction_changes
                    ],
                    backgroundColor: [
                        'rgba(23, 177, 105, 0.7)', // Tennis court green
                        'rgba(44, 82, 130, 0.7)',  // Deep blue
                        'rgba(229, 62, 62, 0.7)'   // Accent red
                    ],
                    borderColor: [
                        '#17B169',
                        '#2C5282',
                        '#E53E3E'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Value',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Movement Metric',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Player Movement Analysis',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                const label = context.dataset.label || '';
                                let value = context.raw || 0;
                                
                                // Format the value based on the metric
                                if (context.dataIndex === 0) {
                                    value = value * 100; // Scale back up
                                    return `${label}: ${value} meters`;
                                } else if (context.dataIndex === 1) {
                                    return `${label}: ${value} sprints`;
                                } else {
                                    return `${label}: ${value} changes`;
                                }
                            }
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering player movement chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display player movement chart</div>';
    }
}

// Render game phase scores chart
function renderGamePhaseScores(data) {
    const chartElement = document.getElementById('gamePhaseScoresChart');
    if (!chartElement) return;
    
    try {
        const phaseData = data.game_phases;
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Preparation', 'Backswing', 'Contact', 'Follow Through'],
                datasets: [{
                    label: 'Phase Score',
                    data: [
                        phaseData.preparation.score,
                        phaseData.backswing.score,
                        phaseData.contact.score,
                        phaseData.follow_through.score
                    ],
                    backgroundColor: 'rgba(23, 177, 105, 0.2)',
                    borderColor: '#17B169',
                    borderWidth: 2,
                    pointBackgroundColor: '#17B169',
                    pointBorderColor: '#fff',
                    pointRadius: 5,
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        max: 100,
                        title: {
                            display: true,
                            text: 'Score',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Stroke Phase',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Stroke Phase Analysis',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering game phase scores chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display game phase scores chart</div>';
    }
}

// Render basic stats comparison chart
function renderStatsComparisonChart(data) {
    const chartElement = document.getElementById('statsComparisonChart');
    if (!chartElement) return;
    
    try {
        const basicStats = data.basic_stats;
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'radar',
            data: {
                labels: [
                    'First Serve %', 
                    'First Serve Won %', 
                    'Second Serve Won %', 
                    'Break Points Saved %', 
                    'Break Points Converted %'
                ],
                datasets: [{
                    label: 'Your Performance',
                    data: [
                        basicStats.first_serve_percentage,
                        basicStats.first_serve_points_won,
                        basicStats.second_serve_points_won,
                        basicStats.break_points_saved * 20, // Scale for visibility
                        basicStats.break_points_converted * 20 // Scale for visibility
                    ],
                    backgroundColor: 'rgba(23, 177, 105, 0.2)',
                    borderColor: '#17B169',
                    pointBackgroundColor: '#17B169',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    r: {
                        angleLines: {
                            display: true
                        },
                        suggestedMin: 0,
                        suggestedMax: 100
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Performance Metrics',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering stats comparison chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display stats comparison chart</div>';
    }
}

// Render serve analysis chart
function renderServeAnalysisChart(data) {
    const chartElement = document.getElementById('serveAnalysisChart');
    if (!chartElement) return;
    
    try {
        const serveData = data.shot_analysis.serve;
        
        const ctx = chartElement.getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Wide', 'Body', 'T'],
                datasets: [{
                    label: 'Serve Placement',
                    data: [
                        serveData.placement.wide,
                        serveData.placement.body,
                        serveData.placement.t
                    ],
                    backgroundColor: [
                        'rgba(23, 177, 105, 0.7)',
                        'rgba(44, 82, 130, 0.7)',
                        'rgba(246, 173, 85, 0.7)'
                    ],
                    borderColor: [
                        '#17B169',
                        '#2C5282',
                        '#F6AD55'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                indexAxis: 'y',
                scales: {
                    x: {
                        beginAtZero: true,
                        title: {
                            display: true,
                            text: 'Count',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    },
                    y: {
                        title: {
                            display: true,
                            text: 'Placement',
                            font: {
                                family: 'Roboto'
                            }
                        }
                    }
                },
                plugins: {
                    title: {
                        display: true,
                        text: 'Serve Placement Analysis',
                        font: {
                            family: 'Inter',
                            size: 16,
                            weight: 'bold'
                        }
                    }
                }
            }
        });
    } catch (error) {
        console.error('Error rendering serve analysis chart:', error);
        chartElement.parentNode.innerHTML = '<div class="alert alert-warning">Could not display serve analysis chart</div>';
    }
}
