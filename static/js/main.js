// Initialize profile dropdown and navigation scroll effects once the DOM is ready
document.addEventListener("DOMContentLoaded", function () {

  // Select the profile button, dropdown menu, and the small arrow icon
  const btn = document.getElementById("profileBtn");
  const menu = document.getElementById("dropdownMenu");
  const chevron = document.getElementById("profileChevron");

  // Check if all elements exist before adding event listeners
  if (btn && menu && chevron) {
    // Toggle the menu visibility and arrow rotation when the button is clicked
    btn.addEventListener("click", function () {
      menu.classList.toggle("hidden");
      chevron.classList.toggle("rotate-180");
    });

    // Close the dropdown menu if the user clicks anywhere else on the screen
    window.addEventListener("click", function (e) {
      if (!btn.contains(e.target) && !menu.contains(e.target)) {
        menu.classList.add("hidden");
        chevron.classList.remove("rotate-180");
      }
    });
  }

});

// Scroll listener to adjust the category navigation bar density
document.addEventListener("DOMContentLoaded", function () {

  // Detect when the window is scrolled
  window.addEventListener("scroll", function () {
    // Select navigation images, text labels, and the main navigation container
    const images = document.querySelectorAll(".nav-img");
    const texts = document.querySelectorAll(".nav-text");
    const nav = document.getElementById("categoryNav");

    // Condense navigation elements when scrolled down more than 50 pixels
    if (window.scrollY > 50) {

      // Hide and shrink the icons to save vertical space
      images.forEach(img => {
        img.style.transform = "scale(0)"; // Shrinks the icon to nothing
        img.style.opacity = "0";          // Fades out the icon
        img.style.height = "0px";         // Collapses the height
      });

      // Tighten the padding and margins of the category text
      texts.forEach(txt => {
        txt.style.marginTop = "0px";
        txt.style.paddingTop = "5px";
        txt.style.paddingBottom = "3px";
      });

      // Reduce the overall padding of the navigation container
      if (nav) {
        nav.style.paddingTop = "5px";
        nav.style.paddingBottom = "5px";
      }

    } else {
      // Restore the full icons and original spacing when at the top of the page
      images.forEach(img => {
        img.style.transform = "scale(1)"; // Back to full size
        img.style.opacity = "1";          // Fully visible
        img.style.height = "28px";        // Standard height (h-7 equivalent)
      });

      // Reset the text labels to their original layout
      texts.forEach(txt => {
        txt.style.marginTop = "0px";
        txt.style.paddingTop = "0px";
        txt.style.paddingBottom = "0px";
      });

      // Restore the original padding to the navigation container
      if (nav) {
        nav.style.paddingTop = "8px";
        nav.style.paddingBottom = "8px";
      }
    }
  });
});