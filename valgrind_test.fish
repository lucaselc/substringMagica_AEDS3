#!/usr/bin/env fish

for strat in BMH Naive
    for f in inputs/(ls inputs/) entrada.txt
        echo -en "[$strat] :: "

        valgrind ./tp3 $strat $f
        set -l code $status

        echo $code

        if test $code -eq 0
            echo -en "\e[32mSucesso"
        else
            echo -en "\e[31mFalha"
        end

        echo -e " \e[0m:: $f"

        if test $code -ne 0
            exit 1
        end
    end
end
