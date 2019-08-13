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
    this._recalculateSize = this._recalculateSize.bind(this)

    // Add dynamic sizing
    document.head.appendChild(document.createElement('style'))
    this._styleSheet = document.styleSheets[document.styleSheets.length - 1]
    this._recalculateSize()
    window.addEventListener('resize', this._recalculateSize)
  }

  pushMessage({ type, payload }) {
    // Handle Interrupt
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
      // Normal Append
      this._messageQueue.push(() => {
        this._handleMessage({ type, payload })
      })
    }
    this._handleQueue()
  }

  _recalculateSize() {
    const { width, height } = getComputedStyle(this._toaster)
    const computedHalfWidth = Number(width.replace('px', '')) / 2
    const computedHeight = Number(height.replace('px', '')) + 20
    while(this._styleSheet.cssRules.length > 0) {
      this._styleSheet.deleteRule(0)
    }
    this._styleSheet.insertRule(`
      .toaster {
        left: calc(50vw - ${computedHalfWidth}px);
      }
    `, 0)
    this._styleSheet.insertRule(`
      .toaster-shown {
        top: calc(100vh - ${computedHeight}px);
      }
    `, 1)
    this._styleSheet.insertRule(`
      @keyframes slidein {
        from { top: 100vh; }
        to { top: calc(100vh - ${computedHeight}px); }
      }
    `, 2)
    this._styleSheet.insertRule(`
      @keyframes slideout {
        from { top: calc(100vh - ${computedHeight}px); }
        to { top: 100vh; }
      }
    `, 3)
  }

  _handleMessage({ type, payload }) {
    this.messageBeingDisplayed = true
    console.log('type: ', type)
    const sCase = {
      error: () => {
        this._toaster.classList.add('warning')
        this._toasterText.innerText = `Error: ${payload.error}`
        this._recalculateSize()
      },
      notification: () => {
        this._toaster.classList.remove('warning')
        this._toasterText.innerText = payload.message
        this._recalculateSize()
      },
      default: () => {
        this._toasterText.innerText = ''
        this._recalculateSize()
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
