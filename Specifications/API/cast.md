# Open Runtime cast API, version 

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The cast API provides typecasting functionality to allow working with multiple types.

For any two number types (including Byte), there are functions `<type1>To<type2>(value: type1)` and `<type2>To<type1>(value: type2)` which convert from one type to the other. Any value outside the range of the convert-to type is truncated.
