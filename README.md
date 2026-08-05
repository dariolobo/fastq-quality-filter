# 🧬 FASTQ Quality Trimmer

A lightweight, pure-Python command-line tool designed to parse, evaluate quality metrics, and filter high-throughput sequencing data in FASTQ format (supporting both raw `.fastq` and compressed `.fastq.gz` input/output).

---

## 📌 Table of Contents
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Prerequisites & Installation](#-prerequisites--installation)
- [Usage](#-usage)
- [Pipeline Architecture](#-pipeline-architecture)
- [Sample Output](#-sample-output)

---

## ✨ Features
* ⚙️ **Format Flexibility:** Seamlessly handles uncompressed (`.fastq`) and Gzip-compressed (`.fastq.gz`) sequence files.
* 🎯 **Custom Quality Thresholds:** Filters reads based on:
  * Minimum average Phred quality score (`min_mean_q`).
  * Minimum sequence length (`min_length`).
  * Maximum allowable percentage of ambiguous bases (`max_n_pct`).
* 📊 **Comprehensive Summary Metrics:** Calculates key sequencing metrics (total reads, total base count, mean read length, GC content percentage, N content percentage, and mean Phred score).
* ⚡ **Zero External Dependencies:** Built entirely with standard Python libraries.

---

## 📁 Project Structure

```text
FASTQ_Quality_Trimmer/
├── data/
│   ├── sample.fastq
│   └── sample_filtered.fastq.gz
├── src/
│   ├── filter.py
│   ├── metrics.py
│   ├── parser.py
│   └── writer.py
├── main.py
└── README.md

🚀 Prerequisites & Installation
Requirements

    🐍 Python 3.10+ (No third-party packages required).

    Setup Instructions

    1. Clone the repository:

    git clone [https://github.com/dariolobo/FASTQ_Quality_Trimmer.git](https://github.com/dariolobo/FASTQ_Quality_Trimmer.git)
    cd FASTQ_Quality_Trimmer

    2. Activate Virtual Environment (Optional but Recommended):
    source ~/bio_env/bin/activate


💻 Usage

Place your input file inside the data/ directory (or update the path in main.py) and run:

python3 main.py


🔄 Pipeline Architecture

    Parse: Reads input FASTQ records sequentially.

    Analyze: Computes and prints baseline metrics of the raw dataset.

    Filter: Evaluates each record against user-defined quality thresholds.

    Export: Writes pass-filter records to a Gzip-compressed FASTQ file (.fastq.gz).


📄 Sample Output

Processing input file data/sample.fastq...
Initial Metrics: {'total_reads': 1000, 'total_bases': 150000, 'mean_read_length': 150.0, 'gc_content_pct': 48.2, 'n_content_pct': 0.05, 'mean_phred_score': 34.1}
Filtering complete! Clean file saved to: data/sample_filtered.fastq.gz