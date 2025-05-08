/**
 * Upload.js - Handles tennis match data upload functionality
 */

document.addEventListener('DOMContentLoaded', function() {
	// Check if we're on the upload page
	const uploadForm = document.getElementById('uploadForm');
	if (!uploadForm) return;

	// File upload preview
	const fileInput = document.getElementById('files');
	const filePreview = document.getElementById('filePreview');

	if (fileInput && filePreview) {
		fileInput.addEventListener('change', updateFilePreview);
	}

	function updateFilePreview() {
		filePreview.innerHTML = '';

		if (fileInput.files.length > 0) {
			const fileList = document.createElement('div');
			fileList.classList.add('list-group', 'mt-3');

			for (let i = 0; i < fileInput.files.length; i++) {
				const file = fileInput.files[i];
				const fileItem = document.createElement('div');
				fileItem.classList.add('list-group-item', 'd-flex', 'justify-content-between', 'align-items-center');

				// File icon based on type
				let fileIcon = 'fas fa-file';
				if (file.type.startsWith('image/')) {
					fileIcon = 'fas fa-file-image';
				} else if (file.type.startsWith('video/')) {
					fileIcon = 'fas fa-file-video';
				} else if (file.type.startsWith('text/')) {
					fileIcon = 'fas fa-file-alt';
				} else if (file.type.startsWith('application/')) {
					fileIcon = 'fas fa-file-code';
				}

				// File size formatting
				const fileSize = formatFileSize(file.size);

				fileItem.innerHTML = `
                    <div>
                        <i class="${fileIcon} me-2 text-secondary"></i>
                        <span>${file.name}</span>
                    </div>
                    <span class="badge bg-secondary">${fileSize}</span>
                `;

				fileList.appendChild(fileItem);
			}

			filePreview.appendChild(fileList);

			// Add a clear button
			const clearButton = document.createElement('button');
			clearButton.classList.add('btn', 'btn-sm', 'btn-outline-secondary', 'mt-2');
			clearButton.textContent = 'Clear Files';
			clearButton.addEventListener('click', function(e) {
				e.preventDefault();
				fileInput.value = '';
				updateFilePreview();
			});

			filePreview.appendChild(clearButton);
		}
	}

	function formatFileSize(bytes) {
		if (bytes < 1024) {
			return bytes + ' B';
		} else if (bytes < 1024 * 1024) {
			return (bytes / 1024).toFixed(1) + ' KB';
		} else if (bytes < 1024 * 1024 * 1024) {
			return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
		} else {
			return (bytes / (1024 * 1024 * 1024)).toFixed(1) + ' GB';
		}
	}

	// Date picker enhancement
	const dateInput = document.getElementById('date');
	if (dateInput) {
		// Set default value to today
		const today = new Date();
		const yyyy = today.getFullYear();
		let mm = today.getMonth() + 1;
		let dd = today.getDate();

		if (dd < 10) dd = '0' + dd;
		if (mm < 10) mm = '0' + mm;

		const formattedToday = yyyy + '-' + mm + '-' + dd;
		dateInput.value = formattedToday;

		// Make sure mobile devices show the date picker when clicked
		dateInput.addEventListener('click', function() {
			this.showPicker();
		});
	}

	// Form validation
	uploadForm.addEventListener('submit', function(e) {
		if (!this.checkValidity()) {
			e.preventDefault();
			e.stopPropagation();
		}

		this.classList.add('was-validated');

		// Show loading spinner on valid submit
		if (this.checkValidity()) {
			const submitButton = document.getElementById('submitButton');
			const loadingSpinner = document.getElementById('loadingSpinner');

			if (submitButton && loadingSpinner) {
				submitButton.disabled = true;
				submitButton.innerHTML = `
                    <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>
                    Uploading...
                `;
				loadingSpinner.classList.remove('d-none');
			}
		}
	});

	// Opponent autocomplete with dummy data for MVP
	const opponentInput = document.getElementById('opponent');
	if (opponentInput) {
		// Sample opponent data
		const opponents = [
			'Roger Federer',
			'Rafael Nadal',
			'Novak Djokovic',
			'Andy Murray',
			'Serena Williams',
			'Venus Williams',
			'Maria Sharapova',
			'Naomi Osaka',
			'Simona Halep',
			'John Smith',
			'Jane Doe',
			'Michael Johnson',
			'Sarah Davis',
			'David Wilson',
			'Emily Brown'
		];

		// Initialize a basic autocomplete
		let currentFocus;

		opponentInput.addEventListener('input', function() {
			const val = this.value;

			// Close any already open lists
			closeAllLists();

			if (!val) { return false; }
			currentFocus = -1;

			// Create a div element that will contain the items
			const dropdownDiv = document.createElement('div');
			dropdownDiv.setAttribute('id', this.id + 'autocomplete-list');
			dropdownDiv.setAttribute('class', 'autocomplete-items');

			// Append the DIV element as a child of the autocomplete container
			this.parentNode.appendChild(dropdownDiv);

			// For each item in the array
			for (let i = 0; i < opponents.length; i++) {
				// Check if the item starts with the same letters as the text field value
				if (opponents[i].toUpperCase().includes(val.toUpperCase())) {
					const itemDiv = document.createElement('div');

					// Make the matching letters bold
					const regex = new RegExp(val, 'gi');
					itemDiv.innerHTML = opponents[i].replace(regex, match => `<strong>${match}</strong>`);

					// Insert a input field that will hold the current array item's value
					itemDiv.innerHTML += `<input type='hidden' value='${opponents[i]}'>`;

					// Execute when someone clicks on the item value
					itemDiv.addEventListener('click', function() {
						opponentInput.value = this.getElementsByTagName('input')[0].value;
						closeAllLists();
					});

					dropdownDiv.appendChild(itemDiv);
				}
			}
		});

		// Close all autocomplete lists except the one passed as an argument
		function closeAllLists(elmnt) {
			const x = document.getElementsByClassName('autocomplete-items');
			for (let i = 0; i < x.length; i++) {
				if (elmnt != x[i] && elmnt != opponentInput) {
					x[i].parentNode.removeChild(x[i]);
				}
			}
		}

		// Close the list when someone clicks outside
		document.addEventListener('click', function(e) {
			closeAllLists(e.target);
		});
	}
});
