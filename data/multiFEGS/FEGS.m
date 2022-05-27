function FEGS(chunkdir, filenum)

filename = strcat(num2str(chunkdir), num2str(filenum), '.fasta');
outfile = strcat(num2str(chunkdir), num2str(filenum), '.mat');

if isfile(outfile) || ~isfile(filename)
    return
end

[P,V] = coordinate;
s = fastaread(filename);
data=upper({s(:).Sequence});
l=length(data);

for i=1:l
    g_p{i}=GRS(data{i},P,V);
    for u=1:158
        EL(i,u)=ME(g_p{i}{u});
    end
end

char='ARNDCQEGHILKMFPSTWYV';
for i=1:l
    [AAC,DIC]=SAD(data{i},char);
    FA(i,:)=AAC';
    FD(i,:)=DIC(:)';
end

FV=[EL FA FD];
save(outfile, 'FV');
