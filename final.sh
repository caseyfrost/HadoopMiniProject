
hadoop jar  /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file mapper1.py -mapper mapper1.py \
-file reducer1.py -reducer reducer1.py \
-input input/data.csv -output output/output1

hadoop jar  /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file mapper2.py -mapper mapper1.py \
-file reducer2.py -reducer reducer1.py \
-input /user/admin/first_output -output /user/admin/output/final_output