Open Runtime Assembly Specification, version 1
==============================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

Open Runtime Assembly (ORASM) is the official human-readable representation of Open Runtime Bytecode. It consists of two main portions: the instruction stream and the module formatting data. Module formatting data is only used when writing ORASM, not when disassembling it.

Instruction stream
------------------

The instruction stream is the representation of actual ORB instructions. Each instruction is formatted into its ORB mnemonic (listed in the ORB Specification) as uppercase, the flags as lowercase, some whitespace, a comma-space delimited list of operands, and a newline followed by zero or more whitespace before the next instruction. Registers are represented by the lowercase letter `r` and the register number. Constants are represented by the type name followed by the value. Hexadecimal numbers are prefixed with `0x`, decimal by `d`, binary by `b`. Comments are delimited by a `;`.

### Example instruction stream

```
CPY someGlobal, r1
ADD r1, Long4
CMP r1, Long6
JMPl 0x0000000000000046 ; JuMP if Less than.
CALL someFunction
JMPa 0x000000000000006B ; JuMP Always.
ARG String"Hello, world!"
CALL someOtherFunction
RUNT exit
```

Module formatting data
----------------------

Module formatting data consists of directives, labels, and function definitions and is used when writing modules in ORASM to make such writing possible. Directives consist of a `/` followed by any string and are parsed by the assembler to perform various actions. Labels are strings followed by a `:` which the assembler remembers and replaces with the correct offset. This allows the programmer to write loops and conditionals without worrying about offsets. Function definitions allow functions to be defined by surrounding a name with a `_` and `:`, followed by a newline, and an instruction stream terminated by three consecutive newlines. Function definitions add the code inside them and a function declaration to the module.

### Directives

The following directives are defined by ORASM and MUST be parsed by ORASM assemblers:

 * `/name`: Set the module name.
 * `/creator`: Set the module creator.
 * `/author`: Set the module author.
 * `/version`: Set the module version; all periods are removed (1.0 becomes 10, 0.9 becomes 9, 2.4 becomes 24, etc).
 * `/entry`: Set the module entry point. Defaults to `start`.
 * `/init`: Set the module init function. Defaults to `init`.
 * `/var`: Declares a variable. Takes three parameters: The variable's name, its type, and its initial value (e.g, `/var someVariable Long 37`).
 * `/func`: Declares, without defining, a function. Takes three parameters: The function's name, its start offset, and its end offset.
 * `/hex`: Passes some raw hexadecimal data directly into the module.

### Example module
```
/name SomeModule
/author A Dude
/version 1.0
/entry main

_main:
  CPY someGlobal, r1
  ADD r1, Long4
  CMP r1, Long6
  JMPl condition ; JuMP if Less than.
  CALL someFunction
  JMPa end ; JuMP Always.
  condition:
  ARG String"Hello, world!"
  CALL someOtherFunction
  end:
  RUNT exit

_someFunction:
  ARG String"Less than 6."
  RUNT terminal.print

_someOtherFunction:
  GARG
  ARG r0
  RUNT terminal.print
  RET
```
