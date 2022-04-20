#!/bin/sh
#$ -S /bin/bash
#$ -v PATH=/home/data/webcomp/RAMMCAP-ann/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
#$ -v BLASTMAT=/home/data/webcomp/RAMMCAP-ann/blast/bin/data
#$ -v LD_LIBRARY_PATH=/home/data/webcomp/RAMMCAP-ann/gnuplot-install/lib
#$ -v PERL5LIB=/home/hying/programs/Perl_Lib
#$ -q cdhit_webserver.q,fast.q
#$ -pe orte 4
#$ -l h_rt=24:00:00


#$ -e /data5/data/webcomp/web-session/1650433672/1650433672.err
#$ -o /data5/data/webcomp/web-session/1650433672/1650433672.out
cd /data5/data/webcomp/web-session/1650433672
sed -i "s/\x0d/\n/g" 1650433672.fas.0

faa_stat.pl 1650433672.fas.0

/data5/data/NGS-ann-project/apps/cd-hit/cd-hit -i 1650433672.fas.0 -d 0 -o 1650433672.fas.1 -c 0.4 -n 2  -G 1 -g 1 -b 20 -l 10 -s 0.0 -aL 0.0 -aS 0.0 -T 4 -M 32000
faa_stat.pl 1650433672.fas.1
/data5/data/NGS-ann-project/apps/cd-hit/clstr_sort_by.pl no < 1650433672.fas.1.clstr > 1650433672.fas.1.clstr.sorted
/data5/data/NGS-ann-project/apps/cd-hit/clstr_list.pl 1650433672.fas.1.clstr 1650433672.clstr.dump
gnuplot1.pl < 1650433672.fas.1.clstr > 1650433672.fas.1.clstr.1; gnuplot2.pl 1650433672.fas.1.clstr.1 1650433672.fas.1.clstr.1.png
/data5/data/NGS-ann-project/apps/cd-hit/clstr_list_sort.pl 1650433672.clstr.dump 1650433672.clstr_no.dump
/data5/data/NGS-ann-project/apps/cd-hit/clstr_list_sort.pl 1650433672.clstr.dump 1650433672.clstr_len.dump len
/data5/data/NGS-ann-project/apps/cd-hit/clstr_list_sort.pl 1650433672.clstr.dump 1650433672.clstr_des.dump des
tar -zcf 1650433672.result.tar.gz * --exclude=*.dump --exclude=*.env
echo hello > 1650433672.ok
