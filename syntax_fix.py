import sublime, sublime_plugin

BufSize = max(
    len('#!/usr/local/bin rubyN.NN.NN'), 
    len('#!/usr/bin/env rubyN.NN.NN'),
    len('#!/usr/local/bin awk -f'),
    len('exec '),
    len('#!/usr/local/bin/expect'),
)


class SyntaxFix(sublime_plugin.EventListener):

    def on_load(self, view):
        buf = view.substr(sublime.Region(0, BufSize))

        if '/bin/ruby' in buf or '/bin/env ruby' in buf:
           view.settings().set('syntax', 'Packages/Ruby/Ruby.sublime-syntax')

        elif '/bin/awk' in buf or '/bin/env awk' in buf:
            view.settings().set('syntax', 'Packages/Awk/Awk.sublime-syntax')

        elif buf.startswith('exec '):
            view.settings().set('syntax', 'Packages/ShellScript/Bash.sublime-syntax')

        elif '/bin/expect' in buf or '/bin/env expect' in buf:
            view.settings().set('syntax', 'Packages/TCL/Tcl.sublime-syntax')
