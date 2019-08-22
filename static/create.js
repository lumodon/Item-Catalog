import { fetchData, validateContent } from '/static/utilities.js'

document.addEventListener('DOMContentLoaded', () => {
  // Handle save
  Array.from(document.querySelectorAll('.controls .save-link'))
    .forEach(link => {
      link.addEventListener('click', event => {
        event.preventDefault()
        const container = document.querySelector('.content')
        const validation = validateContent(container)
        if (validation.valid) {
          fetchData(`/items/create`, {
            'owner': sessionUser.gplus_id,
            ...['description', 'name', 'category'].reduce((acc, type) => {
              acc[type] = container.querySelector(`.${type}`).value
              return acc
            }, {}),
          })
            .then(res => res.json())
            .then(serverResponse => {
              if(serverResponse.response == 'success') {
                window.location = '/'
              }
            })
        } else {
          toaster.pushMessage({
            type: 'error',
            payload: {...validation, interrupt: true}
          })
        }
      })
    })
})
