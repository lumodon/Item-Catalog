export function validateContent(container, valEle) {
  const validateWithError = err => ({
    valid: false,
    component: valEle,
    error: err,
  })

  for (const valEle of container.querySelectorAll('.value')) {
    if (!valEle.value) {
      return validateWithError('Empty input', valEle)
    }
  }
  return { valid: true }
}

export function fetchData(url, payload) {
  return fetch(url, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
    },
    body: JSON.stringify(payload),
  })
}
