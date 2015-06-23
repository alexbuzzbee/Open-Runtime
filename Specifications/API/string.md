Open Runtime string API, version 1
==================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The string API provides string manipulation and conversion functions.

List of API functions
---------------------

* `concat(str1: String, str2: String)`: Concatenates `str2` to the end of `str1` and returns the result.
* `length(str: String)`: Returns the length of `str`.
* `encoding(str: String)`: Returns an MIME charset name (such as "UTF-8", "US-ASCII", "EBCDIC-US", "macintosh", or "windows-1252") identifying the character set of `str`.
* `toBytes(str: String)`: Converts `str` to an Object with 0-indexed numeric property names and returns it. Each property is one of the bytes that makes up the String.
* `fromBytes(bytes: Object)`: The inverse of `toBytes(str)`.
* `toLong(str: String)`: Converts `str` to a Long.
* `fromLong(long: Long)`: Converts `long` to a String.
* `toFloat(str: String)`: Converts `str` to a Long float.
* `fromFloat(float: Long float)`: Converts `float` to a String.
* `toBool(str: String)`: Converts `str` to a Boolean (from "true", "yes", "1", "false", "no", or "0").
* `fromBool(bool: Boolean)`: Converts `bool` to a String (either "true" or "false").
