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

function toasterMessage({type, payload}) {
  const toasterText = document.querySelector('#toaster p')
  const sCase = {
    error: () => {
      toasterText.classList.add('warning')
      toasterText.innerText = `Error: ${payload.error}`
    },
    notification: () => {
      toasterText.innerText = payload.message
    },
    default: () => {
      toasterText.innerText = ''
      throw new Error('Error - invalid toaster message case')
    }
  }
  try {
    sCase[type]()
  } catch(err) {
    console.trace(err)
  }
  const toasterEle = document.querySelector('#toaster')
  toasterEle.classList.remove('hidden', 'toaster-offscreen')
  toasterEle.classList.add('slidein', 'toaster-shown')
}

document.addEventListener('DOMContentLoaded', () => {
  toasterMessage({type: 'notification', payload: {message: 'hello'}})
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
        toasterMessage({type: 'error', payload: validation})
      }
    })
  })
})
