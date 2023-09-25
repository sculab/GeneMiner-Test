#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 14:57
# @Author  : xiepulin
# @File    : download_reference.py
# @Software: PyCharm
import csv
import os
import argparse
import sys

import time
from Bio import SeqIO
from Bio import pairwise2
from Bio.SeqRecord import  SeqRecord
from Bio.Seq import  Seq
import subprocess
from concurrent.futures import ProcessPoolExecutor
from collections import  defaultdict
import urllib
from urllib.request import urlretrieve
from urllib.error import HTTPError
import socket


def run_command(cmd):
    subprocess.call(cmd,shell=True)

def get_file_list(path):
    file_list = []
    if os.path.isdir(path):
        files = get_files(path)
        for i in files:
            if os.path.getsize(i) == 0:
                pass
            else:
                file_list.append(i)
    elif os.path.isfile(path):
        size = os.path.getsize(path)
        if size == 0:
            pass
        else:
            file_list.append(path)
    else:
        pass
    return file_list


def get_files(ref):
    file_path_list = []
    for root, dirs, files in os.walk(ref):
        for file in files:
            file_path = os.path.join(root, file)
            file_path_list.append(file_path)
    return file_path_list


def is_exist(file):
    if os.path.isfile(file):
        if os.path.getsize(file) > 0:
            flag = 1
        else:
            flag = 0

    elif os.path.isdir(file):
        files = get_files(file)
        if files==[]:
            flag=0
        else:
            flag = 1
            for i in files:
                if os.path.getsize(i) > 0:
                    continue
                else:
                    flag = 0
                    break
    else:
        flag=0

    return flag


def get_absolute(path):
    if path == None:
        return None
    else:
        if os.path.isabs(path):
            return path
        else:
            path = os.path.abspath(path)
            return path

def get_basename(file):
    extension = (".fasta", ".fas", ".fa", ".fna", ".ffn", ".frn", ".faa", ".fna")
    if is_exist(file):
        basename=os.path.basename(file)
        stem, suffix = os.path.splitext(basename)
        if suffix:
            if suffix.lower() in extension:
                basename=stem
        else:
            basename=basename
        return  basename


'''
获得序列
structure:  [{gene1:seq1},{gene2:seq2}]
'''
def get_seq(fasta_file, max_seq_number=100, seq_count_limit=False):
    my_list = []
    seq_number = 0
    for rec in SeqIO.parse(fasta_file, "fasta"):
        name = rec.name
        seq = str(rec.seq)
        temp = {name: seq}
        my_list.append(temp)
        if seq_count_limit and max_seq_number:
            if seq_number >= max_seq_number:
                break
    return my_list

def get_seq_from_name(file,name_list):
    my_list = []
    for rec in SeqIO.parse(file, "fasta"):
        name = rec.name
        if name in name_list:
            seq = str(rec.seq)
            temp = {name: seq}
            my_list.append(temp)
            name_list.remove(name)
        if name_list==[]:
            break
    return my_list #[{gene:seq}]

def My_Log_Recorder(message,keep_quiet=True,path="",stage="",printout_flag=True,stored_flag=False,make_a_newline=True,use_cutting_line=False):
    '''
    :param message: 需要打印/记录的信息
    :param keep_quiet: 静默
    :param path:  log路径
    :param stage:  当前阶段（注释信息）
    :param printout_flag: 是否打印
    :param stored_flag:  是否保存记录
    :param make_a_newline:  是否换行
    :param use_cutting_line:  使用函数，打印一些标志性的东西
    :return:
    '''

    if keep_quiet==True :
        return 0
    if printout_flag==True:
        if make_a_newline==True:
            print(message,flush=True)
        else:
            print(message,flush=True,end='\r')
    if stored_flag==True and path:
        my_time=time.localtime()
        time_header=str(my_time.tm_year)+"-"+str(my_time.tm_mon)+"-"+str(my_time.tm_mday)+"-"+str(my_time.tm_hour)+"-"+str(my_time.tm_min)+"-"+str(my_time.tm_sec)
        stored_message=time_header+" "+stage+":"+message+"\n"
        with open(path,"a") as f:
            f.write(stored_message)
    if use_cutting_line:
        cutting_line(message)


