# script.subsize
This is a Kodi script addon for Kodi v19 (Matrix) and above.

Usage:

This addon is intended to set the size of text-based subtitles by controlling
the Kodi Player/Subtitles/Size setting.  Will not affect graphics subtitles
such as PGS or Vobsub and you must override the style in text subtitle formats
that support style (SSA/ASS).

Bind the script to a desired input (example keyboard key using keyboard.xml) 
with the builtin command "Runscript(script.subsize)".  Suggested binding is
for at least the fullscreenvideo window.

During video play, use the bound input to start the addon.  A select dialog
will launch with the allowed fonsize options.  The current size is pre-selected.
Scroll up/down to desired size and click to select or cancel to keep current
size.

The addon will also be listed as a "program" addon in menues, but running it
from a menu will probably not provide a benefit over changing the setting in 
Kodi settings menu.




 
