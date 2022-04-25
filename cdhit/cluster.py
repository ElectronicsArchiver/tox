from collections import defaultdict

lines = []
with open("./posSeqsResult/1650433672.fas.1.clstr.sorted", "r") as f:
    lines = f.read().splitlines()

currCluster = None
clusterToProteins = defaultdict(set)
numProteins = 0
proteinIds = []
# proteinToClusters = defaultdict(set)
for line in lines:
    if line.startswith('>Cluster'):
        currCluster = int(line.split()[1])
    else:
        proteinId = int(line.split('\t')[1].split('>')[1].split('...')[0])
        clusterToProteins[currCluster].add(proteinId)
        numProteins += 1
        proteinIds.append(proteinId)
        # proteinToClusters[proteinId].add(currCluster)

proteinIds.sort()

# print(proteinIds)
ids = [i for i in range(6942)]
notThere = []
for protid in ids:
    if protid not in proteinIds:
        notThere.append(protid)
print(notThere)

print("number of proteins: ", numProteins)
print("goal train: ", numProteins * 0.9)
print("goal test: ", numProteins * 0.1)

# print(clusterToProteins[0])
# print(proteinToClusters[680])

