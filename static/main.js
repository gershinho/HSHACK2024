// main.js
$(document).ready(function() {
    $('form.ajax').on('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Create a FormData object from the form
        var formData = new FormData(this);
        var subjects = formData.get('subjects');
        var difficulty = formData.get('difficulty');

        // Validation checks
        if (subjects === null && difficulty === null) {
            $('#enter-all-fields').html('<p>Enter All Fields</p>');
            return false; // Stop the form submission
        } 
        else if (subjects === null) {
            $('#enter-all-fields').html('<p>Enter Subject</p>');
            return false; // Stop the form submission
        } 
        else if (difficulty === null) {
            $('#enter-all-fields').html('<p>Enter Difficulty</p>');
            return false; // Stop the form submission
        } 
        else {
            $('#enter-all-fields').html('<p></p>');

            // Send data to Flask route using Fetch API
            fetch('/', {
                method: 'POST',
                body: new URLSearchParams(formData), // Serialize the form data
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded' // Set content type
                }
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text(); // Assuming the server returns HTML
            })
            .then(html => {
                // Update the DOM with the new HTML content
                $('#submitted-values').html(html); // Update only the list of groups
            })
            .catch(error => {
                console.error('Error:', error);
                // Optionally, update the DOM to show an error message
                $('#submitted-values').html('<p>An Error Occurred</p>');
            });

            return true; // Proceed with form submission
        }
    });

    function updateValue(id) {
        var slider = document.getElementById("groupsize-input");
        var output = document.getElementById("groupsize-value");
        output.innerHTML = slider.value;
        slider.oninput = function() {
            output.innerHTML = this.value;
        };
    }

    updateValue('groupsize');
});
