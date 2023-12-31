README.WIN32 for PHP

For installation instructions, see http://www.php.net/manual/install-windows95-nt.php3

---------------------------------------------------------------------
COMPILING UNDER WINDOWS

Windows compilation has only been tested with Microsoft Visual C++
Version 6 Professional Edition.  The PHP executable has only had limited
testing under Windows 95 and Windows 98. Safe mode and many filesystem-
related functions are not available under Windows.

-----------------------------------------------------------------------
Obtaining the Support Files

To compile PHP and all of the extensions supported in the default
configuration, you will need to obtain the necessary support programs
(bison and flex) and include files and libraries. Simply download
http://www.php.net/extra/win32build.zip and unzip it in the win32
directory of the source. (This should create bin, include, and lib
directories under win32. You may need to specify a flag such as "-d"
to your unzip program to make it unpack the files correctly.)

It may also be possible to use pre-installed versions of flex and
bison, but you will need to change the custom build instructions
in the php_custom_build project.

-----------------------------------------------------------------------
Compiling PHP with MSVC6

There are two MSVC workspaces provided with this distribution.  The one
most people will use is php3.dsw.  This contains project files for the CGI
version of PHP, along with a number of dynamically loadable extensions.

The next workspace is php3extras.dsw.  This project contains the converter
and a program called phpwatch, which is a simple program to watch debugger
output under Windows.  The 'socket' program is also available from the PHP
site, which is a better alternative to phpwatch.

-----------------------------------------------------------------------
Default Configuration and Configuration Issues

* The default configuration for the Windows PHP version contains ODBC
  support. Support for other database modules is provided using 
  dynamically-loaded extensions.

* ODBC can be used to connect to many of the databases that are also
  supported using specific extensions.

-----------------------------------------------------------------------
Working with the Project Files

There are some things to remember when working with the project files:

1. Do not include system-specific paths. All paths should be relative
   to the project files (which are in the win32\ directory). You should
   install Windows-specific header files and libraries in the include\
   and lib\ directories and update win32build.zip.

2. Extensions should output their DLL into the module_{debug,release}
   directories, and intermediate objects into module_{debug,release}\ext
   (where ext is a unique name for the extension). This avoids having
   collisions when two extensions compile the same file. (For example,
   the Solid extension simply compiled unified_odbc.c with some Solid-
   specific #defines. Without writing the intermediate objects to a
   unique subdirectory, DevStudio will get confused when it tries to
   compile another extension that also compiles unified_odbc.c with
   different #defines.

3. Make sure you set up both the debug and release builds of any
   new project files you add!
