import sys

for line in sys.stdin:
    data = line.strip().split(',')
    print(f'{data[2]}\t("{data[1]}", "{data[3]}", "{data[5]}")')


# for testing
# csv = r"/Users/caseyfrost/Desktop/Springboard/HadoopMiniProject/data.csv"
# csv_out = r"/Users/caseyfrost/Desktop/Springboard/HadoopMiniProject/map1_out.csv"
#
# with open(csv_out, 'w') as out_file:
#     with open(csv) as file:
#         for line in file.readlines():
#             data = line.strip().split(',')
#             line = f'{data[2]}\t("{data[1]}", "{data[3]}", "{data[5]}")'
#             print(line)
#             out_file.write(line + '\n')
