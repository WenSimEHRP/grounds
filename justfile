# preprocess and compile

file := "grounds"

def: preprocess compile
    @echo "Build complete"

# preprocess using gcc
preprocess:
    gcc -E -x c {{file}}.pnml > {{file}}.nml

# compile using nmlc
compile:
    nml/nmlc -c {{file}}.nml --md5={{file}}.md5 --nml={{file}}_parsed.nml --grf={{file}}.grf
    cat {{file}}.md5

# copy to openttd newgrf directory (linux)
cp:
    cp ./{{file}}.grf ~/.local/share/openttd/newgrf/

check:
    nml/nmlc {{file}}_parsed.nml
