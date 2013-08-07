import sublime
import sublime_plugin


class HexToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for item in reglist:
            hx = v.substr(v.sel()[reglist.index(item)])
            hx = hx.strip()
            hexdig = '0123456789abcdefABCDEF'
            l = True
            if hx == '':
                l = False
            for i in hx:
                if not(i in hexdig):
                    l = False

            if l:
                v.replace(edit, v.sel()[reglist.index(item)], str(int(hx, 16)))
            else:
                if len(hx) > self.MAX_STR_LEN:
                    logMsg = hx[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = hx
                sublime.status_message("\"%s\" isn't a hexadecimal number!" % logMsg)
                sublime.error_message("\"%s\" isn't a hexadecimal number!" % logMsg)