#分割线 文字内容不得大于分割线
def cutting_line(message=""):
    element = ["="]
    cutting_line_number = 60
    element_all = element * cutting_line_number
    length = len(message)
    start = int((cutting_line_number - length) / 2)

    for i in range(len(message)):
        element_all[i + start] = message[i]
    element_all = "".join(element_all)
    print(element_all)
    return element_all


def get_taxonomic_category(order, family, genus, species):
    temp = [order, family, genus, species]
    temp=[i for i in temp if i]
    taxonomic_category=""
    if len(temp)<1:
        print("Please specify a taxonomic category")
        sys.exit()
    elif len(temp)>=2:
        print("Specify up to one  taxonomic category")
    else:
        taxonomic_category = temp[0]
    return  taxonomic_category


'''
解析依赖文件，制作为dict
'''
def parse_dataset_csv(dependency,order,family,genus,species):
    my_dict=defaultdict(list)

    with open(dependency, "r") as f:
        reader=csv.DictReader(f)
        for i in reader:
            try:
                order_name,family_name,genus_name,species_name,fasta_url=i["Order"].replace(" ","_"),i["Family"].replace(" ","_"),i["Genus"].replace(" ","_"),i["Species"].replace(" ","_") ,i["Fasta file url"]
            except:
                continue

            if order:
                if order_name not in my_dict:
                    my_dict[order_name]=[(fasta_url,species_name)]
                else:
                    my_dict[order_name].append((fasta_url,species_name))
            elif family:
                if family_name not in my_dict:
                    my_dict[family_name]=[(fasta_url,species_name)]
                else:
                    my_dict[family_name].append((fasta_url,species_name))
            elif genus:
                if genus_name not in my_dict:
                    my_dict[genus_name]=[(fasta_url,species_name)]
                else:
                    my_dict[genus_name].append((fasta_url,species_name))
            elif species:
                if species_name not in my_dict:
                    my_dict[species_name] = [(fasta_url,species_name)]
                else:
                    my_dict[species_name].append((fasta_url,species_name))
            else:
                pass
    # print(my_dict)  {"order":[ (url1,species_name1),(url2,species_name2) ...   ]}
    return  my_dict



'''
下载指定要求的fasta文件
exclude 需要排除的种
taxonomic_category：目标分类
'''
def get_specified_fasta_file(my_dict,exclude,target,out_dir):
    specified_fasta_file = []
    if target in my_dict:
        files=my_dict[target]
    else:
        print("Please check the -order/-famlily/-genus/-species parameters,failed to find a qualified reference sequence in the dependency file")
        sys.exit()

    if exclude:
        for i in files:
            if i[1] not in exclude:
                specified_fasta_file.append(i)
    else:
        specified_fasta_file=files


    ##将拟下载的数据写进csv表格
    if specified_fasta_file:
        csv_path=os.path.join(out_dir,"download.csv")
        species_name_list=[i[1] for i in specified_fasta_file]

        with open(dependency, "r") as f1,open(csv_path,"a",newline="") as f2:
            reader = csv.DictReader(f1)
            writer= csv.DictWriter(f2,fieldnames=reader.fieldnames)
            writer.writeheader()
            for i in reader:
                if i["Species"].replace(" ","_") in species_name_list:
                    writer.writerow(i)
    print(len(specified_fasta_file))
    return specified_fasta_file


