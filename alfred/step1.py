#!/usr/bin/python
# encoding: utf-8

import sys
import applescript
from workflow import Workflow, web

logger = None

def main(wf):
    scpt = applescript.AppleScript('''
        on getUrls()
            set urls to {}
            tell application "System Events"
                tell process "Safari"
                    set developMenu to menu 1 of menu item "Simulator" of menu 8 of menu bar 1
                    set allUIElements to entire contents of developMenu
                    
                    repeat with anElement in allUIElements
                        try
                            set tmpName to name of anElement

                            set boolName to (offset of "." in tmpName) is not 0
                            
                            if boolName is true then
                                set urls to urls & tmpName
                            end if
                        end try
                    end repeat
                end tell
            end tell

            return urls
        end getUrls
    ''')
    ganks = []
    ganks = scpt.call('getUrls')
    
    if len(ganks) == 0:
        wf.add_item(title=u"没有搜索到要调试的URL",
                        subtitle=u"请确保xcode调试器打开了一个webview页面",
                        arg="",
                        valid=True)
    else:
        for gank in ganks:
            wf.add_item(title=gank,
                        subtitle=gank,
                        arg=gank,
                        valid=True)
    
    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    logger = wf.logger
    sys.exit(wf.run(main))
