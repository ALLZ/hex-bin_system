import sublime
import sublime_plugin


class BinToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 20

    def run(self, edit):
        v = self.view
        reglist = list(v.sel())
<<<<<<< HEAD
        for j in range(0, len(reglist)):
            bin = v.substr(v.sel()[j])
=======
        for item in reglist:
            bin = v.substr(v.sel()[reglist.index(item)])
>>>>>>> 736565c4382dadd2d10eeb9626dae94fe68a70a3
            bin = bin.strip()
            l = True
            if bin == '':
                l = False
            for i in bin:
                if not((i == '1') or (i == '0')):
                    l = False
            if l:
<<<<<<< HEAD
                v.replace(edit, v.sel()[j], str(int(bin, 2)))
=======
                v.replace(edit, v.sel()[reglist.index(item)], str(int(bin, 2)))
>>>>>>> 736565c4382dadd2d10eeb9626dae94fe68a70a3
            else:
                if len(bin) > self.MAX_STR_LEN:
                    logMsg = bin[0:self.MAX_STR_LEN] + "..."
                else:
                    logMsg = bin
                sublime.status_message("\"%s\" isn't a binary number!" % logMsg)
                sublime.error_message("\"%s\" isn't a binary number!" % logMsg)
