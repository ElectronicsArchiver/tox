from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

########## TOXIBTL ##########
toxibtlPosSeqs = set()
toxibtlNegSeqs = set()

toxibtlPosRepeats = set()
toxibtlNegRepeats = set()

toxibtlProteinTrainSeqs = SeqIO.parse(open('../data/toxibtl/protein/train.fa'), 'fasta')
for fasta in toxibtlProteinTrainSeqs:
    _, isPos = fasta.description.split('\t')
    seq = str(fasta.seq)
    if isPos == '0':
        if seq in toxibtlNegSeqs:
            toxibtlNegRepeats.add(seq)
        toxibtlNegSeqs.add(seq)
    else:
        if seq in toxibtlPosSeqs:
            toxibtlPosRepeats.add(seq)
        toxibtlPosSeqs.add(seq)

toxibtlProteinTestSeqs = SeqIO.parse(open('../data/toxibtl/protein/test.fa'), 'fasta')
for fasta in toxibtlProteinTestSeqs:
    _, isPos = fasta.description.split('\t')
    seq = str(fasta.seq)
    if isPos == '0':
        if seq in toxibtlNegSeqs:
            toxibtlNegRepeats.add(seq)
        toxibtlNegSeqs.add(seq)
    else:
        if seq in toxibtlPosSeqs:
            toxibtlPosRepeats.add(seq)
        toxibtlPosSeqs.add(seq)

toxibtlPeptideSeqs = SeqIO.parse(open('../data/toxibtl/peptide/peptide.fasta'), 'fasta')
for fasta in toxibtlPeptideSeqs:
    isPos, _ = fasta.description.split(' ')
    seq = str(fasta.seq)
    if isPos == '|non-toxin':
        if seq in toxibtlNegSeqs:
            toxibtlNegRepeats.add(seq)
        toxibtlNegSeqs.add(seq)
    else:
        if seq in toxibtlPosSeqs:
            toxibtlPosRepeats.add(seq)
        toxibtlPosSeqs.add(seq)

# sanity check:
# print(len(toxibtlPosSeqs))
# print(len(toxibtlNegSeqs))

# print(len(toxibtlPosRepeats))
# print(len(toxibtlNegRepeats))
# CONCLUSION: there are repeat sequences between the protein/peptide train/test datasets! (not good!)

########## TOXINPRED ##########

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

posNotInIBTL = []
for seq in set(toxinpredPosSeqs):
    if seq not in toxibtlPosSeqs:
        posNotInIBTL.append(seq)
negNotInIBTL = []
for seq in set(toxinpredNegSeqs):
    if seq not in toxibtlNegSeqs:
        negNotInIBTL.append(seq)

# sanity check:
print(len(set(toxinpredPosSeqs)))
print(len(set(toxinpredNegSeqs)))
# CONCLUSION: data splits have repeats

# print(len(posNotInIBTL))
# print(len(negNotInIBTL))
# CONCLUSION: toxinpred dataset contains sequences NOT in the ToxIBTL dataset

########## TOXDL ##########

toxdlPosSeqs = set()
toxdlNegSeqs = set()

toxdlNegRepeats = set()
toxdlPosRepeats = set()

toxdlFiles = ['../data/toxdl/bacteria1.fa', '../data/toxdl/test.fa', '../data/toxdl/train.fa', '../data/toxdl/valid.fa']
for file in toxdlFiles:
    toxdlSeqs = SeqIO.parse(open(file), 'fasta')
    for fasta in toxdlSeqs:
        _, isPos = fasta.description.split('\t')
        seq = str(fasta.seq)
        if isPos == '0':
            if seq in toxdlNegSeqs:
                toxdlNegRepeats.add(seq)
            toxdlNegSeqs.add(seq)
        else:
            if seq in toxdlPosSeqs:
                toxdlPosRepeats.add(seq)
            toxdlPosSeqs.add(seq)

# sanity check:
# print(len(toxdlPosSeqs))
# print(len(toxdlNegSeqs))

# print(len(toxdlPosRepeats))
# print(len(toxdlNegRepeats))
# CONCLUSION: repeats exist in different splits of toxDL dataset

toxdlPosNotInIBTL = []
for seq in toxdlPosSeqs:
    if seq not in toxibtlPosSeqs:
        toxdlPosNotInIBTL.append(seq)
toxdlNegNotInIBTL = []
for seq in toxdlNegSeqs:
    if seq not in toxibtlNegSeqs:
        toxdlNegNotInIBTL.append(seq)

print(len(toxdlPosNotInIBTL))
print(len(toxdlNegNotInIBTL))
# CONCLUSION: toxindl dataset contains sequences NOT in the ToxIBTL dataset

########## WRITE TO FASTA FILE ##########

posSeqs = set(toxibtlPosSeqs.union(toxinpredPosSeqs).union(toxdlPosSeqs))
negSeqs = set(toxibtlNegSeqs.union(toxinpredNegSeqs).union(toxdlNegSeqs))
posSeqs = [SeqRecord(Seq(seq), id=str(i)) for i, seq in enumerate(posSeqs)]
negSeqs = [SeqRecord(Seq(seq), id=str(i)) for i, seq in enumerate(negSeqs)]

print(len(posSeqs))

# with open("../cdhit/input/posSeqs.fasta", "w") as f:
#     SeqIO.write(posSeqs, f, "fasta")
# with open("../cdhit/input/negSeqs.fasta", "w") as f:
#     SeqIO.write(negSeqs, f, "fasta")
