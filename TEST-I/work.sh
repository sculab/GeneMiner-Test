### decompress all gz files to speed up the analysis
tar -zcvf ref_Brassicaceae_353.gz
tar -zcvf ref_Poaceae_353.gz

###1. Run GeneMiner
#(1) Arabidopsis thaliana
geneminer.py -1 SRR18391637_1.fastq -2 SRR18391637_2.fastq  -rtfa ref_Brassicaceae_353/ -o geneminer_out_Arabidopsis_thaliana -t 4 -k1 29 -k2 41 -limit_count auto
#(2) Oryza sativa
geneminer.py  -1 SRR9663069_1.fastq -2 SRR9663069_2.fastq  -rtfa ref_Poaceae_353/ -o geneminer_out_Oryza_sativa -t 4 -k1 29 -k2 41 -limit_count auto


###2. Run HybPiper
#(1) Arabidopsis thaliana
hybpiper assemble -t_dna Brassicaceae_hybpiper.fasta  -r SRR18391637_1.fastq  SRR18391637_2.fastq  --prefix hybpiper_out_Arabidopsis_thaliana -run_intronerate  --bwa --cpu 4
#(2) Oryza sativa
hybpiper assemble -t_dna Poaceae_hybpiper.fasta  -r  SRR9663069_1.fastq SRR9663069_2.fastq  --prefix  hybpiper_out_Oryza_sativa -run_intronerate --bwa --cpu 4


###3. Run aTRAM
#(1) Arabidopsis thaliana
atram_preprocessor.py --cpus 4 -b atram_out_Arabidopsis_thaliana/blastdb/index -1 SRR18391637_1.fastq -2 SRR18391637_2.fastq
mkdir -p atram_out_Arabidopsis_thaliana/atram_out
atram.py  -b atram_out_Arabidopsis_thaliana/blastdb/index -q ref_Brassicaceae_353/* -o atram_out_Arabidopsis_thaliana/atram_out --cpus 4 -a spades -i 1 
#(2) Oryza sativa
atram_preprocessor.py --cpus 4 -b atram_out_Oryza_sativa/blastdb/index -1 SRR9663069_1.fastq -2 SRR9663069_2.fastq 
mkdir -p atram_out_Oryza_sativa/atram_out
atram.py  -b atram_out_Oryza_sativa/blastdb/index -q ref_Poaceae_353/* -o atram_out_Oryza_sativa/atram_out --cpus 4 -a spades -i 1 


###4. Run Trinity
#(1) Arabidopsis thaliana
Trinity --seqType fq --max_memory 50G --left SRR18391637_1.fastq --right SRR18391637_2.fastq  --CPU 4 --output  trinity_out_Arabidopsis_thaliana
#(2) Oryza sativa
Trinity --seqType fq --max_memory 50G --left SRR9663069_1.fastq  --right SRR9663069_2.fastq   --CPU 4 --output  trinity_out_Oryza_sativa



###5. Run SPAdes
#(1) Arabidopsis thaliana
spades.py -1 SRR18391637_1.fastq -2 SRR9663069_1.fastq  -t 4 -m 50 -o spades_out_Arabidopsis_thaliana
#(2) Oryza sativa
spades.py -1 SRR9663069_1.fastq -2 SRR9663069_2.fastq  -t 4 -m 50 -o spades_out_Oryza_sativa















