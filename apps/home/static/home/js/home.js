// ================= PRODUCT SLIDER (MANUAL NAVIGATION) =================
let slider = document.getElementById("productSlider");
let nextBtn = document.getElementById("nextBtn");
let prevBtn = document.getElementById("prevBtn");

let scrollAmount = 0; // Tracks the current scroll position
let cardWidth = 276;  // Width of a single product card

// Logic for the Next button
nextBtn.onclick = () => {
    scrollAmount += cardWidth; // Increase scroll distance
    slider.style.transform = `translateX(-${scrollAmount}px)`; // Move slider to the left
};

// Logic for the Previous button
prevBtn.onclick = () => {
    scrollAmount -= cardWidth; // Decrease scroll distance
    if(scrollAmount < 0) scrollAmount = 0; // Prevent scrolling past the first item
    slider.style.transform = `translateX(-${scrollAmount}px)`; // Move slider to the right
};


// MAIN HERO CAROUSEL (AUTO-PLAY)
document.addEventListener("DOMContentLoaded", function () {
    const carousel = document.getElementById("main-carousel");
    if (!carousel) return; // Exit if the carousel element is not found

    let index = 0; // Tracks the current slide number
    const totalSlides = carousel.children.length; // Total number of images/slides

    // Function to handle the slide transition
    function updateSlide() {
        // Move the carousel based on the current index (100% per slide)
        carousel.style.transform = `translateX(-${index * 100}%)`;
    }

    // Initialize the first slide
    updateSlide();

    // Set timer to switch slides automatically every 2 seconds (2000ms)
    setInterval(() => {
        index = (index + 1) % totalSlides; // Increment index and reset to 0 at the end
        updateSlide();
    }, 2000);
});