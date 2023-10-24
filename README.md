## Instructions for Running TEST I

**Note1:** Prior to execution, ensure the installation of the following software: GeneMiner, HybPiper 2.01, aTRAM 2.02,3, Trinity-v2.14.04 and SPAdes v3.15.55

**Note2:** Pay attention to parameter selection and path configuration.

**1. Download Sequencing Data**

Download two public datasets for _Arabidopsis thaliana_ (SRR18391637) and _Oryza sativa_ (SRR9663069) from the European Nucleotide Archive (http://www.ebi.ac.uk)

Place the downloaded files in the TEST I folder or use the following commands to download directly:
```
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR183/037/SRR18391637/SRR18391637_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR183/037/SRR18391637/SRR18391637_2.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR966/009/SRR9663069/SRR9663069_1.fastq.gz
wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR966/009/SRR9663069/SRR9663069_2.fastq.gz
```
**2. Decompression Reference Sequences**

To decompress the Angiosperms353 sequences for Brassicaceae sourced from the Kew Tree of Life Explorer (https://treeoflife.kew.org), use the following command:
```
tar -zxvf ref_Brassicaceae_353.gz
```
To decompress the Angiosperms353 sequences for Poaceae from the same source, use:
```
tar -zxvf ref_Poaceae_353.gz
```
**3. Run work.sh**

Execute the "work.sh" script.

**Introduction to Files and Folders**

INSDC.PRJNA10719.Arabidopsis_thaliana.a353.fasta:
- The Angiosperms353 sequences of _Arabidopsis thaliana_ from Kew Tree of Life Explorer (https://treeoflife.kew.org)

INSDC.PRJDB1747.Oryza_sativa.a353.fasta:
- The Angiosperms353 sequences of _Oryza sativa_ from Kew Tree of Life Explorer (https://treeoflife.kew.org)

ref_Brassicaceae_353:

This directory stores Angiosperms353 sequences of the Brassicaceae family, used as reference sequences for GeneMiner. These reference sequences have been modified and merged from the Angiosperms353 sequences of the Brassicaceae family. Alternatively, you can directly utilize the "gene_file" folder in download_Brassicaceae_353.

ref_Poaceae_353:

This directory stores Angiosperms353 sequences of the Poaceae family, used as reference sequences for GeneMiner. These reference sequences have been modified and merged from the Angiosperms353 sequences of the Poaceae family. Alternatively, you can directly use the "gene_file" folder in download_Poaceae_353.

ref_Brassicaceae_for_hybpiper.fasta:

These reference sequences are utilized for HybPiper and can be obtained by modifying and merging the Angiosperms353 genes from the Brassicaceae family. Alternatively, you can directly use the "ref_hybpiper.fasta" file in download_Brassicaceae_353.

ref_Poaceae_for_hybpiper.fasta:

These reference sequences are utilized for HybPiper and can be obtained by modifying and merging the Angiosperms353 genes from the Poaceae family. Alternatively, you can directly use the "ref_hybpiper.fasta" file in download_Poaceae_353.

work.sh:

This file contains the commands to run TEST I.

## Instructions for Running TEST II
**Note:** Before running, ensure the installation of [NGSNGS](https://github.com/RAHenriksen/NGSNGS)

**Detailed Steps**

- Execute the "work_1.sh" script.
- Create a backup of the "path_of_GeneMiner/lib/my_assemble.py" file.
- Replace the original file with the provided "my_assemble.py" to eliminate the weighted node model.
- Execute the "work_2.sh" script.
- Restore the previously backed-up "my_assemble.py" file.

**Introduction to Files and Folders**

ref_var:

This folder contains sequences with random mutations based on the _Arabidopsis thaliana_ Angiosperms353 gene (with Arabidopsis_thaliana_0 as the gold standard). The number following the folder represents the percentage of mutation.

\*.list files:

These files contain the required identifiers for generating script files. Please refrain from modifying them.

AccFreqL150R1.txt:

This file contains the commands to run the first part of TEST II.

work_1.sh:

This file contains the commands to run the first part of TEST II.

my_assemble.py:

Before running work_2.sh, make a backup of the path_of_GeneMiner/lib/my_assemble.py, and replace the original file with this my_assemble.py to remove the weighted node model.

work_2.sh:

This file contains the commands to run the second part of TEST II.

After running work_2.sh, please restore the backed-up my_assemble.py.

**References**
- Johnson, M. G. et al. HybPiper: Extracting coding sequence and introns for phylogenetics from high‐throughput sequencing reads using target enrichment. Applications in Plant Sciences 4, 1600016 (2016).
- Allen, J. M., Huang, D. I., Cronk, Q. C. & Johnson, K. P. aTRAM - automated target restricted assembly method: a fast method for assembling loci across divergent taxa from next-generation sequencing data. BMC Bioinformatics 16, 98 (2015).
- Allen, J. M., LaFrance, R., Folk, R. A., Johnson, K. P. & Guralnick, R. P. aTRAM 2.0: An Improved, Flexible Locus Assembler for NGS Data. Evol Bioinform Online 14, 117693431877454 (2018).
- Grabherr, M. G. et al. Full-length transcriptome assembly from RNA-Seq data without a reference genome. Nat Biotechnol 29, 644–652 (2011).
- Bankevich, A. et al. SPAdes: A New Genome Assembly Algorithm and Its Applications to Single-Cell Sequencing. Journal of Computational Biology 19, 455–477 (2012).
- Henriksen, R. A., Zhao, L., & Korneliussen, T. S. NGSNGS: next-generation simulator for next-generation sequencing data. Bioinformatics 39 1,btad041 (2023).