def download_reference_from_url(url,path,out_dir):
    log_path=os.path.join(out_dir,"log.txt")

    socket.setdefaulttimeout(60)
    try:
        # my_url = urllib.request.urlopen(url)
        urlretrieve(url,path)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(url, path)
                break
            # except socket.timeout:
            except:
                err_info = "Reloading for {} time, url:{}".format(count,url)
                My_Log_Recorder(message=err_info,keep_quiet=False,path=log_path,stored_flag=True,printout_flag=False,make_a_newline=False,use_cutting_line=False)
                count += 1
        if count > 5:
            err_info="Downloading {} fialed!".format(url)
            My_Log_Recorder(message=err_info, keep_quiet=False, path=log_path, stored_flag=True, printout_flag=False,
                            make_a_newline=False, use_cutting_line=False)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            err_info = "{}:404".format(url) # 404
            My_Log_Recorder(message=err_info, keep_quiet=False, path=log_path, stored_flag=True, printout_flag=False,
                            make_a_newline=False, use_cutting_line=False)
        else:
            err_info = "Some is wrong:{}".format(url)
            My_Log_Recorder(message=err_info, keep_quiet=False, path=log_path, stored_flag=True, printout_flag=False,
                            make_a_newline=False, use_cutting_line=False)
    except:
        err_info = "Some is wrong:{}".format(url)
        My_Log_Recorder(message=err_info, keep_quiet=False, path=log_path, stored_flag=True, printout_flag=False,
                        make_a_newline=False, use_cutting_line=False)


    if os.path.isfile(path):
        return get_basename(path)

def download_reference_from_url_parallel(specified_fasta_file,out_dir,thread_number):
    '''
    :param specified_fasta_file:  [(url,species),(url,species)]
    :param out_dir:
    :param thread_number:
    :return:
    '''
    task_pool = []
    results = []
    executor = ProcessPoolExecutor(max_workers=thread_number)

    if not specified_fasta_file:
        return 0
    fasta_file_path=os.path.join(out_dir,"fasta_file")
    gene_file_path=os.path.join(out_dir,"gene_file")
    log_path=os.path.join(out_dir,"log.txt")

    number=1
    whole_number=len(specified_fasta_file)

    repeat_species=[]
    species_list=[]
    message_list=[]


    for i in specified_fasta_file:
        url=i[0]
        name=i[1]
        if name not in species_list:
            species_list.append(name)
        else:
            repeat_species.append(name)
            repeat_number=repeat_species.count(name)
            name=name+"_"+str(repeat_number+1)
            target_path=os.path.join(fasta_file_path,name+".fasta")
            message="Species {} repeated {} times, download to {}".format(i[1],repeat_number+1,target_path)
            message_list.append(message)
        file_path=os.path.join(fasta_file_path,name+".fasta")
        task_pool.append(executor.submit(download_reference_from_url,url,file_path,out_dir))
    if message_list:
        for i in message_list:
            My_Log_Recorder(message=i, keep_quiet=False, path=log_path, stored_flag=True,printout_flag=True,
                            make_a_newline=True,
                            use_cutting_line=False)

    for i in task_pool:
        if number < whole_number:
            print("Downloading:{}/{}".format(number, whole_number), end="\r")
        else:
            print("Downloading:{}/{}".format(number, whole_number))
        number+=1
        results.append(i.result())

    if len(get_file_list(fasta_file_path))>0:
        parse_fasta2gene_for_geneminer(fasta_file_path,gene_file_path) #fasta文件转为 一基因一文件形式
        parse_fasta2gene_for_hybpiper(fasta_file_path,out_dir)        #合并所有353基因  name‘s format: taxon-gene


def parse_fasta2gene_for_geneminer(input_dir,out_dir):
    files=get_file_list(input_dir)
    my_record_dict=defaultdict(list)
    for i in files:
        species_name=get_basename(i)
        for rec in SeqIO.parse(i,"fasta"):
            name=rec.name
            identifier=name+"_"+species_name
            description=rec.description.replace(" ","_")
            seq=rec.seq
            record=SeqRecord(id=identifier,seq=seq,description=description)

            if name not in my_record_dict:
                my_record_dict[name]=[record]
            else:
                my_record_dict[name].append(record)
    if my_record_dict:
        if not os.path.isdir(out_dir):
            os.makedirs(out_dir)
        for key,value in my_record_dict.items():
            path=os.path.join(out_dir,key+".fasta")
            record=value
            SeqIO.write(record,path,"fasta")

