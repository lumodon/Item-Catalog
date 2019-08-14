import Toaster from '/static/toaster.js'
import { fetchData, validateContent } from '/static/utilities.js'

const TOASTER_DURATION = 3000

document.addEventListener('DOMContentLoaded', () => {
  // Initialize notification system
  const toaster = new Toaster({
    toasterElement: document.querySelector('.toaster'),
    duration: TOASTER_DURATION, /* TODO: need SASS for SSOT */
  })

  // Populate description values from template data
  Array.from(document.querySelectorAll('.description')).forEach(desc => {
    desc.value = desc.dataset['description']
  })

  // Handle save
  Array.from(document.querySelectorAll('.content .save-link')).forEach(link => {
    link.addEventListener('click', event => {
      event.preventDefault()
      const id = event.target.dataset['id']
      const container = document.querySelector(`#content-${id}`)
      const validation = validateContent(container)
      if (validation.valid) {
        fetchData(`/restaurants/${id}/menu/<int:menuitem_id>`, {
          id,
          ...['description', 'price', 'name'].reduce((acc, type) => {
            acc[type] = container.querySelector(`.${type}`).value
            return acc
          }, {}),
        })
      } else {
        toaster.pushMessage({type: 'error', payload: {...validation, interrupt: true}})
      }
    })
  })
})
