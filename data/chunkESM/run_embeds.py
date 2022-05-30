from pathlib import Path
from multiprocessing import Pool
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

def run_command(batch):
    for file in batch:
        outdir = Path(f"test-embeds/{file.stem}")
        print(f"Running {file.name} ...")
        outdir.mkdir(exist_ok=True)
        pipe = subprocess.Popen(f"python extract.py esm1b_t33_650M_UR50S {file} {outdir} --include mean".split())
        pipe.wait()

def run_test():
    print("Running test directories...")
    test_dir = Path('test-chunks')
    test_files = check_dirs(test_dir)
    print(f"Test files remaining: {len(test_files)} ...")
    batch_size = 5
    batches = []
    for i in range(0, len(test_files), batch_size):
        batches.append(test_files[i : i + batch_size])
    processes = 6
    with Pool(processes) as p:
        p.map(run_command, batches)

def run_train():
    train_dir = Path('train-chunks')
    train_files = check_dirs(train_dir)

def check_dirs(dir):
    files = [x for x in dir.iterdir() if x.is_file() and x.suffix == '.fasta']
    output_dirs = [Path(f"test-embeds/{x.stem}") for x in files]
    filtered_files = []
    for i, file in enumerate(files):
        if not output_dirs[i].is_dir():
            filtered_files.append(file)
        else:
            file_seqs = list(SeqIO(file, 'fasta'))
            if len(file_seqs) != len(list(output_dirs[i].iterdir())):
                filtered_files.append(file)
                output_dirs_files = [x for x in output_dirs[i].iterdir()]
                for x in output_dirs_files:
                    x.unlink()
                output_dirs[i].rmdir()
    return filtered_files

if __name__ == "__main__":
    main()