import sublime, sublime_plugin

class DecToBinCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 30
    def run(self, edit):
        v = self.view

        dec = v.substr(v.sel()[0])
        dec = dec.strip()

        if dec.isdigit():
            v.replace(edit, v.sel()[0], bin(int(dec))[2:].upper())
        else:
            if len(dec) > self.MAX_STR_LEN:
                logMsg = dec[0:self.MAX_STR_LEN]+ "..."
            else:
                logMsg = dec
            sublime.status_message("\"" + logMsg + "\" isn't a decimal number!")
            sublime.error_message("\"" + logMsg + "\" isn't a decimal number!")