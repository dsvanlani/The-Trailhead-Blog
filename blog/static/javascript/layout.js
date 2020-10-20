function subscribeFetch() {
  // get the form data
  const name = document.querySelector('#subscriber-name').value
  const email = document.querySelector('#subscriber-email').value

  // Make a fetch to add to the database
  fetch('/subscriptions/add_subscriber', {
  method: 'POST',
  body: JSON.stringify({
    name: name,
    email: email
    })
})
.then(response => response.json())
.then(result => {
  console.log(result.message)
  if (result.message == "error") {
    document.querySelector('#subscriber-error-message').innerText = result.errorMessage
  } else {
    document.querySelector('#subscriber-modal-form').style.display = "none"
    document.querySelector('#subscriber-modal-success-view').style.display = "block"
  }
  })
}

document.addEventListener("DOMContentLoaded", () => {
    // Configure Subscriber button
    document.querySelector("#subscribe-button").onclick = subscribeFetch

})
