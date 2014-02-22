import sublime
import sublime_plugin


class DecToBinCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
<<<<<<< HEAD
        for i in range(0, len(reglist)):
            dec = v.substr(v.sel()[i])
            dec = dec.strip()
            if dec.isdigit():
                v.replace(edit, v.sel()[i], '{0:b}'.format(int(dec)))
=======
        for item in reglist:
            dec = v.substr(v.sel()[reglist.index(item)])
            dec = dec.strip()
            if dec.isdigit():
                v.replace(edit, v.sel()[reglist.index(item)], bin(int(dec))[2:].upper())
>>>>>>> 736565c4382dadd2d10eeb9626dae94fe68a70a3
            else:
                if len(dec) > self.MAX_STR_LEN:
                    logMsg = dec[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = dec
                sublime.status_message("\"%s\" isn't a decimal number!" % logMsg)
                sublime.error_message("\"%s\" isn't a decimal number!" % logMsg)
