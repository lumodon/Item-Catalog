class Toaster {
  constructor({toasterElement, duration}) {
    this.messageBeingDisplayed = false
    this._messageQueue = []
    this._toaster = toasterElement
    this._toasterText = toasterElement.querySelector('p')
    this._msgTimeout = null
    this.toastDuration = duration /* TODO: need SASS for SSOT */

    this._messageEnd = this._messageEnd.bind(this)
    this._handleQueue = this._handleQueue.bind(this)
  }

  pushMessage({ type, payload }) {
    this._messageQueue.push(() => {
      this.messageBeingDisplayed = true
      console.log('type: ', type)
      const sCase = {
        error: () => {
          this._toasterText.classList.add('warning')
          this._toasterText.innerText = `Error: ${payload.error}`
        },
        notification: () => {
          this._toasterText.innerText = payload.message
        },
        default: () => {
          this._toasterText.innerText = ''
          throw new Error('Error - invalid toaster message case')
        },
      }
      try {
        sCase[type]()
      } catch (err) {
        console.trace(err)
      }
      this._toaster.classList.remove('hidden', 'toaster-offscreen')
      this._toaster.classList.add('slidein', 'toaster-shown')
      setTimeout(this._messageEnd, this.toastDuration)
    })
    this._handleQueue()
  }

  _messageEnd() {
    this._toaster.classList.remove('slidein', 'toaster-shown')
    this._toaster.classList.add('slideout', 'toaster-offscreen')
    setTimeout(() => {
      this.messageBeingDisplayed = false
      this._toaster.classList.remove('slideout')
      this._toaster.classList.add('hidden')
      this._handleQueue()
    }, Number(this.toastDuration / 4))
  }

  _handleQueue() {
    if (this._messageQueue.length > 0 && !this.messageBeingDisplayed) {
      this._messageQueue.shift()()
    }
  }
}

export default Toaster
