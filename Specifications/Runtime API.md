Open Runtime API Specification, version 1
=========================================
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [RFC 2119](http://www.ietf.org/rfc/rfc2119.txt).

Open Runtime has a simplistic API, accessed using the RUNT[0C] instruction. The Runtime's calling convention is as follows:

Arguments: argument stack

Return value: register 0

Preserved: all others

Requirement levels
------------------

The Open Runtime API is made up of several smaller APIs. They are divided into a few categories:

 * Required: These APIs are parts of the core of Open Runtime, and MUST be provided by all implementations. Implementations which provide less then all Required APIs are 'Nonconforming'. Implementations which provide only Required APIs are 'Minimal'.
 * Recommended: These APIs SHOULD be implemented, but are not required. Some APIs may be Recommended on one platform, but Optional or Deprecated on others. Implementations which provide all Required APIs and some but not all Recommended APIs are 'Partial'. Implementations which provide all Required and Recommended APIs are 'Full'.
 * Optional: These APIs MAY be implemented. Implementations which provide all Required and Recommended APIs and any number of Optional APIs are 'Extended'.
 * Deprecated: These APIs SHOULD NOT be implemented. Implementations which provide any number of Deprecated APIs are 'Zealously-compatible'.

APIs
----

The list of Open Runtime APIs are as follows:

 * terminal: Required. Provides terminal I/O.
 * terminal.curses: Recommended on Unix, Optional on others. Provides access to an implementation of the ncurses terminal utility library.
 * filesystem: Required. Provides access to the filesystem.
 * process: Required. Provides process management and starting.
 * thread: Recommended. Provides cross-platform threading.
 * graphics.opengl: Recommended. Provides access to OpenGL.
 * windowing.generic: Recommended on graphical operating systems, Optional on others. Provides generic windowing functionality.
 * windowing.win32: Recommended on Windows, Deprecated on others. Provides Windows windowing.
 * windowing.glfw: Recommended. Provides access to the GLFW API.
 * widgets.win32: Recommended on Windows, Deprecated on others. Provides Windows graphics widgets.
 * framework.qt: Optional. Provides access to the Qt framework.
 * framework.tk: Optional. Provides access to the Tk toolkit.
 * framework.gtkplus: Optional. Provides access to the GTK+ framework.
 * framework.wxwidgets: Optional. Provides access to the wxWidgets toolkit.
 * framework.cocoa: Recommended on OS X, Optional on others. Provides access to Cocoa.
 * system.unix: Recommended on Unix and OS X, Optional on others. Provides access to the POSIX/SUS standard Unix API.
 * system.osx: Recommended on OS X, Optional on others. Provides access to OS X Core Services.
 * system.windows: Recommended on Windows, Deprecated on others. Provides direct access to the Win32 API.
