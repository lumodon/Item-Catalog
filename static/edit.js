import Toaster from '/static/toaster.js'

const TOASTER_DURATION = 3000

function validateContent(container) {
  const validateWithError = err => ({
    valid: false,
    component: valEle,
    error: err,
  })

  for (const valEle of container.querySelectorAll('.value')) {
    if (!valEle.value) {
      return validateWithError('Empty input')
    } else if (valEle.classList.contains('price') && isNaN(valEle.value)) {
      return validateWithError('Price is not a valid number')
    }
  }
  return { valid: true }
}

function fetchEdit(payload) {
  fetch('', {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
}

document.addEventListener('DOMContentLoaded', () => {
  const toaster = new Toaster({
    toasterElement: document.querySelector('.toaster'),
    duration: TOASTER_DURATION, /* TODO: need SASS for SSOT */
  })
  toaster.pushMessage({type: 'notification', payload: {message: 'Test 1'}})
  toaster.pushMessage({type: 'notification', payload: {message: 'Test 2'}})
  toaster.pushMessage({type: 'notification', payload: {message: 'Test 3'}})
  toaster.pushMessage({type: 'notification', payload: {message: 'Test 4'}})
  Array.from(document.querySelectorAll('.description')).forEach(desc => {
    desc.value = desc.dataset['description']
  })

  Array.from(document.querySelectorAll('.content .save-link')).forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault()
      const id = event.target.dataset['id']
      const container = document.querySelector(`#content-${id}`)
      const validation = validateContent(container)
      if (validation.valid) {
        fetchEdit({
          id,
          ...['description', 'price', 'name'].reduce((acc, type) => {
            acc[type] = container.querySelector(`.${type}`).value
            return acc
          }, {}),
        })
      } else {
        toaster.pushMessage({type: 'error', payload: validation})
      }
    })
  })
})
