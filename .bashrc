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


alias vim=nvim
# alias alacritty="__GLX_VENDOR_LIBRARY_NAME=nvidia __NV_PRIME_RENDER_OFFLOAD=1 alacritty"
alias mv='mv -i'
alias rm='rm -i'
alias ..='cd ..'

export EDITOR='nvim'
export VISUAL='nvim'

# This line loades the starship on very launch of terminal
eval "$(starship init bash)"


# This line is to use the dircolors the path below is where it is saved.
eval "$(dircolors /home/zeyrie/.dir_colors/dircolors)"

alias config='/usr/bin/git --git-dir=/home/zeyrie/dotfiles --work-tree=/home/zeyrie'