def parse_fasta2gene_for_hybpiper(input_dir,out_dir):
    files = get_file_list(input_dir)
    my_record_dict = defaultdict(list)
    for i in files:
        species_name = get_basename(i)
        for rec in SeqIO.parse(i, "fasta"):
            name = rec.name
            identifier = species_name + "-" + name   # taxon-genename
            description = ""
            seq = rec.seq
            record = SeqRecord(id=identifier, seq=seq, description=description)

            if name not in my_record_dict:
                my_record_dict[name] = [record]
            else:
                my_record_dict[name].append(record)

    hybpiper_records=[]
    if my_record_dict:
        for key, value in my_record_dict.items():
            for record in value:
                hybpiper_records.append(record)

        path=os.path.join(out_dir,"ref_hybpiper.fasta")
        SeqIO.write(hybpiper_records,path,"fasta")



def workflow_main(configuration):
    out_dir=configuration["out_dir"]
    thread_number=configuration["thread_number"]
    dependency=configuration["dependency"]
    order=configuration["order"]
    family=configuration["family"]
    genus=configuration["genus"]
    species=configuration["species"]
    exclude=configuration["exclude"]

    t1=time.time()
    fasta_file_path=os.path.join(out_dir,"fasta_file")
    gene_file_path=os.path.join(out_dir,"gene_file")
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    if not os.path.isdir(fasta_file_path):
        os.makedirs(fasta_file_path)
    if not os.path.isdir(gene_file_path):
        os.makedirs(gene_file_path)
    target=get_taxonomic_category(order,family,genus,species)
    my_dict= parse_dataset_csv(dependency, order, family, genus, species)
    specified_fasta_file=get_specified_fasta_file(my_dict,exclude,target,out_dir)
    download_reference_from_url_parallel(specified_fasta_file, out_dir, thread_number)
    t2=time.time()
    message="Time used:{}s".format(round(t2-t1,4))
    print(message)


if __name__ == '__main__':
    t1 = time.time()
    # -i -r 中的文件名必须是xx.fasta 同名 muslce3 必须写在路径中
    #eg. python download_reference.py -d example/specimens.csv -o example/ref_Apiaceae -family Apiaceae -exclude Chamaesium_paradoxum -t 4
    #eg.  python download_reference.py -d requirement.csv -o example/ref_Brassicaceae_353  -family Brassicaceae -exclude Arabidopsis_thaliana  -t 4
    pars = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="reports",
                                   usage="%(prog)s <-i> <-o> [options]")

    pars.add_argument("-o", "--out", dest="out_dir", help="Specify the result folder <dir>",
                      metavar="", required=True)
    pars.add_argument("-t", "--thread", metavar="", dest="thread_number", help="Thread", type=int, default=1)
    pars.add_argument("-d", "--dependency", metavar="", dest="dependency", help="Path of the dependency file(requirement.csv)", type=str,default="requirement.csv")
    pars.add_argument("-order", metavar="", dest="order", help="order", type=str)
    pars.add_argument("-family", metavar="", dest="family", help="family", type=str)
    pars.add_argument("-genus", metavar="", dest="genus", help="genus", type=str)
    pars.add_argument("-species", metavar="", dest="species", help="species", type=str)
    pars.add_argument("-exclude", metavar="", dest="exclude", help="exclude",nargs="*")  # *(>=0) ?(0,1) +(>=1)


    args = pars.parse_args()
    out_dir=get_absolute(args.out_dir)
    thread_number=args.thread_number
    dependency=get_absolute(args.dependency)
    order=args.order
    family=args.family
    genus=args.genus
    species=args.species
    exclude=args.exclude

    configuration={"out_dir":out_dir,"thread_number":thread_number,"dependency":dependency, "order":order, "family":family, "genus":genus, "species":species, "exclude":exclude}

    workflow_main(configuration)











