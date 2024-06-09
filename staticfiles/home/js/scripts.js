document.addEventListener('DOMContentLoaded', () => {
  // Function to handle sort form submission
  const sortForm = document.querySelector('.sort-options form');
  if (sortForm) {
      sortForm.addEventListener('change', () => {
          sortForm.submit();
      });
  }

  // Enhancing the search input functionality
  const searchForm = document.querySelector('.navbar form');
  if (searchForm) {
      const searchInput = searchForm.querySelector('input[name="q"]');
      searchInput.addEventListener('keypress', (event) => {
          if (event.key === 'Enter') {
              event.preventDefault();
              searchForm.submit();
          }
      });
  }

  // Adding animation to search results
  const searchResults = document.querySelectorAll('.search-results .container > div');
  searchResults.forEach((result, index) => {
      setTimeout(() => {
          result.classList.add('visible');
      }, index * 100); // Staggered animation
  });
});

// CSS for visibility animation (add this to your styles.css)
// .search-results .container > div {
//     opacity: 0;
//     transform: translateY(20px);
//     transition: opacity 0.3s ease, transform 0.3s ease;
// }
// .search-results .container > div.visible {
//     opacity: 1;
//     transform: translateY(0);
// }
