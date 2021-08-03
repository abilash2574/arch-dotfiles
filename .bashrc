#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='[\u@\h \W]\$ '

# set a fancy prompt (non-color, unless we know we "want" color)
case "$TERM" in
    xterm-color|*-256color) color_prompt=yes;;
esac


# some more ls aliases
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'


### RANDOM COLOR SCRIPT ###
#   Get this script from GitLab: https://gitlab.com/dwt1/shell-color-scripts
colorscript random


# >>> Terminal Cosmetic <<<<<<<

# Creating a function
function selArt(){

    # num=1
    num=$(((RANDOM % 10) ))
    
    case "$num" in 
        1)
            clear && figlet -f Bloody "ZEYRIE" | lolcat
            ;;
        2)
            clear && figlet -f Poison "ZEYRIE" | lolcat
            ;;
        3)
            clear && figlet -f sblood "ZEYRIE" | lolcat
            ;;
        4)
            clear && figlet -f Roman "ZEYRIE" | lolcat
            ;;
        5)
            clear && figlet -f Bright "ZEYRIE" | lolcat
            ;;
        6) 
            clear && figlet -f Banner3-D "ZEYRIE" | lolcat
            ;;
        7)
            clear && figlet -f Colossal "ZeYrIe" | lolcat
            ;;
        8)
            clear && figlet -f Varsity "ZEYRIE" | lolcat
            ;;
        9)
            clear && figlet -f cosmic "Zeyrie" | lolcat
            ;;
        *)
            clear && figlet -f Univers "Zeyrie" | lolcat
            ;;
    esac

}

alias clear=selArt 

# >>> Terminal Ending <<<<<<<

alias vim=nvim
# alias alacritty="__GLX_VENDOR_LIBRARY_NAME=nvidia __NV_PRIME_RENDER_OFFLOAD=1 alacritty"
alias mv='mv -i'
alias rm='rm -i'
alias ..='cd ..'

export EDITOR='nvim'
export VISUAL='nvim'
export PATH=$PATH:~/bin

# This line loades the starship on very launch of terminal
eval "$(starship init bash)"


# This line is to use the dircolors the path below is where it is saved.
eval "$(dircolors /home/zeyrie/.dir_colors/dircolors)"

alias config='/usr/bin/git --git-dir=/home/zeyrie/dotfiles --work-tree=/home/zeyrie'
# alias maim_to_clip='maim -s |  xclip -selection clipboard -t image/png'

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/zeyrie/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/zeyrie/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/zeyrie/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/zeyrie/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<







