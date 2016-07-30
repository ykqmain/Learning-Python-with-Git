test

function lazygit() {
    git add .
    git commit -m "updated: $(date +"%Y-%m-%d %T")"
    git push
}


lazy

datetest