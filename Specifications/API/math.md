Open Runtime math API, version 1
================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The math API provides generic mathematical functions to allow more complex math to be done in native code (and thus more quickly).

List of API functions
---------------------

 * factorial(num: Long): Returns the factorial of `num`.
 * exponent(num: Long float, base: Long): Returns `num`^`base`.
 * root(num: Long float, base: Long): Returns the `base`th root of `num`.
 * log(base: Long, num: Long float): Returns the logarithm `num` to base `base`.

### Constants

 * pi(): Returns an approximation of π.
 * e(): Returns an approximation of e.

### Trigonometric functions

 * sin(num: Long float): Returns the sine of `num`.
 * cos(num: Long float): Returns the cosine of `num`.
 * arcsin(num: Long float): Returns the arcsine of `num`.
 * sec(num: Long float): Returns the secant of `num`.
 * csc(num: Long float): Returns the cosecant of `num`.
 * tan(num: Long float): Returns the tangent of `num`.
 * arctan(num: Long float): Returns the arctangent of `num`.
 * cotan(num: Long float): Returns the cotangent of `num`.
