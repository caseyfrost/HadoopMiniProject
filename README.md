# HadoopMiniProject

To run the code from terminal:

cat data.csv | python mapper1.py | sort | python reducer1.py | python mapper2.py | sort |
python reducer2.py

To run this code in distributed mode, using virtual box and hortonworks sandbox
1. configure your sandbox environment
2. create your input directory in your HDFS
3. edit the input directory path within the .sh file to match that of your HDFS
4. run the .sh file from your virtual machine
