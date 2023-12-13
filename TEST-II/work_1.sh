###1.resample
mkdir data
rm resample.sh
less reads-depth.list |while read a b;do echo "ngsngs -i TAIR10_chr_all.fas -r ${a} -f fq -l 100 -seq SE -t 1 -q1 AccFreqL150R1.txt -o ./data/${b}" >>resample.sh;done
#run
ParaFly -c resample.sh -CPU 4

###2.depth
#Prepare the commands 
mkdir depth
rm run_depth.sh
less depth.list |while read a ;do echo "geneminer.py -s data/${a}x.fq -rtfa ref_Brassicaceae_353/ -t 4 -o depth/${a}x" >>run_depth.sh;done
#run
ParaFly -c run_depth.sh -CPU 4

###3.var
#Prepare the commands
mkdir var
rm run_var.sh
for i in $(cat depth.list);do for j in $(cat limit.list);do echo "geneminer.py -s data/${i}x.fq -rtfa ref_var/Arabidopsis_thaliana_${j} -t 4 -o var/var_${j} ">>run_var.sh;done;done
#run
ParaFly -c run_var.sh -CPU 4


###4.bootstrap
#Prepare the commands
mkdir bootstrap
rm run_bootstrap.sh
less var.list |while read a;do echo "geneminer.py -s data/50x.fq -rtfa ref_var/Arabidopsis_thaliana_${a} -t 4 -o bootstrap/bootstrap_${a} -bn 50 ">>run_bootstrap.sh;done
#run
ParaFly -c run_bootstrap.sh -CPU 4