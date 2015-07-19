# Open Runtime core API, version 1

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The core API provides essential functionality. Its functions MUST NOT be namespaced (i.e, `loadModule(name)` is `loadModule(name)`, and not `core.loadModule(name)`).

## List of API functions

 * `loadModule(name: String)`: Loads the module named `name`. How the module is located is implementation-dependant.
 * `isAvailable(name: String)`: Returns a Boolean indicating whether the API call named by `name` is available.
 * `functionExists(name: String)`: Returns a Boolean indicating whether the function named by `name` exists.
 * `exit(code: Integer)`: Terminates the program with the exit code `code`.
 * `onExit(functionName: String)`: Causes the function named by `functionName` to be called before the program exits using `exit(code)`.
 * `abort()`: Terminates the program without calling functions registered using `onExit(functionName)`.
 * `null()`: Returns null.
