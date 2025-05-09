/**
 * Main JavaScript file for Tennis Analytics Platform
 */

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]');
    const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl));
    
    // Initialize popovers
    const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
    const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));
    
    // Flash message auto-dismiss
    const flashMessages = document.querySelectorAll('.alert-dismissible');
    flashMessages.forEach(message => {
        setTimeout(() => {
            const closeButton = message.querySelector('.btn-close');
            if (closeButton) {
                closeButton.click();
            }
        }, 5000); // Dismiss after 5 seconds
    });
    
    // Handle navigation active state
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('.nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath || 
            (linkPath !== '/' && currentPath.startsWith(linkPath))) {
            link.classList.add('active');
        }
    });
    
    // Dynamic date picker initialization
    const datePickers = document.querySelectorAll('.date-picker');
    if (datePickers.length > 0) {
        datePickers.forEach(picker => {
            picker.addEventListener('focus', function() {
                this.type = 'date';
                this.showPicker();
            });
            
            picker.addEventListener('blur', function() {
                if (!this.value) {
                    this.type = 'text';
                }
            });
        });
    }
    
    // Share match functionality
    const shareButtons = document.querySelectorAll('.share-match-btn');
    if (shareButtons.length > 0) {
        shareButtons.forEach(button => {
            button.addEventListener('click', function() {
                const matchId = this.getAttribute('data-match-id');
                window.location.href = `/share?match_id=${matchId}`;
            });
        });
    }
    
    // Form validation enhancement
    const forms = document.querySelectorAll('.needs-validation');
    
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            
            form.classList.add('was-validated');
        }, false);
    });
    
    // Password strength meter
    const passwordField = document.getElementById('password');
    const passwordStrengthMeter = document.getElementById('password-strength-meter');
    
    if (passwordField && passwordStrengthMeter) {
        passwordField.addEventListener('input', function() {
            const strength = calculatePasswordStrength(this.value);
            updatePasswordStrengthMeter(strength);
        });
    }
    
    function calculatePasswordStrength(password) {
        // Simple password strength calculation
        let strength = 0;
        
        if (password.length >= 8) strength += 1;
        if (password.match(/[a-z]+/)) strength += 1;
        if (password.match(/[A-Z]+/)) strength += 1;
        if (password.match(/[0-9]+/)) strength += 1;
        if (password.match(/[^a-zA-Z0-9]+/)) strength += 1;
        
        return strength;
    }
    
    function updatePasswordStrengthMeter(strength) {
        const meter = document.getElementById('password-strength-meter');
        const text = document.getElementById('password-strength-text');
        
        if (!meter || !text) return;
        
        // Update the meter
        meter.value = strength;
        
        // Update the text
        let strengthText = '';
        let strengthClass = '';
        
        switch (strength) {
            case 0:
            case 1:
                strengthText = 'Weak';
                strengthClass = 'text-danger';
                break;
            case 2:
                strengthText = 'Fair';
                strengthClass = 'text-warning';
                break;
            case 3:
                strengthText = 'Good';
                strengthClass = 'text-info';
                break;
            case 4:
                strengthText = 'Strong';
                strengthClass = 'text-success';
                break;
            case 5:
                strengthText = 'Very Strong';
                strengthClass = 'text-success';
                break;
        }
        
        text.textContent = strengthText;
        text.className = strengthClass;
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.testimonial-carousel');
    if (!carousel) return;

    // Pause animation on mouse enter
    carousel.addEventListener('mouseenter', function() {
        this.style.animationPlayState = 'paused';
    });

    // Resume animation on mouse leave
    carousel.addEventListener('mouseleave', function() {
        this.style.animationPlayState = 'running';
    });

    // For touch devices
    carousel.addEventListener('touchstart', function() {
        this.style.animationPlayState = 'paused';
    });

    carousel.addEventListener('touchend', function() {
        this.style.animationPlayState = 'running';
    });
});

/**
 * Hero Title Animation
 *
 * This script creates a letter-by-letter reveal animation for the hero title.
 * Each letter of the title appears sequentially with a slight delay between them,
 * creating a typing-like effect.
 *
 * The title text is taken from the 'data-text' attribute of the hero-title element,
 * and each letter is wrapped in a span with the 'letter' class for individual animation.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Get the hero title element
    const heroTitle = document.querySelector('.hero-title');

    // Exit if hero title doesn't exist on the page
    if (!heroTitle) return;

    // Get the original text from data-text attribute
    const originalText = heroTitle.getAttribute('data-text');

    // Clear the title content to prepare for animation
    heroTitle.innerHTML = '';

    // Split the title into two roughly equal lines
    const words = originalText.split(' ');
    const totalWords = words.length;
    const midPoint = Math.ceil(totalWords / 2);

    // First line (first half of the words)
    const firstLine = words.slice(0, midPoint).join(' ');

    // Second line (second half of the words)
    const secondLine = words.slice(midPoint).join(' ');

    // Process first line - create span for EACH CHARACTER (including spaces)
    for (let i = 0; i < firstLine.length; i++) {
        const letter = document.createElement('span');
        letter.className = 'letter';

        // Preserve spaces (using non-breaking space for visibility)
        if (firstLine[i] === ' ') {
            letter.innerHTML = '&nbsp;';
        } else {
            letter.textContent = firstLine[i];
        }

        heroTitle.appendChild(letter);
    }

    // Add line break between the two lines
    heroTitle.appendChild(document.createElement('br'));

    // Process second line - create span for EACH CHARACTER (including spaces)
    for (let i = 0; i < secondLine.length; i++) {
        const letter = document.createElement('span');
        letter.className = 'letter';

        // Preserve spaces (using non-breaking space for visibility)
        if (secondLine[i] === ' ') {
            letter.innerHTML = '&nbsp;';
        } else {
            letter.textContent = secondLine[i];
        }

        heroTitle.appendChild(letter);
    }

    // Get all letter elements for animation
    const letters = heroTitle.querySelectorAll('.letter');

    // Set delay between each letter appearance (in milliseconds)
    let letterDelay = 30; // Adjust this value to control animation speed

    // Animate each letter with incremental delay
    letters.forEach((letter, index) => {
        setTimeout(() => {
            letter.classList.add('visible');
        }, index * letterDelay);
    });
});

/**
 * Fade-in Animation
 *
 * This script handles fade-in animations for elements as they enter the viewport.
 * All elements will fade in from bottom to top with a slight upward movement.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Get all elements with fade-in animations
    const fadeElements = document.querySelectorAll('.fade-in, .fade-in-card');

    // If no elements found, exit
    if (fadeElements.length === 0) return;

    // Check if element is in viewport and should be animated
    function checkFadeElements() {
        const triggerBottom = window.innerHeight * 0.85;

        fadeElements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;

            if (elementTop < triggerBottom) {
                element.classList.add('visible');
            }
        });
    }

    // Listen for scroll events
    window.addEventListener('scroll', checkFadeElements);

    // Check on initial load
    checkFadeElements();

    // Also check after a short delay
    setTimeout(checkFadeElements, 300);
});