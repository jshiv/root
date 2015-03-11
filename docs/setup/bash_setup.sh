

 
check_if_line_exists()
{
    # grep wont care if one or both files dont exist.
    grep -qsFx "$LINE_TO_ADD" ~/.profile ~/.bash_profile
}
 
add_line_to_profile()
{
    profile=~/.profile
    [ -w "$profile" ] || profile=~/.bash_profile
    printf "%s\n" "$LINE_TO_ADD" >> "$profile"
}
 



LINE_TO_ADD='alias ls="ls -G"'
check_if_line_exists || add_line_to_profile

LINE_TO_ADD='alias ipynb="ipython notebook --pylab inline"'
check_if_line_exists || add_line_to_profile

LINE_TO_ADD="alias showFiles='defaults write com.apple.finder AppleShowAllFiles YES; killall Finder /System/Library/CoreServices/Finder.app'"
check_if_line_exists || add_line_to_profile

LINE_TO_ADD="alias hideFiles='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'"
check_if_line_exists || add_line_to_profile

LINE_TO_ADD="alias hideFiles='defaults write com.apple.finder AppleShowAllFiles NO; killall Finder /System/Library/CoreServices/Finder.app'"
check_if_line_exists || add_line_to_profile


LINE_TO_ADD='export JAVA_HOME="/Library/Internet Plug-Ins/JavaAppletPlugin.plugin/Contents/Home"'
check_if_line_exists || add_line_to_profile




