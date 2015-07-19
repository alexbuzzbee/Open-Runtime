# Open Runtime Bytecode, version 1

The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

The Open Runtime Bytecode (ORB) is a simple bytecode language for use in Open Runtime programs. It is a core part of Open Runtime, and all implementations MUST contain an ORB interpreter.

## Format

ORB strings are strings of any bytes except [FD], [FE], and [FF] (used as seperators).

ORB modules begin with a header (If the sequence `#!` is detected, the Runtime MUST move to the first end-of-line character before parsing the header. This is for UNIX compatibility.). It is formatted as follows:

ORB version[FE]Creator[FE]Author[FE]Module name[FE]Module version[FE]Module size[FE]Module checksum[FE]Entry point[FE]Init function[FF]

* The ORB version is the version of ORB in use in the module. It is a 16-bit unsigned integer. Modules with unknown or unsupported versions MUST be rejected by the Runtime.
* The Creator is the name of the program that created the module. It is a string.
* Author is the name of the module's author. It is a string.
* Module name is the name of the module. It is a string.
* Module version is the version of the module. It is a 16-bit integer.
* Module size is the size of the module, excluding the header. The Runtime MUST reject the module if the size does not match. It is a 32-bit integer.
* The Module checksum is an SHA-1 binary checksum of the entire module, not including the header. The Runtime MUST reject the module if the checksum does not match.
* The Entry point is a function name which is called if the module is executed. It MAY be null, in which case executions MUST be rejected by the Runtime. It is a string.
* The Init function is a function name which is called when the module is loaded. It MAY be null. It is a string.

The ORB header is followed by a list of global variables created by the module. Each one is formatted as follows:

Variable name[FE]Type[FE]Constant flag[FE]Initial value (optional)[FF]

* The Variable name is the name of the variable used to reference it from code. It is a string.
* The Type is used to determine the contents of the variable. See 'Types' later in this document. It is an 16-bit unsigned integer.
* The Constant flag indicates whether the variable is immutable (read-only).
* The Initial value is the value the variable is initially set to. Its format is dependent on the Type, and is null for Objects and RuntimeDatas.

The list of global variables is followed by an extra [FF], and the list of functions declared by the module.

Functions are pieces of code, invoked with arguments. Their entries in the function list are formatted as follows:

Function name[FE]Code start offset[FE]Code end offset[FF]

* The Function name is a name used to reference and execute the function. It is a string.
* The Code start offset is an offset from the end of the function list at which function execution begins.
* The Code end offset is an offset from the end of the function list at which function execution terminates.

After the list of functions is the bytecode itself, one function after the other.

## Types

ORB has a few primitive types, as well as an 'Object' type, which allows new types to be defined. They are enumerated below:

* Null: nothing. Identified with the type number 0x0.
* Byte: an unsigned 8-bit integer. Identified with the type number 0x1.
* Short: a signed 16-bit integer. Identified with the type number 0x2.
* Integer: a signed 32-bit integer. Identified with the type number 0x3.
* Long: a signed 64-bit integer. Identified with the type number 0x4.
* Superlong: a signed 128-bit integer. Identified with the type number 0x5. (NOTE: This type is optional, as many programming languages and processors cannot work with 128-bit numbers.)
* Short float: a signed 16-bit floating-point number. Identified with the type number 0x6.
* Float: a signed 32-bit floating-point number. Identified with the type number 0x7.
* Long float: a signed 64-bit floating-point number. Identified with the type number 0x8.
* String: any series of bytes except [00], terminated by a [00]. Identified with the type number 0x9.
* Boolean: true or false. Identified with the type number 0xA.
* RuntimeData: a runtime-created value which cannot be manipulated by user code without calling the runtime. Identified with the type number 0xB
* Object: a user-defined dynamic object containing properties and methods. Methods are identified with Strings, properties with Strings or Longs. Identified with the type number 0xC. (NOTE: Objects cannot be constant!)

## ORB virtual machine

The ORB virtual machine is a register-based machine. There are 16 registers numbered 0 to 15 each able to hold a reference to any value. The virtual machine has an exception-handling mechanism, described in the Exceptions specification. There is an invisible set of binary flags used by comparison and (in the event of errors) arithmetic operations to pass on their results.

The flags are as follows:

