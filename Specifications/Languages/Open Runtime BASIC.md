Open Runtime BASIC Specification, version 1
===========================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

Open Runtime BASIC (ORBASIC) is an object-oriented variant of BASIC (the Beginner's All-purpose Symbolic Instruction Code) designed for use in Open Runtime.

Basic syntax
------------

The basic syntax of ORBASIC is fairly complex. The best way to teach is by example, and so, the syntax is given in example format.

All code except class and variable definitions is contained within a function, and subroutines don't exist (by default, `main` is executed at program start):

```basic
FUNCTION main()
  PRINT "Hello, world!"
END FUNCTION
```

There are only four types of variable (Number, the default, stored as a Long float; String, identified with the `$` suffix; Boolean, identified with the `*` suffix; and Object, identified with the `@` suffix):

```basic
aNumber = 259.64
aString$ = "Hello, world!"
aBoolean* = true
anObject@
```

Comments are defined with the `;` character or the REM statement.

Lines are not numbered; when a `GOTO` is needed, it points to a label instead:

```basic
FUNCTION main()
  hello: PRINT "Hello, world!"
  GOTO hello
END FUNCTION
```

Function calls are performed by name:

```basic
FUNCTION something(someArgument$)
  PRINT "Doing something with ", someArgument$
END FUNCTION

FUNCTION main()
  something("some text") ; Prints "Doing something with some text".
END FUNCTION
```

The core statements are `PRINT` (prints (a) string(s) to the terminal), `INPUT` (reads a line from the terminal), `INPUTN` (reads a number from the terminal), `REM` (a comment), `RETURN` (returns a value from a function), `CAST` (casts a value to a new type, like `aString = CAST aNumber, String`), NEW (creates an instance of a class), and EXISTS (returns true for non-null values, false for null values).

Assignments are performed by placing a variable name before an `=` and an expression:

```basic
FUNCTION add(num1, num2)
  RETURN num1 + num2
END FUNCTION

FUNCTION main()
  result = add(2, 5)
  result$ = CAST result, String
  PRINT result$ ; Prints "7".
END FUNCTION
```

Conditions may be performed using the `IF`, `THEN`, `ELSE`, and `END IF` keywords:

```basic
FUNCTION main()
  someVariable = 5
  someVariable = someVariable + 1
  IF someVariable == 6 THEN
    PRINT "We good."
  ELSE
    PRINT "Math is broken. Please check Universe and try again."
  END IF
END FUNCTION
```

Classes may be defined using the `CLASS` keyword:

```basic
CLASS SomeClass
  property = 2

  FUNCTION set(newValue)
    self.property = newValue
  END FUNCTION

  FUNCTION get()
    RETURN self.property
  END FUNCTION

  FUNCTION print()
    PRINT self.get()
  END FUNCTION

  INITIALIZER(initalValue)
    IF EXISTS initialValue THEN
      self.property = initialValue
    END IF
  END FUNCTION
END CLASS

FUNCTION main()
  someObject@ = NEW SomeClass(3)
  someOtherObject@ = NEW SomeClass()
  someObject@.print() ; Prints "3".
  someOtherObject.print() ; Prints "2".
  someObject.set(7)
  someObject.print() ; Prints "7".
END FUNCTION
```

Loops may be accomplished through the use of the `WHILE` and `END WHILE` keywords:

```basic
FUNCTION main()
  i = 0
  WHILE i <= 10
    i$ = CAST i, String
    PRINT i$
    i = i + 1
  END WHILE ; Prints "0
  ;1
  ;2
  ;3
  ;4
  ;5
  ;6
  ;7
  ;8
  ;9
  ;10".
```
