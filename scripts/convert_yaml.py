import os
import yaml
import re
import random
import argparse
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

def process_text_tc(x):
    x = x[2:]
    x = x.replace("[", "")
    x = x.replace("]", "")
    return re.sub("[\(\[].*?[\)\]]", "", x)

def read_yaml(yamlFile, taskName):
    with open(yamlFile, "r") as f:
        data = yaml.safe_load(f)
    return data[taskName]

def convert_yaml(dataDir, yamlFileList, resTrainPath, resValPath, labelPath, trainRatio, shuffleData):

    open(resTrainPath, "w").close()
    open(resValPath, "w").close()
    open(labelPath, "w").close()

    data = []
    for yamlFile in yamlFileList:
        yamlFilePath = os.path.join(dataDir, yamlFile, "nlu.yml")
        data += read_yaml(yamlFilePath, 'nlu')

    with open(resTrainPath, "a") as train_f:
        with open(resValPath, "a") as val_f:
            with open(labelPath, "a") as label_f:
                trainData, valData, labels = [], [], []
                for intentIdx in range(len(data)):
                    labels.append(data[intentIdx]["intent"])
                    examples = data[intentIdx]['examples'].split("\n")
                    examplesNoDash = list(map(process_text_tc, examples))[:-1]
                    numTrainData = int(len(examplesNoDash) * trainRatio)
                    for expIdx in range(len(examplesNoDash)):
                        line = examplesNoDash[expIdx] + '\t' + str(intentIdx)
                        if expIdx < numTrainData:
                            trainData.append(line)
                        else:
                            valData.append(line)
                if shuffleData:
                    random.shuffle(trainData)
                    random.shuffle(valData)
                label_f.write("\n".join(labels))
                train_f.write("\n".join(trainData))
                val_f.write("\n".join(valData))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--dd", "--data_dir", help="path to data dir", type=str)
    parser.add_argument("--yf", "--yaml_file", nargs='+', help="path to yaml file", required=True)
    parser.add_argument("--tm", "--train_manifest", help="result train manifest", type=str)
    parser.add_argument("--vm", "--val_manifest", help="result val manifest", type=str)
    parser.add_argument("--lb", "--label_file", help="label file", type=str)
    parser.add_argument("--tr", "--train_ratio", help="train manifest ratio", type=float)
    parser.add_argument("--shuffle", help="shuffle data", action="store_true")

    args = parser.parse_args()

    if not args.dd:
        print("no data dir is specified. set current folder as default.")
        args.dd = os.getcwd()

    if not args.yf:
        print("you must provide at least 1 yaml file to use this script.")
        exit()

    if not args.tm:
        args.tm = "train.tsv"

    if not args.vm:
        args.vm = "val.tsv"

    if not args.lb:
        args.lb = 'labels.csv'

    if not args.tr:
        args.tr = 0.8

    if not args.shuffle:
        args.shuffle = False

    convert_yaml(args.dd, args.yf, args.tm, args.vm, args.lb, args.tr, args.shuffle)
