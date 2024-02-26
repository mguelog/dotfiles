# ~/.bashrc

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# Prompt
# https://github.com/git/git/blob/master/contrib/completion/git-prompt.sh
. ~/.config/git/git-prompt.sh
export GIT_PS1_SHOWDIRTYSTATE=1
PS1='\[\e[0;1;2;92m\]\u\[\e[0;1;2;92m\]@\[\e[0;1;2;92m\]\h\[\e[0;1m\]:\[\e[0;1;2;94m\]\w\[\e[0;2;3;91m\]$(__git_ps1 "(%s)")\[\e[0;1m\]\$ \[\e[0m\]'

# Aliases
alias grep='grep --color=auto'
alias ls='exa --group-directories-first'
alias tree='exa -T'
alias cat='ccat'
