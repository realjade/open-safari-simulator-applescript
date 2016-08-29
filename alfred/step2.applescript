on alfred_script(q)
  tell application "Safari"
        activate
        tell application "System Events"
            tell process "Safari"
                click menu item (q) of menu 1 of menu item "Simulator" of menu 8 of menu bar 1
            end tell
        end tell
    end tell
end alfred_script