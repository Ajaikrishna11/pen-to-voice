const form = document.querySelector('form');
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const fileInput = document.querySelector('input[type="file"]');
  const file = fileInput.files;
  const formData = new FormData();
  formData.append('file', file);
  fetch('/upload', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    console.log(data);
  })
  .catch(error => {
    console.error(error);
  });
});