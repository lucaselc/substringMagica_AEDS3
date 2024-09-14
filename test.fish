#!/usr/bin/env fish

for strat in BMH Naive
    for f in (ls inputs) entrada.txt
        echo -en "[$strat] :: "
        if ./tp3 $strat $f | rg -i 'Diferença' > /dev/null
            echo -en "\e[31mFalha"
        else
            echo -en "\e[32mSucesso"
        end

        echo -e " \e[0m:: $f"
    end
end
