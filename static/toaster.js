class Toaster {
  constructor({ toasterElement, duration }) {
    this.messageBeingDisplayed = false
    this._messageQueue = []
    this._toaster = toasterElement
    this._toasterText = toasterElement.querySelector('p')
    this._msgTimeout = null
    this._currentMessage = null
    this.toastDuration = duration /* TODO: need SASS for SSOT */

    this._messageEnd = this._messageEnd.bind(this)
    this._handleQueue = this._handleQueue.bind(this)
    this._handleMessage = this._handleMessage.bind(this)
  }

  pushMessage({ type, payload }) {
    if(payload.interrupt) {
      clearTimeout(this._msgTimeout)
      this.messageBeingDisplayed = false
      this._toaster.classList.remove(
        'slideout',
        'toaster-shown',
        'hidden',
      )
      // Repeat current message next since user may not
      // have enough time to view it
      if(this._currentMessage) {
        this._messageQueue.unshift(this._currentMessage)
        this._currentMessage = null
      }

      this._messageQueue.unshift(() => {
        this._handleMessage({ type, payload })
      })
    } else {
      this._messageQueue.push(() => {
        this._handleMessage({ type, payload })
      })
    }
    this._handleQueue()
  }

  _handleMessage({ type, payload }) {
    this.messageBeingDisplayed = true
    console.log('type: ', type)
    const sCase = {
      error: () => {
        this._toasterText.classList.add('warning')
        this._toasterText.innerText = `Error: ${payload.error}`
      },
      notification: () => {
        this._toasterText.classList.remove('warning')
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
    this._msgTimeout = setTimeout(this._messageEnd, this.toastDuration)
  }

  _messageEnd() {
    this._toaster.classList.remove('slidein', 'toaster-shown')
    this._toaster.classList.add('slideout', 'toaster-offscreen')
    this._msgTimeout = setTimeout(() => {
      this.messageBeingDisplayed = false
      this._currentMessage = null
      this._toaster.classList.remove('slideout')
      this._toaster.classList.add('hidden')
      this._handleQueue()
    }, Number(this.toastDuration / 4))
  }

  _handleQueue() {
    if (this._messageQueue.length > 0 && !this.messageBeingDisplayed) {
      this._currentMessage = this._messageQueue.shift()
      this._currentMessage()
    }
  }
}

export default Toaster
