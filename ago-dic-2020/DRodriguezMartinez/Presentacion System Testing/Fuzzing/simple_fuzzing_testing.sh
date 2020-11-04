> error.txt

for i in {1..200}; 
do python3 simple_fuzzing.py | python3 program_example.py 2>>error.txt; 
done