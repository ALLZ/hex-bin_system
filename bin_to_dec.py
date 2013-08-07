import sublime
import sublime_plugin


class BinToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
        for item in reglist:
            bin = v.substr(v.sel()[reglist.index(item)])
            bin = bin.strip()
            l = True
            if bin == '':
                l = False
            for i in bin:
                if not((i == '1') or (i == '0')):
                    l = False
            if l:
                v.replace(edit, v.sel()[reglist.index(item)], str(int(bin, 2)))
            else:
                if len(bin) > self.MAX_STR_LEN:
                    logMsg = bin[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = bin
                sublime.status_message("\"%s\" isn't a binary number!" % logMsg)
                sublime.error_message("\"%s\" isn't a binary number!" % logMsg)
