import sublime, sublime_plugin

class BinToDecCommand(sublime_plugin.TextCommand):
    MAX_STR_LEN = 30
    def run(self, edit):
        v = self.view

        
        bin = v.substr(v.sel()[0])
        bin = bin.strip()
        l=True
        if bin == '': l = False
        for i in bin:
            if not((i=='1') or (i=='0')):
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