Open Runtime windowing.generic API, version 1
=============================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The windowing.generic API provides generic cross-platform window management and event handling for said windows. Along with cross-platform graphics such as OpenGL, this allows fully portable and custom UIs.

List of API functions
---------------------

 * `listWindows()`: Returns a 0-base numerically indexed Object containing one Object for each open window.
 * `openWindow(width: Long, height: Long, minWidth: Long, minHeight: Long, maxWidth: Long, maxHeight: Long, canFullScreen: Boolean)`: Creates a new window on screen `width` by `height` screen pixels which cannot be smaller than `minWidth` x `minHeight` and cannot be larger than `maxWidth` x `maxHeight`. If `canFullScreen` is true, the fullscreen/maximize/zoom button is enabled. Returns an Object representing the window containing the following methods and properties:
  * Property `height`: The current height of the window.
  * Property `width`: The current width of the window.
  * Property `canFullScreen`: If the window can currently be fullscreened/maximized/zoomed.
  * Method `setCanFullScreen(newValue: Boolean)`: Set if the window can currently be fullscreened/maximized/zoomed.
  * Method `close()`: Closes the window.
  * Method `clear()`: Blanks the contents of the window to plain white.
  * Method `onClick(function: String)`: Call the function named by `function` every time a click happens inside the window, passing two Longs: `width` and `height`.
  * Method `onKeyPress(function: String)`: Call the function named by `function` every time a keypress happens while the window has focus, passing one String: `keyChars`.
  * For each supported graphics rendering system, appropriate methods to acquire/release a drawing context (e.g, for OpenGl: `glBegin()` and `glEnd()`, for some example object-oriented rendering system: `exAcquire()` returning an Object).
