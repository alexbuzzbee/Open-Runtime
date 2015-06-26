# Open Runtime process API, version

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The process API provides process manipulation functionality. Functions in this API may throw a `"PermissionException"` if non-permitted operations are attempted.

## List of API function

 * `getEnv(name: String)`: Returns the String value stored in the environment variable `name`.
 * `setEnv(name: String, value: String)`: Sets the environment variable named by `name` to the value in `value`.
 * `getPath()`: Returns a 0-base numerically-indexed Object representing the current executable search path.
 * `setPath(newPath: Object)`: Attempts to convert `newPath` to a path string and make it the current executable search path. If `newPath` is not a 0-base numerically-indexed Object, throws a `"BadArgumentException"`.
 * `getPid()`: Returns the process ID for the calling process.
 * `getParent()`: Returns the process ID for the parent of the calling process.
 * `execute(path: Object)`: Attempts to execute, as a new process, the executable identified by the filesystem API path Object `path`.
 * `system(command: String)`: Executes, using the system command interpreter, `command`.
 * `getProcessList()`: Returns a 0-base numerically-indexed Object containing process IDs (e.g, if three processes, 0, 32, and 73 are running, returns `{0: 0, 1: 32, 2: 73}`).
 * `getInfoForPid(pid: Long)`: Returns an Object containing the following properties:
  * `command`: The command used the start the process.
  * `imagePath`: The path to the process image (executable file).
  * `user`: A Long identifying the owning user.
  * `parent`: A Long indicating the PID of the parent process.
  * `canKill`: A Boolean indicating whether this process can be terminated by the Open Runtime program.
 * `terminate(pid: Long)`: Attempts to cleanly terminate the process identified by `pid`.
 * `kill(pid: Long)`: Attempts to forcefully terminate the process identified by `pid`.
 * `onSignal(signalId: Long, function: String)`: Upon receiving the Unix signal `signalId` or its equivalent, run the function named by `function`.
