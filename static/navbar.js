import mainToaster from '/static/toaster.js'

document.addEventListener('DOMContentLoaded', () => {
  for (const msg of flashMessages) {
    mainToaster.pushMessage({type: 'notification', payload: {
      'message': msg,
    }})
  }
  const sessionUser = sessionUserData || {
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
