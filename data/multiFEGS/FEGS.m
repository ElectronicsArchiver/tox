function FEGS(data)
[P,V]=coordinate;

s = fastaread(strcat('chunks/', num2str(data), '.fasta'));
data={s(:).Sequence};
l=length(data);
char='ARNDCQEGHILKMFPSTWYV';

for i=1:l
    g_p{i}=GRS(data{i},P,V);
    [AAC,DIC]=SAD(data{i},char);
    FA(i,:)=AAC';
    FD(i,:)=DIC(:)';
    for u=1:158
        EL(i,u)=ME(g_p{i}{u});
    end
end

FV=[EL FA FD];
save(strcat('chunks/', num2str(data), '.mat'), FV);