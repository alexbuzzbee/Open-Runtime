Open Runtime API Specification, version 1
=========================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

Open Runtime has a simplistic API, accessed using the `RUNT[0C]` instruction. The Runtime's calling convention is as follows:

Arguments: argument stack

Return value: register 0

Preserved: all others

Requirement levels
------------------

The Open Runtime API is made up of several smaller APIs. They are divided into a few categories:

 * Required: These APIs are parts of the core of Open Runtime, and MUST be provided by all implementations. Implementations which provide less then all Required APIs are 'Nonconforming'. Implementations which provide only Required APIs are 'Minimal'.
 * Recommended: These APIs SHOULD be implemented, but are not required. Some APIs may be Recommended on one platform, but Optional or Deprecated on others. Implementations which provide all Required APIs and some but not all Recommended APIs are 'Partial'. Implementations which provide all Required and Recommended APIs are 'Full'.
 * Optional: These APIs MAY be implemented. Implementations which provide all Required and Recommended APIs and any number of Optional or unspecified APIs are 'Extended'.
 * Deprecated: These APIs SHOULD NOT be implemented. Implementations which provide any number of Deprecated APIs are 'Zealously-compatible'.

Namespacing
-----------

APIs are to be namespaced for access in a RUNT[0C] instruction by prepending the API name, followed by a dot, to the function name. For example, `print(value)` in the terminal API becomes `terminal.print(value)` in the global Runtime API namespace.

Passthrough APIs
----------------

Passthrough APIs allow easy use of existing APIs without the necessity of redefining them completely. If a specification document for such an API exists, anything stated in it overrides anything stated here.

All functions MUST be renamed to remove any namespacing prefix (such prefixes are already handled), and then to maintain their existing naming scheme. For example, `glBegin()`, in graphics.opengl, becomes `graphics.opengl.begin()`, and `glCreateBuffer()` becomes `graphics.opengl.createBuffer()`.

Any API-defined non-number types MUST be represented either as RuntimeDatas, or as Objects depending on whether their primary purpose is to have operations performed on them or if they have user code-editable properties. For example, an open window would be an Object with methods, but a timestamp would be a RuntimeData. If such a type needs to be created by user code but no function is defined by the API itself, a new function MUST be added named `create<PascalCasedTypeName>()`, which returns a default-value instance (e.g, `createWindow()` would return a new default Window object).

Global variables are represented by adding two new functions to the API: `get_<variableName>()` (the 'getter') and `set_<variableName>(newValue)` (the 'setter'). The first MUST return the current value, while the second MUST set it to its first argument and returns the previous value. A `"BadArgumentException"` exception MUST be thrown by the setter if no new value is provided.

APIs
----

The list of Open Runtime APIs are as follows:

 * core: Required. Essential functionality.
 * terminal: Required. Provides terminal I/O.
 * terminal.curses (passthrough): Recommended on Unix, Optional on others. Provides access to the ncurses terminal utility library.
 * math: Required. Provides various math functions.
 * string: Required. Provides various functions for working with Strings.
 * cast: Required. Provides typecasting between various types.
 * filesystem: Required. Provides access to the filesystem.
 * process: Required. Provides process management and starting.
 * thread: Recommended. Provides cross-platform threading.
 * graphics.opengl (passthrough): Recommended. Provides access to OpenGL.
 * windowing.generic: Recommended on graphical operating systems, Optional on others. Provides generic windowing functionality.
 * windowing.windows (passthrough): Recommended on Windows, Deprecated on others. Provides Windows windowing.
 * windowing.glfw (passthrough): Recommended. Provides access to the GLFW API.
 * widgets.windows (passthough): Recommended on Windows, Deprecated on others. Provides Windows graphics widgets.
 * framework.qt (passthough): Optional. Provides access to the Qt framework.
 * framework.tk (passthough): Optional. Provides access to the Tk toolkit.
 * framework.gtkplus (passthough): Optional. Provides access to the GTK+ framework.
 * framework.wxwidgets (passthough): Optional. Provides access to the wxWidgets toolkit.
 * framework.cocoa (passthough): Recommended on OS X, Optional on others. Provides access to Cocoa.
 * system.unix (passthough): Recommended on Unix and OS X, Optional on others. Provides access to the POSIX/SUS standard Unix API.
 * system.osx (passthrough): Recommended on OS X, Optional on others. Provides access to OS X Core Services.
 * system.windows (passthrough): Recommended on Windows, Deprecated on others. Provides direct access to the Win32 API.
