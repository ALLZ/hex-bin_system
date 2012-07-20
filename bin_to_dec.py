import sublime, sublime_plugin

class BinToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 30
    def run(self, edit):
        v = self.view

        
        bin = v.substr(v.sel()[0])
        l=True
        for i in xrange(0,len(bin)):
            if not((bin[i]=='1') or (bin[i]=='0')):
             l=False
            
        if l:
            v.replace(edit, v.sel()[0], str(int(bin, 2)))
        else:
             
            if len(bin) > self.MAX_STR_LEN:
                logMsg = bin[0:self.MAX_STR_LEN]+ "..."
            else:
                logMsg = bin
            sublime.status_message("\"" + logMsg + "\" isn't a binar number!")
            sublime.error_message("\"" + logMsg + "\" isn't a binar number!")