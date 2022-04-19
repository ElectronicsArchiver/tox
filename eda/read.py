from Bio import SeqIO


# TOXIBTL
toxibtlPosSeqs = []
toxibtlNegSeqs = []

toxibtlProteinTrainSeqs = SeqIO.parse(open('../data/toxibtl/protein/train.fa'), 'fasta')
for fasta in toxibtlProteinTrainSeqs:
    _, isPos = fasta.description.split('\t')
    seq = str(fasta.seq)
    toxibtlNegSeqs.append(seq) if isPos == '0' else toxibtlPosSeqs.append(seq)

toxibtlProteinTestSeqs = SeqIO.parse(open('../data/toxibtl/protein/test.fa'), 'fasta')
for fasta in toxibtlProteinTestSeqs:
    _, isPos = fasta.description.split('\t')
    seq = str(fasta.seq)
    toxibtlNegSeqs.append(seq) if isPos == '0' else toxibtlPosSeqs.append(seq)

toxibtlPeptideSeqs = SeqIO.parse(open('../data/toxibtl/peptide/peptide.fasta'), 'fasta')
for fasta in toxibtlPeptideSeqs:
    isPos, _ = fasta.description.split(' ')
    seq = str(fasta.seq)
    toxibtlNegSeqs.append(seq) if isPos == '|non-toxin' else toxibtlPosSeqs.append(seq)

print(len(toxibtlPosSeqs))
print(len(toxibtlNegSeqs))
# print(toxibtlPosSeqs)
# print(toxibtlNegSeqs)

# TOXINPRED

toxinpredPosSeqs = []
toxinpredNegSeqs = []

posFiles = ['../data/toxinpred/toxinpred-main-pos-1.txt', '../data/toxinpred/toxinpred-main-pos-2.txt', '../data/toxinpred/toxinpred-ind-pos-1.txt', '../data/toxinpred/toxinpred-ind-pos-2.txt']
negFiles = ['../data/toxinpred/toxinpred-main-neg-1.txt', '../data/toxinpred/toxinpred-main-neg-2.txt', '../data/toxinpred/toxinpred-ind-neg-1.txt', '../data/toxinpred/toxinpred-ind-neg-2.txt']

lines = []
for file in posFiles:
    with open(file) as f:
        lines = f.read().splitlines()
        toxinpredPosSeqs.extend(lines)
for file in negFiles:
    with open(file) as f:
        lines = f.read().splitlines()
        toxinpredNegSeqs.extend(lines)

print(len(toxinpredPosSeqs))
print(len(toxinpredNegSeqs))

