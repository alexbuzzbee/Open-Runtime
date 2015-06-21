Open Runtime terminal API, version 1
====================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The terminal API provides text-based I/O for simple (usually command-line) applications.

Terminal API Overview
---------------------

The terminal API defines a number of functions, almost all of which work with Strings. It interacts with a device called a 'terminal' (defined below).

Concepts
--------

Terminal: Any kind of character-by-character I/O device used to communicate with a human. Terminals need not be physical devices.
Main terminal: The primary terminal being used by the terminal API.

List of API functions
---------------------

 * print(value: String): Prints a String value to the main terminal. Returns a Short indicating error condition, which may be 0 (success), 1 (no terminal), 2 (invalid value), 3 (value too long), or 32767 (unknown error).
 * read(length: Integer): Reads `length` bytes from the main terminal and returns them as a string.
 * clear(): Clears the screen. Returns a Short indicating error condition, which may be 0 (success), 1 (no terminal), or 32767 (unknown error).
 * readUntil(endByte: Byte): Reads bytes from the main terminal until a byte with the value of `endByte` is read, at which point reading stops and a String containing the read data (minus the `endByte`) is returned.
 * getSystemNewline(): Returns the newline character used on the current system. Similar to C++'s `std::endl`.
 * readLine(): Equivalent to readUntil(getSystemNewline()).
