search_box = document.getElementById('search_box')

search_box.addEventListener('input', function () {
    // Get the search query from the input field
    var search_query = this.value.toLowerCase();

    // Get all the rows in the table (except the header row)
    var rows = document.querySelectorAll('tbody tr');

    // Loop through all rows using a traditional for loop
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];

        // Get the title and description columns (index 1 and 2)
        var title = row.cells[1].textContent.toLowerCase();
        var description = row.cells[2].textContent.toLowerCase();

        // Check if either title or description matches the search query
        if (title.includes(search_query) || description.includes(search_query)) {
            row.style.display = ''; // Show the row if it matches the search
        } else {
            row.style.display = 'none'; // Hide the row if it doesn't match
        }
    }

});