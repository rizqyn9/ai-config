# Config overlays: share sessions, memory and rules with the default omp; only override settings.
_omp_dir="${${(%):-%x}:A:h}"
alias omp-lite='omp --config "$_omp_dir/profiles/lite.yml"'
alias omp-pro='omp --config "$_omp_dir/profiles/pro.yml"'
