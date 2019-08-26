import mainToaster from '/static/toaster.js'

for (const deleteLink of document.querySelectorAll('.delete-btn')) {
  deleteLink.addEventListener('click', event => {
    event.preventDefault()
    fetch(deleteLink.dataset['url'], {
      method: 'POST',
    })
      .then(res => res.json())
      .then(res => {
        if(res.response && res.response === 'success') {
          const container = deleteLink.parentElement.parentElement
          container.parentElement.removeChild(container)
        } else {
          mainToaster.pushMessage({type: 'error', payload: {
            error: JSON.stringify(res,0,2),
            interrupt: true,
          }})
        }
      })
  })
}
