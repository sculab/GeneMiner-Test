## Instructions for running TEST I

**Note1:** Before running, You should install GeneMiner, HybPiper 2.01, aTRAM 2.02,3, Trinity-v2.14.04, SPAdes v3.15.55
**Note2:** Please pay attention to the parameters selection and path setting.

**1. Download sequencing data**

Two public data sets of Arabidopsis thaliana (SRR18391637) and Oryza sativa (SRR9663069) should be downloaded from the European Nucleotide Archive (http://www.ebi.ac.uk)

Place the downloaded files in the TEST I folder, or you can use the following commands to download directly:

- wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR183/037/SRR18391637/SRR18391637_1.fastq.gz
- wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR183/037/SRR18391637/SRR18391637_2.fastq.gz
- wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR966/009/SRR9663069/SRR9663069_1.fastq.gz
- wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR966/009/SRR9663069/SRR9663069_2.fastq.gz

**2. Download reference sequences**

Download Angiosperms353 sequences of Brassicaceae
- python download_reference.py -d requirement.csv -o download_Brassicaceae_353 -family Brassicaceae  -exclude Arabidopsis_thaliana  -t 4

Download Angiosperms353 sequences of Poaceae
- python download_reference.py -d requirement.csv -o download_Poaceae_353 -family Poaceae -exclude Oryza_sativa  -t 4

**3. Download the gold standard**

INSDC.PRJNA10719.Arabidopsis_thaliana.a353.fasta:
- The Angiosperms353 sequences of Arabidopsis thaliana from Kew Tree of Life Explorer (https://treeoflife.kew.org)

INSDC.PRJDB1747.Oryza_sativa.a353.fasta:
- The Angiosperms353 sequences of Oryza sativa from Kew Tree of Life Explorer (https://treeoflife.kew.org)

**4. ref_Brassicaceae_353**

The directory to store Angiosperms353 sequences of the Brassicaceae family is used as reference sequences for GeneMiner. These reference sequences are modified and merged from the Angiosperms353 sequences of the Brassicaceae family, or you can directly use the “gene_file” folder in download_Brassicaceae_353.

**5. ref_Poaceae_353**

The directory to store Angiosperms353 sequences of the Poaceae family is used as reference sequences for GeneMiner. These reference sequences are modified and merged from the Angiosperms353 sequences of the Poaceae family, or you can directly use the “gene_file” folder in download_Poaceae_353.

**6. ref_Brassicaceae_for_hybpiper.fasta**

The reference sequences are used for HybPiper, which can be obtained by modifying and merging the Angiosperms353 genes from the Brassicaceae family or by directly using the “ref_hybpiper.fasta” file in download_Brassicaceae_353.

**7. ref_Poaceae_for_hybpiper.fasta**

The reference sequences are used for HybPiper, which can be obtained by modifying and merging the Angiosperms353 genes from the Poaceae family or by directly using the “ref_hybpiper.fasta” file in download_ Poaceae_353.

**8. work.sh**

The file records the command to run the TEST I 

## Instructions for running TEST II
**Note:** Before running, you need to first install [NGSNGS](https://github.com/RAHenriksen/NGSNGS)

**1. ref_var**

The folder contains sequences that are randomly mutated based on the Arabidopsis thaliana Angiosperms353 gene (with Arabidopsis_thaliana_0 as the gold standard). The number following the folder represents the percentage of mutation.

**2. \*.list文件**

The required identifiers for generating script files. Please do not modify.

**3. AccFreqL150R1.txt**

From NGSNGS, this is the Read Quality profile for single-end read.

**4. work_1.sh**

The file records the command to run the first part of TEST II.

**5. my_assemble.py**

Before running work_2.sh, please first backup path_of_GeneMiner/lib/my_assemble.py, and replace the original file with this my_assemble.py, to remove the weighted node model.

**6. work_2.sh**

The file records the command to run the second part of TEST II.

After running work_2.sh, please restore the backed-up my_assemble.py.

**References**
- Johnson, M. G. et al. HybPiper: Extracting coding sequence and introns for phylogenetics from high‐throughput sequencing reads using target enrichment. Applications in Plant Sciences 4, 1600016 (2016).
- Allen, J. M., Huang, D. I., Cronk, Q. C. & Johnson, K. P. aTRAM - automated target restricted assembly method: a fast method for assembling loci across divergent taxa from next-generation sequencing data. BMC Bioinformatics 16, 98 (2015).
- Allen, J. M., LaFrance, R., Folk, R. A., Johnson, K. P. & Guralnick, R. P. aTRAM 2.0: An Improved, Flexible Locus Assembler for NGS Data. Evol Bioinform Online 14, 117693431877454 (2018).
- Grabherr, M. G. et al. Full-length transcriptome assembly from RNA-Seq data without a reference genome. Nat Biotechnol 29, 644–652 (2011).
- Bankevich, A. et al. SPAdes: A New Genome Assembly Algorithm and Its Applications to Single-Cell Sequencing. Journal of Computational Biology 19, 455–477 (2012).
- Henriksen, R. A., Zhao, L., & Korneliussen, T. S. NGSNGS: next-generation simulator for next-generation sequencing data. Bioinformatics 39 1,btad041 (2023).