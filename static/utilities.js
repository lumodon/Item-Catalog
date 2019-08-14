export function validateContent(container) {
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

export function fetchData(url, payload) {
  fetch(url, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
}
