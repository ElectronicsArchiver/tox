from pathlib import Path
from Bio import SeqIO
import sys
import subprocess

def main():
    if 'test' in sys.argv:
        run_test()
    elif 'train' in sys.argv:
        run_train()
    else:
        print("Please specify test or train.")

def run_test():
    print("Running test directories...")
    test_dir = Path('test-chunks')
    test_files = check_dirs_test(test_dir)
    print(f"Test files remaining: {len(test_files)} ...")
    for file in test_files:
        outdir = Path(f"test-embeds/{file.stem}")
        print(f"Running {file.name} ...")
        outdir.mkdir(exist_ok=True)
        pipe = subprocess.Popen(f"python extract.py esm1b_t33_650M_UR50S {file} {outdir} --include mean".split())
        pipe.wait()

def run_train():
    print("Running train directories...")
    train_dir = Path('train-chunks')
    train_files = check_dirs_train(train_dir)
    print(f"Train files remaining: {len(train_files)} ...")
    for file in train_files:
        outdir = Path(f"train-embeds/{file.stem}")
        print(f"Running {file.name} ...")
        outdir.mkdir(exist_ok=True)
        pipe = subprocess.Popen(f"python extract.py esm1b_t33_650M_UR50S {file} {outdir} --include mean".split())
        pipe.wait()

def check_dirs_train(dir):
    files = [x for x in dir.iterdir() if x.is_file() and x.suffix == '.fasta']
    output_dirs = [Path(f"train-embeds/{x.stem}") for x in files]
    filtered_files = []
    for i, file in enumerate(files):
        if not output_dirs[i].is_dir():
            filtered_files.append(file)
        else:
            file_seqs = list(SeqIO.parse(file, 'fasta'))
            if len(file_seqs) != len(list(output_dirs[i].iterdir())):
                filtered_files.append(file)
                output_dirs_files = [x for x in output_dirs[i].iterdir()]
                for x in output_dirs_files:
                    x.unlink()
                output_dirs[i].rmdir()
    return filtered_files
        
def check_dirs_test(dir):
    files = [x for x in dir.iterdir() if x.is_file() and x.suffix == '.fasta']
    output_dirs = [Path(f"test-embeds/{x.stem}") for x in files]
    filtered_files = []
    for i, file in enumerate(files):
        if not output_dirs[i].is_dir():
            filtered_files.append(file)
        else:
            file_seqs = list(SeqIO.parse(file, 'fasta'))
            if len(file_seqs) != len(list(output_dirs[i].iterdir())):
                filtered_files.append(file)
                output_dirs_files = [x for x in output_dirs[i].iterdir()]
                for x in output_dirs_files:
                    x.unlink()
                output_dirs[i].rmdir()
    return filtered_files

if __name__ == "__main__":
    main()
