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

function postComment() {
  
  commenterName = document.querySelector('#commenter-name').value
  commenterEmail = document.querySelector('#commenter-email').value
  commentBody = document.querySelector('#comment-body').value
  articleURL = document.querySelector('#article-url').innerText

  fetch('/post-comment', {
    method: "POST",
    body: JSON.stringify({
      commenterName: commenterName,
      commenterEmail: commenterEmail,
      commentBody: commentBody,
      articleURL: articleURL
    })
  })
  .then(response => response.json())
  .then(result => {
    console.log(result)
  })
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelector('#new-comment-button').onclick = displayNewComment

  document.querySelector("#less-comment-button").onclick = hideNewComment

  document.querySelector("#submit-comment-button").onclick = postComment
})
