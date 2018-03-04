# decorate python fcns with @profile

kernprof -l -o $1.lprof $1
python3 -m line_profiler $1.lprof
