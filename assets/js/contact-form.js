/**
 * Contact Form Handler
 * Handles form submission with AJAX and validation
 */

document.addEventListener("DOMContentLoaded", function () {
  const contactForm = document.getElementById("contactForm");

  if (!contactForm) return;

  // Bootstrap form validation
  contactForm.addEventListener("submit", function (event) {
    event.preventDefault();
    event.stopPropagation();

    // Validate form
    if (!contactForm.checkValidity()) {
      contactForm.classList.add("was-validated");
      return;
    }

    // Form is valid, submit via AJAX
    submitContactForm();
  });

  // Remove validation class when user starts typing
  const inputs = contactForm.querySelectorAll(".form-control");
  inputs.forEach((input) => {
    input.addEventListener("input", function () {
      if (this.value.trim() !== "") {
        this.classList.remove("is-invalid");
      }
    });
  });
});

function submitContactForm() {
  const form = document.getElementById("contactForm");
  const submitBtn = document.getElementById("submitBtn");
  const loadingMsg = document.getElementById("loadingMessage");
  const errorMsg = document.getElementById("errorMessage");
  const errorText = document.getElementById("errorText");
  const successMsg = document.getElementById("successMessage");

  // Hide all messages
  loadingMsg.classList.add("d-none");
  errorMsg.classList.add("d-none");
  successMsg.classList.add("d-none");

  // Show loading
  loadingMsg.classList.remove("d-none");
  submitBtn.disabled = true;
  submitBtn.innerHTML = '<i class="bi bi-hourglass-split me-2"></i>Sending...';

  // Collect form data
  const formData = new FormData(form);

  // Send AJAX request
  fetch(form.action, {
    method: "POST",
    body: formData,
    headers: {
      "X-Requested-With": "XMLHttpRequest",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      loadingMsg.classList.add("d-none");

      if (data.success) {
        // Show success message
        successMsg.classList.remove("d-none");

        // Reset form
        form.reset();
        form.classList.remove("was-validated");

        // Reset button
        submitBtn.disabled = false;
        submitBtn.innerHTML =
          '<i class="bi bi-send-fill me-2"></i>Send Message';

        // Scroll to message
        successMsg.scrollIntoView({ behavior: "smooth", block: "nearest" });

        // Hide success message after 5 seconds
        setTimeout(() => {
          successMsg.classList.add("d-none");
        }, 5000);
      } else {
        // Show error message
        errorText.textContent =
          data.message || "An error occurred. Please try again.";
        errorMsg.classList.remove("d-none");

        // Reset button
        submitBtn.disabled = false;
        submitBtn.innerHTML =
          '<i class="bi bi-send-fill me-2"></i>Send Message';

        // Scroll to error
        errorMsg.scrollIntoView({ behavior: "smooth", block: "nearest" });
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      loadingMsg.classList.add("d-none");

      errorText.textContent =
        "Network error. Please check your connection and try again.";
      errorMsg.classList.remove("d-none");

      // Reset button
      submitBtn.disabled = false;
      submitBtn.innerHTML = '<i class="bi bi-send-fill me-2"></i>Send Message';

      // Scroll to error
      errorMsg.scrollIntoView({ behavior: "smooth", block: "nearest" });
    });
}
