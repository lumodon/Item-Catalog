import mainToaster from '/static/toaster.js'

document.addEventListener('DOMContentLoaded', () => {
  const logoutBtn = document.querySelector('#logout')
  if(logoutBtn) {
    logoutBtn.addEventListener('click', (e) => {
      e.preventDefault()
      const controlsEles = Array.from(document.querySelectorAll('.controls'))
      for(const controlsEle of controlsEles) {
        controlsEle.classList.add('hidden')
      }
      signOut()
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
