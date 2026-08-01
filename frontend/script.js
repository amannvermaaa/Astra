document.addEventListener('DOMContentLoaded', () => {
    
    // --- Mobile Menu Toggle ---
    const mobileMenu = document.getElementById('mobile-menu');
    const navLinks = document.querySelector('.nav-links');

    mobileMenu.addEventListener('click', () => {
        navLinks.classList.toggle('active');
    });

    // --- Navbar Scroll Effect ---
    const header = document.getElementById('navbar');
    const scrollContainer = document.querySelector('.scroll-container');

    scrollContainer.addEventListener('scroll', () => {
        if (scrollContainer.scrollTop > 50) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }
    });

    // --- Intersection Observer for Fade-In Animations ---
    const observerOptions = {
        root: scrollContainer,
        rootMargin: '0px',
        threshold: 0.3
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
            } else {
                // Optional: remove visible class if you want it to animate every time
                entry.target.classList.remove('visible');
            }
        });
    }, observerOptions);

    const fadeElements = document.querySelectorAll('.fade-in-up');
    fadeElements.forEach(el => observer.observe(el));


    // --- Form Submission to Backend ---
    const registrationForm = document.getElementById('registration-form');
    const formMessage = document.getElementById('form-message');
    const submitBtn = document.getElementById('submit-btn');

    registrationForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Disable button while processing
        submitBtn.disabled = true;
        submitBtn.textContent = "PROCESSING...";

        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            destination: document.getElementById('destination').value
        };

        try {
            // Send to our Python backend
            const response = await fetch('http://localhost:5000/api/register', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            const result = await response.json();

            if (response.ok) {
                formMessage.textContent = "Success! " + result.message;
                formMessage.className = "success-msg";
                registrationForm.reset();
            } else {
                formMessage.textContent = "Error: " + result.message;
                formMessage.className = "error-msg";
            }
        } catch (error) {
            console.error('Error submitting form:', error);
            formMessage.textContent = "Failed to connect to the server. Is the backend running?";
            formMessage.className = "error-msg";
        } finally {
            formMessage.classList.remove('hidden');
            submitBtn.disabled = false;
            submitBtn.textContent = "JOIN WAITLIST";
        }
    });

    // --- Parallax Background Effect ---
    document.addEventListener("mousemove", (e) => {
        // Calculate offset (adjust the 30 for more/less movement)
        const xOffset = (e.clientX / window.innerWidth - 0.5) * 30;
        const yOffset = (e.clientY / window.innerHeight - 0.5) * 30;
        
        document.querySelectorAll('.hero-section, .form-section').forEach(section => {
            section.style.backgroundPosition = `calc(50% + ${xOffset}px) calc(50% + ${yOffset}px)`;
        });
    });

});
