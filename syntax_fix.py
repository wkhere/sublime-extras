#
# put it in ~/.config/sublime-text/Packages/User/

import sublime, sublime_plugin

BufSize = max(
    len('#!/usr/local/bin rubyN.NN.NN'), 
    len('#!/usr/bin/env rubyN.NN.NN'),
)


class SyntaxFix(sublime_plugin.EventListener):

    def on_load(self, view):
        buf = view.substr(sublime.Region(0, BufSize))

        if '/bin/ruby' in buf or '/bin/env ruby' in buf:
           view.settings().set('syntax', 'Packages/Ruby/Ruby.sublime-syntax')
