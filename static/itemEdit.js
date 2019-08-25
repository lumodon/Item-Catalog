import { fetchData, validateContent } from '/static/utilities.js'
import mainToaster from '/static/toaster.js'

// TODO: DRY itemEdit.js & edit.js
document.addEventListener('DOMContentLoaded', () => {
  // Populate description values from template data
  const desc = document.querySelector('.description')
  desc.value = desc.dataset['description']

  // Handle save
  const link = document.querySelector('.controls .save-link')
  link.addEventListener('click', event => {
    event.preventDefault()
    const { name, id  } = event.target.dataset
    const container = document.querySelector(`#content-${id}`)
    const validation = validateContent(container)
    if (validation.valid) {
      fetchData(`/items/${id}/edit`, {
        id,
        ...['description', 'name'].reduce((acc, type) => {
          acc[type] = container.querySelector(`.${type}`).value
          return acc
        }, {}),
      })
        .then(res => res.json())
        .then(serverResponse => {
          if(serverResponse.response == 'success') {
            mainToaster.pushMessage({
              type: 'notification',
              payload: { 'message': msg }
            })

            // Remove 'edit' from end of url
            const currentPath = window.location.pathname.split('/')
            const redirectHref = currentPath.slice(0,currentPath.length-1)
              .join('/')

            window.location = redirectHref
          }
        })
    } else {
      mainToaster.pushMessage({
        type: 'error',
        payload: {...validation, interrupt: true}
      })
    }
  })
})
