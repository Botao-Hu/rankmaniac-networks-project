for((i=1;i<=50;i++));
do

python pagerank_map.py < input.txt | sort | python pagerank_reduce.py | python process_map.py | sort | python process_reduce.py > output.txt
rm input.txt
cp output.txt input.txt

echo '-----Iteration!-----'

if grep -q FinalRank input.txt 
then
	echo 'Convergence!'
    break
fi

done