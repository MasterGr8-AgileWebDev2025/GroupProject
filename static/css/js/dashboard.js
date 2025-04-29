/**
 * Dashboard.js - Handles tennis dashboard visualization and interactions
 */

document.addEventListener('DOMContentLoaded', function() {
    // Check if we're on the dashboard page
    if (!document.getElementById('dashboard-page')) return;
    
    // Initialize charts if they exist
    if (document.getElementById('performanceTrendChart')) {
        initializePerformanceTrendChart();
    }
    
    if (document.getElementById('winLossChart')) {
        initializeWinLossChart();
    }
    
    if (document.getElementById('recentMatchesChart')) {
        initializeRecentMatchesChart();
    }
    
    // Handle match card click for details view
    const matchCards = document.querySelectorAll('.match-card');
    matchCards.forEach(card => {
        card.addEventListener('click', function() {
            const matchId = this.getAttribute('data-match-id');
            window.location.href = `/match/${matchId}`;
        });
    });
    
    // Initialize filter controls
    initializeFilters();
});

// Performance trend chart initialization
function initializePerformanceTrendChart() {
    const ctx = document.getElementById('performanceTrendChart').getContext('2d');
    
    // Sample data - in a real app, this would come from the server
    const performanceData = {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        datasets: [
            {
                label: 'First Serve %',
                data: [65, 68, 64, 70, 72, 75],
                borderColor: '#17B169',
                backgroundColor: 'rgba(23, 177, 105, 0.1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            },
            {
                label: 'Winners',
                data: [15, 17, 20, 18, 22, 25],
                borderColor: '#2C5282',
                backgroundColor: 'rgba(44, 82, 130, 0.1)',
                borderWidth: 2,
                tension: 0.4,
                fill: true
            }
        ]
    };
    
    new Chart(ctx, {
        type: 'line',
        data: performanceData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Performance Trends (Last 6 Months)',
                    font: {
                        family: 'Inter',
                        size: 16,
                        weight: 'bold'
                    }
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                },
                legend: {
                    position: 'top',
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'IBM Plex Mono'
                        }
                    }
                },
                x: {
                    ticks: {
                        font: {
                            family: 'Roboto'
                        }
                    }
                }
            }
        }
    });
}

// Win/Loss chart initialization
function initializeWinLossChart() {
    const ctx = document.getElementById('winLossChart').getContext('2d');
    
    // Sample data - in a real app, this would come from the server
    const winLossData = {
        labels: ['Wins', 'Losses'],
        datasets: [{
            data: [15, 7],
            backgroundColor: [
                '#17B169', // Green for wins
                '#E53E3E'  // Red for losses
            ],
            borderWidth: 0,
            hoverOffset: 4
        }]
    };
    
    new Chart(ctx, {
        type: 'doughnut',
        data: winLossData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Win/Loss Record',
                    font: {
                        family: 'Inter',
                        size: 16,
                        weight: 'bold'
                    }
                },
                legend: {
                    position: 'bottom'
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
            },
            cutout: '70%'
        }
    });
}

// Recent matches performance chart
function initializeRecentMatchesChart() {
    const ctx = document.getElementById('recentMatchesChart').getContext('2d');
    
    // Sample data - in a real app, this would come from the server
    const recentMatchesData = {
        labels: ['vs Smith', 'vs Jones', 'vs Williams', 'vs Brown', 'vs Davis'],
        datasets: [
            {
                label: 'Winners',
                data: [18, 25, 15, 20, 22],
                backgroundColor: '#17B169',
                stack: 'Stack 0'
            },
            {
                label: 'Unforced Errors',
                data: [15, 12, 20, 16, 14],
                backgroundColor: '#E53E3E',
                stack: 'Stack 0'
            }
        ]
    };
    
    new Chart(ctx, {
        type: 'bar',
        data: recentMatchesData,
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Recent Matches Performance',
                    font: {
                        family: 'Inter',
                        size: 16,
                        weight: 'bold'
                    }
                },
                legend: {
                    position: 'top'
                },
                tooltip: {
                    mode: 'index',
                    intersect: false
                }
            },
            scales: {
                x: {
                    stacked: false,
                    ticks: {
                        font: {
                            family: 'Roboto'
                        }
                    }
                },
                y: {
                    stacked: false,
                    beginAtZero: true,
                    ticks: {
                        font: {
                            family: 'IBM Plex Mono'
                        }
                    }
                }
            }
        }
    });
}

// Initialize filter controls
function initializeFilters() {
    const filterControls = document.querySelectorAll('.filter-control');
    if (!filterControls.length) return;
    
    filterControls.forEach(control => {
        control.addEventListener('change', function() {
            // In a real app, this would trigger an AJAX request to filter data
            console.log('Filter changed:', this.id, 'Value:', this.value);
            
            // Show loading indicator
            const loadingIndicator = document.getElementById('loading-indicator');
            if (loadingIndicator) {
                loadingIndicator.classList.remove('d-none');
            }
            
            // Simulate loading delay
            setTimeout(() => {
                // Hide loading indicator
                if (loadingIndicator) {
                    loadingIndicator.classList.add('d-none');
                }
                
                // Update page heading to show active filters
                updateActiveFilters();
            }, 800);
        });
    });
}

// Update the active filters display
function updateActiveFilters() {
    const filterControls = document.querySelectorAll('.filter-control');
    const activeFiltersContainer = document.getElementById('active-filters');
    
    if (!activeFiltersContainer) return;
    
    // Clear existing filters
    activeFiltersContainer.innerHTML = '';
    
    // Collect active filters
    const activeFilters = [];
    filterControls.forEach(control => {
        if (control.value && control.value !== 'all') {
            const filterName = control.previousElementSibling.textContent;
            const filterValue = control.value;
            
            activeFilters.push({
                name: filterName,
                value: filterValue
            });
        }
    });
    
    // Display active filters
    if (activeFilters.length > 0) {
        activeFiltersContainer.classList.remove('d-none');
        
        activeFilters.forEach(filter => {
            const badge = document.createElement('span');
            badge.classList.add('badge', 'bg-secondary', 'me-2');
            badge.textContent = `${filter.name}: ${filter.value}`;
            
            // Add remove button
            const removeBtn = document.createElement('button');
            removeBtn.classList.add('btn-close', 'btn-close-white', 'ms-1');
            removeBtn.setAttribute('aria-label', 'Remove filter');
            removeBtn.style.fontSize = '0.5rem';
            
            removeBtn.addEventListener('click', function() {
                // Find the corresponding filter control and reset it
                filterControls.forEach(control => {
                    if (control.previousElementSibling.textContent === filter.name) {
                        control.value = 'all';
                        // Trigger the change event
                        const event = new Event('change');
                        control.dispatchEvent(event);
                    }
                });
            });
            
            badge.appendChild(removeBtn);
            activeFiltersContainer.appendChild(badge);
        });
    } else {
        activeFiltersContainer.classList.add('d-none');
    }
}
