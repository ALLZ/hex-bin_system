import sublime, sublime_plugin

class HexToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 30
    def run(self, edit):
        v = self.view

        
        hx = v.substr(v.sel()[0])
        l=True
        for i in xrange(0,len(hx)):
            if not((hx[i] in ('0','1','2','3','4','5','6','7','8','9')) or (hx[i] in ('A','B','C','D','E','F'))):
             l=False
            
        if l:
            v.replace(edit, v.sel()[0], str(int(hx, 16)))
        else:
             
            if len(hx) > self.MAX_STR_LEN:
                logMsg = hx[0:self.MAX_STR_LEN]+ "..."
            else:
                logMsg = hx
            sublime.status_message("\"" + logMsg + "\" isn't a hexadecimal number!")
            sublime.error_message("\"" + logMsg + "\" isn't a hexadecimal number!")