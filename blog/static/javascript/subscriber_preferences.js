function savePreferences() {
    const name = document.querySelector('#subscriber-preference-name').value
    const email = document.querySelector('#subscriber-preference-email').value
    const active = document.querySelector('#subscriber-active-switch').checked
    console.log(active)
    // TODO: make a fetch call to update Preferences
    fetch('/subscriptions/save-preferences', {
      method: 'POST',
      body: JSON.stringify({
        name: name,
        email: email,
        active: active
      })
    })
    .then(response => response.json())
    .then(result => {
      console.log(result.message)
      if (result.message == 'success') {
        document.querySelector('#save-message').innerText = "Saved!"
        document.querySelector('#error-message').innerText = ""
      } else {
        document.querySelector('#save-message').innerText = ""
        document.querySelector('#error-message').innerText = result.errorMessage
      }
    })
}

document.addEventListener("DOMContentLoaded", () => {
    // Configure save button
    document.querySelector('#save-button').onclick = savePreferences
})
