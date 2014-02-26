import sublime
import sublime_plugin


class DecToHexCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for i in range(0, len(reglist)):
            dec = v.substr(v.sel()[i])
            dec = dec.strip()
            if dec.isdigit():
                v.replace(edit, v.sel()[i], '{0:X}'.format(int(dec)))
            else:
                if len(dec) > self.MAX_STR_LEN:
                    logMsg = dec[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = dec
                sublime.status_message("\"%s\" isn't a decimal number!" % logMsg)
                sublime.error_message("\"%s\" isn't a decimal number!" % logMsg)
