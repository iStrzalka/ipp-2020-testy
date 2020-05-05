#!/bin/bash

VALGRIND="valgrind "

function run_test(){
    test_str="$1"
    max_allocs=$2
    max_mem=$3
    should_fail=$4

    cd /part2/
    rm -rf gamma
    cp -r original_gamma gamma
    cd gamma/src

    sed -i 's/main/original_main/g' gamma_main.c

    for f in *.c; do 
        printf "#include \"remalloc.h\"\n\n" > tempfile.c
        cat $f >> tempfile.c
        mv tempfile.c $f
        sed -i 's/free(/myfree(/g' $f
        sed -i 's/malloc(/mymalloc(/g' $f
        sed -i 's/calloc(/mycalloc(/g' $f
        sed -i 's/realloc(/myrealloc(/g' $f
    done

    cp /part2/tests/remalloc.h remalloc.h
    cp /part2/tests/remalloc.c remalloc.c

    cat /part2/tests/test_max_n_allocs.c >> gamma_main.c
    sed -i 's/MAX_ALLOCS/'"$max_allocs"'/g' remalloc.c
    sed -i 's/MAX_MEMORY_ALLOCATED/'"$max_mem"'/g' remalloc.c
    
    cd ..
    sed -i 's/(SOURCE_FILES/(SOURCE_FILES src\/remalloc.h src\/remalloc.c/g' CMakeLists.txt

    mkdir -p debug && cd debug
    cmake -d cmake -D CMAKE_BUILD_TYPE=Debug .. > /dev/null && make >/dev/null 2>/dev/null
    #cmake -d cmake -D CMAKE_BUILD_TYPE=Debug .. > /dev/null && make

    printf "$test_str" | ./gamma > /dev/null 2> /dev/null
    gamma_exit_code=$?
    printf "$test_str" | $VALGRIND --error-exitcode=42 --log-file=valgrind_out ./gamma > /dev/null
    valgrind_exit_code=$?

    printf "Test: "
    echo "$test_str"
    echo "NULL po $max_allocs alokacjach"
    if [ "$valgrind_exit_code" -eq "42" ] 
    then
        echo "ERROR blad pamieci valgrinda"
        cat valgrind_out
    else
        echo "PAMIEC OK"
    fi

    if [ "$should_fail" -eq "2" ] 
    then  # czyli nie wiadomo czy ma byc fail czy nie, zalezy od implementacji
        echo "KOD PROGRAMU ZALEZNY OD IMPLEMENTACJI"
        echo
        return
    fi

    if [ "$should_fail" -eq "0" ] 
    then
        if [ "$gamma_exit_code" -eq "0" ] 
        then
            echo "KOD PROGRAMU OK"
        else
            echo "KOD GAMMA BLEDNY"
        fi
    else
        if [ "$gamma_exit_code" -eq "0" ] 
        then
            echo "KOD GAMMA BLEDNY"
        else
            echo "KOD PROGRAMU OK"
        fi
    fi
    echo
}

rm -rf test_gamma
cp -r original_gamma test_gamma
cd test_gamma/src

sed -i 's/main/original_main/g' gamma_main.c
cp gamma_main.c original_gamma_main.c

printf "\nTesty wywalajace malloca, jezeli nie ma outputu to znaczy ze wszystko dobrze\n"

printf "\nTesty na max 7 alokacji\n\n"

run_test "B 1 1 1 1\np\n" 7 100000000 0
run_test "B 1 0 1 1\nB 0 1 1 1\nB 1 1 0 1\nB 1 1 1 0\n" 7 100000000 0
run_test "B 1 1 1 1\np\n" 7 100000000 0
run_test "B 5 5 5 1\np\n\np\n\np\n\np\n\np\n\np\n\np\n\np\n\np\np\np\np\np\np\np\np\np\n" 5 100000000 1

run_test "B 2 2 2 1\np\np\np\n" 0 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 1 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 3 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 4 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 5 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 6 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 7 100000000 1
run_test "B 2 2 2 1\np\np\np\n" 8 100000000 0
run_test "B 2 2 2 1\np\np\np\n" 9 100000000 0

run_test "B 2 0 2 1\nB -2 2 2 1\nB 2 2 -2 1\nB 2 2 r\nB eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 2 2 1\nB 2 2 1\nB 2c 2 2 1\nB 1 1 2 1\np\n" 0 100000000 1
run_test "B 2 0 2 1\nB -2 2 2 1\nB 2 2 -2 1\nB 2 2 r\nB eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 2 2 1\nB 2 2 1\nB 2c 2 2 1\nB 1 1 2 1\np\n" 1 100000000 1
run_test "B 2 0 2 1\nB -2 2 2 1\nB 2 2 -2 1\nB 2 2 r\nB eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 2 2 1\nB 2 2 1\nB 2c 2 2 1\nB 1 1 2 1\np\n" 2 100000000 2
run_test "B 2 0 2 1\nB -2 2 2 1\nB 2 2 -2 1\nB 2 2 r\nB eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 2 2 1\nB 2 2 1\nB 2c 2 2 1\nB 1 1 2 1\np\n" 3 100000000 2
run_test "B 2 0 2 1\nB -2 2 2 1\nB 2 2 -2 1\nB 2 2 r\nB eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee 2 2 1\nB 2 2 1\nB 2c 2 2 1\nB 1 1 2 1\np\n" 5 100000000 0

run_test "I 0 2 2 1\n" 0 100000000 2
run_test "I 0 2 2 1\n" 1 100000000 0
run_test "I 1 1 1 1\n" 1 100000000 2
run_test "I 1 1 1 1\n" 2 100000000 0
run_test "I 1 1 1 1\n" 3 100000000 0