* Less
* Greater
* Equal
* Not equal
* Error (used to identify an error when an exception is unnecessary)

## Code formatting and instructions

ORB code is formatted into instructions, consisting of a one-byte instruction number, a one-byte flag block, and zero or more instruction-dependent operands. Non-fixed-size operands are terminated by [00] bytes. Constant operands are prefixed with a two-byte type number. The Runtime MUST move through the code of the current function, executing each instruction as it comes across it, until it comes across a JMP or CALL instruction. Invalid instructions MUST trigger the String `"InvalidInstructionException:{hexadecimal instruction code}"` to be thrown as an exception. The valid instructions are enumerated below in the format {hexadeximal instruction code}, MEMONIC: Description.

* 00, NOP: No operation.
* 01, ADD: Add the two operands. The first operand must be a register, and it is where the result is stored. The first two flag bits determine whether the second operand identifies a register, a global variable, or a constant value.
* 02, SUB: Subtract the second operand from the first. The first operand must be a register, and it is where the result is stored. The first two flag bits determine whether the second operand identifies a register, a global variable, or a constant value.
* 03, MUL: Multiply the two operands. The first operand must be a register, and it is where the result is stored. The first two flag bits determine whether the second operand identifies a register, a global variable, or a constant value.
* 04, DIV: Divide the second operand by the first. The first operand must be a register, and it is where the result is stored. The first two flag bits determine whether the second operand identifies a register, a global variable, or a constant value. The third flag bit, when enabled, transforms the operation into a modulus.
* 05, CPY: Copy the first value to the second. The first two flag bits determine whether the first operand identifies a register, a global variable, or a constant value. The second two flag bits determine whether the second operand identifies a register, or a global variable.
* 06, PCPY: Copy a property from an object to a register or vice versa. The first operand is an object, the second a property name, and the third a register. The first two flag bits determine whether the first operand identifies a register, or a global variable, while the third determines direction (0 = Object -> Register, 1 = Register -> Object)
* 07, CMP: Compare two numbers of the same type. The first two flag bits determine whether the second operand identifies a register, a global variable, or a constant value, while the third and forth flag bits do the same for the second operand.
* 08, JMP: Transfers execution to another position in the current function, identified with a 64-bit offset. Each flag identifies a possible condition.
  * 00000001: Less than.
  * 00000010: Greater than.
  * 00000100: Equal to.
  * 00001000: Not equal to.
  * 00010000: Arithmetic/logic error.
  * 10000000: Always.
* 09, ARG: Adds its operand to the stack of arguments for the next function or runtime call. The first two flag bits determine whether the operand identifies a register, variable, or constant value.
* 0A, CALL: Executes another function by name. Its operand is non-fixed-size, being a string.
* 0B, MCAL: Almost identical to CALL, except that methods are called, not functions. The second operand is an object reference. The first two flag bits determine whether it identifies a register or variable.
* 0C, RUNT: Executes a runtime request by name. The result is placed in register 0. Its operand is non-fixed-size, being a string.
* 0D, GARG: Pops the last argument to the current function into register 0.
* 0E, RET: Return execution to the instruction after the CALL instruction which invoked the current function.
* 0D, ECAT: Triggers a jump to the specified position (with register 0 set to the exception object) if an exception occurs. If the operand is 0, the catch point is unset.
* 10, ETHR: Throws its operand as an exception. The first two flag bits determine whether the operand identifies a register, or a global variable.
* 11, OCRT: Creates a new empty object in the specified register or global variable. The first flag bit determines if the operand is a register or a global variable.
* 12, OPRP: Creates a new property of the specified type. The first operand is a type, the second a name, the third an initial value (which may be null), the forth an object. The first two flag bits determine whether the third operand identifies a register, a global variable, or a constant value; the second two flag bits do much the same for the forth operand (e.g. OPRP String hello "Hello, world!" myObj).
* 13, OMTH: Creates a new method, creating a reference to the specified function in the specified name, within the specified object (e.g. OMTH Object::blah "blah" myObj).
* 14, GREF: Creates a new reference to the value referenced by the first operand and places it in the second operand. The first flag bit determines whether the first operand identifies a register or a global variable.
* 15, TYPE: Places the type number (as a Short) of the first operand into the second, which must be a register. The first flag bit determines whether the first operand identifies a register or a global variable.
