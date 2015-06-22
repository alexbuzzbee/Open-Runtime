Open Runtime filesystem API, version 1
======================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The filesystem API provides access to filesystems. Paths are represented as a 0-base numerically indexed Object, with each property representing one path component. ANY of these functions may throw a `"PermissionException"` if non-permitted operations are attempted.

List of API functions
---------------------

 * `getSeparator()`: Returns a String containing the path separator.
 * `getRoot()`: Returns a path Object representing the root of the filesystem (e.g, on Unix, this is `{0: "/"}`, and on Windows, it's empty).
 * `parsePath(path: String)`: Converts a String to a path Object.
 * `serializePath(path: Object)`: The inverse of `parsePath(path)`.
 * `list(path: Object)`: Return a 0-base numerically indexed Object containing one path Object for each item in the contents of the directory at `path`.
 * `getInfo(path: Object)`: Returns an Object containing the following properties:
  * `type`: `"dir"`, `"file"`, `"link"`, or `"other"`, depending on the file's type. `"link"` may be used for Windows shortcuts, Unix symbolic links, OS X aliases, and other similar concepts.
  * `size`: The size, in bytes, of the file (0 for directories).
  * `timeModified`: The time the file was last modified.
  * `timeAccessed`: The time the file was last opened.
 * `open(path: Object, mode: String)`: Opens the `path` in the mode `mode`. The mode may be `w` (read-write), `r` (read-only), or `a` (read and append). If a non-existant file is opened in `r` mode, a `"DoesntExistException"` is thrown; in other modes, it is created. The mode may have `b` added to specify a binary file (raw access; read/write bytes, not characters). Returns an Object containing the following methods:
  * `read(startLocation: Long, length: Long)`: Returns `length` bytes from the file, starting at `startLocation`. If less than `length` bytes are returned, the end of file has been reached. If `length` is 0, reads the entire file.
  * `readUntil(startLocation: Long, endByte: Byte)`: Reads bytes from the file, starting at `startLocation`, until a byte with the value of `endByte` is read, at which point reading stops and a String containing the read data (minus the `endByte`) is returned.
  * `write(startLocation: Long, data: String or Object)`: Throws a `"ReadOnlyWriteException"` if the file is open in read-only mode. If `data` is a String, writes that to the file starting at `startLocation`. If `data` is an Object, it is assumed to be a 0-base numerically indexed Object, and each property is assumed to be a Byte. Those bytes are then written starting at `startLocation`. If either of those assumptions proves false, a `"BadArgumentException"` is thrown.
  * `flush()`: Ensures that the file's contents are synced to physical storage media.
  * `close()`: Closes the file. Any further operations will throw a `"ClosedException"`.
 * `delete(path: Object, deleteNonEmptyDir: Boolean)`: Deletes the file or directory at `path`. If `deleteNonEmptyDir` is false, will throw a `"NotEmptyException"` if the directory at `path` isn't empty.
 * `makeDir(path: Object)`: Creates an empty directory at `path`.
