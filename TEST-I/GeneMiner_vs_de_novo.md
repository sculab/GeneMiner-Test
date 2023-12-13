Typically, employing reference-guided de novo assembly on filtered data leads to more favorable outcomes than the direct application of de novo assembly software on unfiltered reads. To validate this assertion, consider conducting re-sampling at various depths using the TEST I dataset. Utilize the following commands to run Minia, SPAdes, and Trinity on unfiltered reads, and then compare these results with those obtained from GeneMiner.


**Resampling**

Raw Data of *Arabidopsis thaliana*: SRR18391637

Raw Data of *Oryza sativa*: SRR9663069

Resampling Tool: seqkit v2.5.1

Athaliana_*.fq: * coverage FASTQ-format reads of *Arabidopsis thaliana*

Osativa_*.fq: * coverage FASTQ-format reads *Oryza sativa*

**Arabidopsis_thaliana**

```shell
#Minia v3.2.5
minia -in Athaliana_5.fq -out minia_out/Athaliana_5  -out-dir minia_out/Athaliana_5 -nb-cores 10
minia -in Athaliana_10.fq -out minia_out/Athaliana_10  -out-dir minia_out/Athaliana_10 -nb-cores 10
minia -in Athaliana_20.fq -out minia_out/Athaliana_20  -out-dir minia_out/Athaliana_20 -nb-cores 10
minia -in Athaliana_50.fq -out minia_out/Athaliana_50  -out-dir minia_out/Athaliana_50 -nb-cores 10

#SPAdes v3.15.5
spades.py -s Athaliana_5.fq -t 10 -m 50 -o spades_out/Athaliana_5
spades.py -s Athaliana_10.fq -t 10 -m 50 -o spades_out/Athaliana_10
spades.py -s Athaliana_20.fq -t 10 -m 50 -o spades_out/Athaliana_20
spades.py -s Athaliana_50.fq -t 10 -m 50 -o spades_out/Athaliana_50

#Trinity v2.15.1
Trinity  --seqType fq --max_memory 50G --single Athaliana_5.fq  --CPU 10 --output trinity_out/trinity_Athaliana_5
Trinity  --seqType fq --max_memory 50G --single Athaliana_10.fq  --CPU 10 --output trinity_out/trinity_Athaliana_10
Trinity  --seqType fq --max_memory 50G --single Athaliana_20.fq  --CPU 10 --output trinity_out/trinity_Athaliana_20
Trinity  --seqType fq --max_memory 50G --single Athaliana_50.fq  --CPU 10 --output trinity_out/trinity_Athaliana_50

#GeneMiner v1.1
geneminer.py -s Athaliana_5.fq -rtfa ref_Brassicaceae_353/ -t 10 -o  geneminer_Athaliana_5 -limit_count auto -b 10000
geneminer.py -s Athaliana_10.fq -rtfa ref_Brassicaceae_353/ -t 10 -o geneminer_Athaliana_5 -limit_count auto -b 10000 
geneminer.py -s Athaliana_20.fq -rtfa ref_Brassicaceae_353/ -t 10 -o geneminer_Athaliana_5 -limit_count auto -b 10000 
geneminer.py -s Athaliana_50.fq -rtfa ref_Brassicaceae_353/ -t 10 -o geneminer_Athaliana_5 -limit_count auto -b 10000 
```

**Oryza_sativa**

```shell
#Minia v3.2.5
minia -in Osativa_5.fq -out minia_out/Osativa_5  -out-dir minia_out/Osativa_5 -nb-cores 10
minia -in Osativa_10.fq -out minia_out/Osativa_10  -out-dir minia_out/Osativa_10 -nb-cores 10
minia -in Osativa_20.fq -out minia_out/Osativa_20  -out-dir minia_out/Osativa_20 -nb-cores 10
minia -in Osativa_50.fq -out minia_out/Osativa_50  -out-dir minia_out/Osativa_50 -nb-cores 10
#SPAdes v3.15.5
spades.py -s Osativa_5.fq -t 10 -m 50 -o spades_out/Osativa_5
spades.py -s Osativa_10.fq -t 10 -m 50 -o spades_out/Osativa_10
spades.py -s Osativa_20.fq -t 10 -m 50 -o spades_out/Osativa_20
spades.py -s Osativa_50.fq -t 10 -m 50 -o spades_out/Osativa_50

#Trinity v2.15.1
Trinity  --seqType fq --max_memory 50G --single Osativa_5.fq  --CPU 10 --output trinity_out/trinity_Osativa_5
Trinity  --seqType fq --max_memory 50G --single Osativa_10.fq  --CPU 10 --output trinity_out/trinity_Osativa_10
Trinity  --seqType fq --max_memory 50G --single Osativa_20.fq  --CPU 10 --output trinity_out/trinity_Osativa_20
Trinity  --seqType fq --max_memory 50G --single Osativa_50.fq  --CPU 10 --output trinity_out/trinity_Osativa_50

#GeneMiner v1.1
geneminer.py  -rtfa ref_Poaceae_353/ -s Osativa_5.fq -o geneminer_out/Osativa_5 -t 10 -b 10000 -limit_count auto
geneminer.py  -rtfa ref_Poaceae_353/ -s Osativa_10.fq -o geneminer_out/Osativa_10 -t 10 -b 10000 -limit_count auto
geneminer.py  -rtfa ref_Poaceae_353/ -s Osativa_20.fq -o geneminer_out/Osativa_20 -t 10 -b 10000 -limit_count auto
geneminer.py  -rtfa ref_Poaceae_353/ -s Osativa_50.fq -o geneminer_out/Osativa_50 -t 10 -b 10000 -limit_count auto
```



