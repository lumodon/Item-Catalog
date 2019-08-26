import mainToaster from '/static/toaster.js'

document.addEventListener('DOMContentLoaded', () => {
  const logoutBtn = document.querySelector('#logout')
  if(logoutBtn) {
    const logoutListener = logoutBtn.addEventListener('click', (e) => {
      e.preventDefault()

      // Prevent repeated logout attempts before callback completes
      logoutBtn.removeEventListener('click', logoutListener)

      // Prevent calls to protected routes
      // until signout completes. (prevent broken pipe error)
      const controlsEles = Array.from(document.querySelectorAll('.controls'))
      for(const controlsEle of controlsEles) {
        controlsEle.classList.add('hidden')
      }
      logoutBtn.innerText = 'Logging Out...'

      const auth2 = gapi.auth2.getAuthInstance()
      auth2.signOut()
        .then(() => {
          return fetch('/gdisconnect').then(res => res.json())
        })
        .then(() => {
          auth2.disconnect()
          window.location.reload(true)
          loggingOut = true
        })
        .catch(err => {
          console.error(err)
        })
    })
  }

  for (const msg of flashMessages) {
    mainToaster.pushMessage({type: 'notification', payload: {
      'message': msg,
    }})
  }
  window.sessionUser = sessionUserData || {
    'gplus_id': null,
    'picture': null,
    'token': null,
  }
  const container = document.querySelector('.google-image-container')
  // If no container then user is logged out
  if(container) {
    container.querySelector('.google-image').src = sessionUser.picture
    container.querySelector('.tooltip').innerText = sessionUser.token
  }
})
