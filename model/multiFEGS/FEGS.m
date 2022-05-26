function FV = FEGS(data)

pkg load bioinfo
[P, V] = coordinate;
s = fastaread(strcat(num2str(data), '.fasta'));

for i = 1:length(s)
    seqs{i} = {s{i}.Sequence};
end

l=length(data);
parfor i=1:l
    g_p{i}=GRS(seqs{i},P,V);
    for u=1:158
        EL(i,u)=ME(g_p{i}{u});
    end
end

char='ARNDCQEGHILKMFPSTWYV';
parfor i=1:l
    [AAC,DIC]=SAD(seqs{i},char);
    FA(i,:)=AAC';
    FD(i,:)=DIC(:)';
end

FV=[EL FA FD];