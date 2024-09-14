#!/usr/bin/env fish

# set -l ranges_BMH (seq 10000 2000 100000)
# set -l ranges_Naive (seq 40)
set -l scale 1000
set -g ranges_BMH (seq $scale (math 10 x $scale) (math 500 x $scale))
set -g ranges_Naive $ranges_BMH
set -g needle_len 5
set -g test_n 8

set -gx TP_MACHINE 1
set -g db "times.db"

rm $db

echo $argv
if test "$argv[1]" != 'k'
    rm -r inputs

    function gen -a h
        ./gen.py $GEN_FLAGS --haystack-len $h --needle-len $needle_len
    end

    for x in $ranges_BMH
        gen $x &
    end

    # for x in $ranges_Naive
    #     gen $x &
    # end
    wait
    echo 1
end

alias sqlite=sqlite3

sqlite $db "create table if not exists configuration(id string primary key, haystack_length int, needle_length int, strat string);"
sqlite $db "create table if not exists time(config_id int, user int, system int, clock int);"

function config -a h n strat
    set -l id (sqlite $db "select id from configuration where (haystack_length = $h) and (needle_length = $n) and (strat = '$strat');")
    if test -z "$id"
        sqlite $db "insert into configuration values('$h-$n-$strat', $h, $n, '$strat') returning id;"
    else
        echo $id
    end
end


function insert -a id user system clock
    sqlite $db "insert into time values('$id', $user, $system, $clock);"
end

for strat in BMH Naive
    for x in $(eval echo \$ranges_$strat | string split ' ')
        echo Starting $strat n: $x

        set -l id (config $x $needle_len $strat)
        if test -z "$id"
            echo 'empty id'
            exit 1
        end

        for i in (seq $test_n)
            set out $(./tp3 $strat inputs/entrada-$x.txt)
            if test $status -ne 0
                echo "Error in $strat $test_n $x $out"
                exit 1
            end
            insert $id $out
        end
    end
end
