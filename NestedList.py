score_collection=[]
only_sc=[]
names=[]
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        record=[name,score]
        score_collection.append(record)
# print(score_collection)
        
for x in score_collection:
    only_sc.append(x[1])

only_sc=sorted(only_sc)

only_sc=list(dict.fromkeys(only_sc))

# print(only_sc)

second_score=only_sc[1]

# print(second_score)

for x in range(len(score_collection)):
    if second_score == score_collection[x][1]:
        names.append(score_collection[x][0])

names=sorted(names)

for name in names:
    print(name)

