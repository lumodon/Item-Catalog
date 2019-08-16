import Toaster, { TOASTER_DURATION } from '/static/toaster.js'
import { fetchData, validateContent } from '/static/utilities.js'

document.addEventListener('DOMContentLoaded', () => {
  // Initialize notification system
  window.toaster = new Toaster({
    toasterElement: document.querySelector('.toaster'),
    duration: TOASTER_DURATION, /* TODO: need SASS for SSOT */
  })

  // Populate description values from template data
  Array.from(document.querySelectorAll('.description')).forEach(desc => {
    desc.value = desc.dataset['description']
  })

  // Handle save
  Array.from(document.querySelectorAll('.controls .save-link')).forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault()
      const { name, id, restaurantid  } = event.target.dataset
      const container = document.querySelector(`#content-${id}`)
      const validation = validateContent(container)
      if (validation.valid) {
        fetchData(`/restaurants/${restaurantid}/menu/${id}`, {
          id,
          ...['description', 'price', 'name'].reduce((acc, type) => {
            acc[type] = container.querySelector(`.${type}`).value
            return acc
          }, {}),
        })
          .then(res => res.json())
          .then(serverResponse => {
            if(serverResponse.response == 'success') {
              toaster.pushMessage({
                type: 'notification',
                payload: {message: `${name} Saved Successfully`}
              })
              console.log(serverResponse.message)
            }
          })
      } else {
        toaster.pushMessage({type: 'error', payload: {...validation, interrupt: true}})
      }
    })
  })
})
