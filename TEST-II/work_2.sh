### weighted node model free
#Prepare the commands
mkdir weighted_model_free
rm run_wmf.sh
less depth.list |while read a ;do echo "geneminer.py -s data/${a}x.fq -rtfa ref_Brassicaceae_353/ -t 4 -o weighted_model_free/${a}x" >>run_wmf.sh;done
#run
ParaFly -c run_wmf.sh -CPU 4