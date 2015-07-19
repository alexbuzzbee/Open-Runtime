# Open Runtime BASIC Specification, version 1

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

Open Runtime BASIC (ORBASIC) is an object-oriented variant of BASIC (the Beginner's All-purpose Symbolic Instruction Code) designed for use in Open Runtime.

## Basic syntax

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

The core statements are `PRINT` (prints (a) string(s) to the terminal), `INPUT` (reads a line from the terminal), `INPUTN` (reads a number from the terminal), `REM` (a comment), `RETURN` (returns a value from a function), `CAST` (casts a value to a new type, like `aString = CAST aNumber, String`), `NEW` (creates an instance of a class), and `EXISTS` (returns true for non-null values, false for null values).

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

Conditions may be used with the `IF`, `THEN`, `ELSE`, and `END IF` keywords:

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

Header information and module loading is done through directives (similar to ORASM directives), using the `#` character; the following is a list of directives:

 * All header-data directives from ORASM. NOTE: `#init` sets a function to be called by the ORBASIC implicit init function, which performs setup of ORBASIC modules (such as module loading).
 * `#var`: Declares a variable without defining it. Takes three parameters: The variable's name, its type, and its initial value (e.g, `/var someVariable Long 37`).
 * `#func`: Declares, without defining, a function. Takes three parameters: The function's name, its start offset, and its end offset.
 * `#asm`: Passes some assembly directly into the module.
 * `#module`: Add a `loadModule(name)` call for the specified module to the implicit init function.

Some examples:

```
#name SomeModule
#author A Dude
#version 1.0
#entry someEntry

aGlobal = 3

FUNCTION someEntry()
  #asm MOV aGlobal, r1
END FUNCTION
```

## Implementation

ORBASIC modules have an implicit init function, generated automatically by the compiler. The `#init` directive simply adds a `CALL` instruction to the end of this function, before the `RET`. This init function performs ORBASIC-specific setup such as `loadModule(name)` calls.

ORBASIC functions return values in `r0` and preserve all other registers. The internal code to do so is implementation-dependant. Methods and initializers take as their first argument the `self` value, identifying the object to operate on.

ORBASIC implements object-orientation through at least one function per class. Each class has a function named `__class_<className>_create()`, optionally (if an `INITIALIZER` is specified), an `__class_<className>_init()` function, and one function per method, named `__class_<className>_<methodName>()`. `__class_<className>_create()` is responsible for creating an Object using `OCRT`, setting the appropriate properties, adding methods, and finally calling `__class_<className>_init()`. A mocked up `__class_<className>_create()` function in ORASM follows:

```
___class_SomeClass_create:
  OCRT r0
  CPRP Long float, property, 2, r0
  OMTH __class_SomeClass_get, get, r0
  OMTH __class_SomeClass_set, set, r0
  OMTH __class_SomeClass_print, print, r0'
  GREF r0, r1
  ARG r1
  GARG
  ARG r0
  CALL __class_SomeClass_init
  GREF r1, r0
  RET
```
