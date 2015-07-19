"""
ORASM grammar
Part of ORASM
Uses [pyPEG2](http://fdik.org/pyPEG/) (ensure you have pyPEG2 installed before
using)
"""


from pypeg2 import (Keyword, K, List, Enum, attr, maybe_some, optional,
                    indent, name, endl, omit, csl, word, restline)
import re


class Type(Keyword):
    """
    Represents an ORB type, such as Null, Byte, String, or Object.
    """
    grammar = attr("type", Enum(K("Null"), K("Byte"), K("Short"), K("Integer"),
                                K("Long"), K("Superlong"), K("Short float"),
                                K("Float"), K("Long float"), K("String"),
                                K("Boolean"), K("RuntimeData"), K("Object")))


class Register(Keyword):
    """
    Represents an ORB register, from r0 to r15.
    """
    grammar = attr("reg", Enum(K("r0"), K("r1"), K("r2"), K("r3"), K("r4"),
                               K("r5"), K("r6"), K("r7"), K("r8"), K("r9"),
                               K("r10"), K("r11"), K("r12"), K("r13"),
                               K("r14"), K("r15")))


class String():
    """
    Represents a string.
    """
    grammar = "\"", attr("value", re.compile(".*?")), "\""


class HexNum():
    """
    Represents a hexadecimal number.
    """
    grammar = "0x", attr("value", re.compile(r"[0-9A-F]*"))


class DecNum():
    """
    Represents a decimal number.
    """
    grammar = "d", attr("value", re.compile(r"[0-9]*"))


class BinNum():
    """
    Represents a binary number.
    """
    grammar = "b", attr("value", re.compile(r"[01]*"))


class NumConst():
    """
    Represents a constant number (hex, dec, or bin).
    """
    grammar = [HexNum, DecNum, BinNum]


class StringConst():
    """
    Represents a string constant.
    """
    grammar = "String", attr("value", String)


class Constant():
    """
    Represents any constant.
    """
    grammar = attr("value", [NumConst, StringConst, "Null"])


class Mnemonic(Keyword):
    """
    Represents an ORASM instruction mnemonic.
    """
    grammar = attr("mne", Enum(K("NOP"), K("ADD"), K("SUB"), K("MUL"),
                               K("DIV"), K("CPY"), K("PCPY"), K("CMP"),
                               K("JMP"), K("ARG"), K("CALL"), K("MCAL"),
                               K("RUNT"), K("GARG"), K("RET"), K("ECAT"),
                               K("ETHR"), K("OCRT"), K("OPRP"), K("OMTH"),
                               K("GREF"), K("TYPE")))


class Comment():
    """
    Represents a `;` comment.
    """
    grammar = ";", restline, endl


class Operand():
    """
    Represents an operand in an instruction.
    """
    grammar = attr("op", [Register])


class Label():
    """
    Represents a label, like `label:`.
    """
    grammar = indent(name(), ":")


class Instruction():
    """
    Represents an entire instruction, including an optional comment!
    """
    grammar = indent(Mnemonic, optional(csl(Operand)), optional(omit(Comment)),
                     endl)


class Line():
    """
    Represents a line, which may have either a label or an instruction on it.
    """
    grammar = attr("contents", [Label, Instruction])


class InstructionStream(List):
    """
    Represents a list of instructions (without labels).
    """
    grammar = maybe_some(Instruction)


class Block(List):
    """
    Represents a series of lines.
    """
    grammar = maybe_some(Line)


class Function():
    """
    Represents a function, like `_someFunction:
      RET ; Do nothing!`.
    """
    grammar = "_", name(), ":", optional(omit(Comment)), endl, InstructionStream


class Directive(List):
    """
    Represents a `/` directive.
    """
    grammar = "/", name(), maybe_some(word), endl


class Module(List):
    """
    Represents an entire module.
    """
    grammar = maybe_some(Directive), maybe_some(Function)
