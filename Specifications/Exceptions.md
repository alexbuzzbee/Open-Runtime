Open Runtime Exception Specification, version 1
===============================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The exception system in Open Runtime is fairly simplistic. When an exception is thrown (either by the Runtime itself or by an `ETHR[10]` instruction), the Runtime checks if an exception catch point is set in the current function (by an `ECAT[0D]`) instruction). If so, the Runtime MUST set register 0 to the exception object and jump execution to the catch point. If not, the function stack MUST be unwound until a catch point is found, at which point execution is jumped there, with register 0 set to the exception. If the stack unwinds fully before a catch point is found, the program MUST be terminated with an "Uncaught exception" error.
