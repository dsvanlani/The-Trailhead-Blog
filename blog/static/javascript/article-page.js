function displayNewComment() {
  document.querySelector("#new-comment-box").style.display = 'block'
  document.querySelector("#new-comment-button").style.display = 'none'
  document.querySelector("#less-comment-button").style.display = 'block'

  // Scroll down to it
  document.querySelector("#new-comment-box").scrollIntoView()
}

function hideNewComment() {
  document.querySelector("#new-comment-box").style.display = 'none'
  document.querySelector("#new-comment-button").style.display = 'block'
  document.querySelector("#less-comment-button").style.display = 'none'
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelector('#new-comment-button').onclick = displayNewComment

  document.querySelector("#less-comment-button").onclick = hideNewComment
})
