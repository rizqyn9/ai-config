# env

export AI_SUMAPOD_RDEV=sk-MEFNnc0KKYQEYzvrPRCVVQ
export AI_9ROUTER=sk-bf36b554c6c889ba-qx7isy-3e966ea9

# Config overlays: share sessions, memory and rules with the default omp; only override settings.
_omp_dir="${${(%):-%x}:A:h}"
alias omp-lite='omp --config "$_omp_dir/profiles/lite.yml"'
alias omp-pro='omp --config "$_omp_dir/profiles/pro.yml"'
