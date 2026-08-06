# FASTQ Quality Trimmer 🧬

A Python-based tool for the quality control, processing, and filtering of next-generation sequencing (NGS) data in FASTQ format.

## 🚀 Overview and Key Features

This tool cleans and prepares raw sequencing data before proceeding with assembly or alignment tasks. Its features include:

* **Sliding-window trimming:** Evaluates the average base quality across sliding windows along the read, trimming low-quality regions.
* **Phred score analysis:** Accurate parsing of sequence qualities to ensure the retention of biologically reliable data.
* **Minimum length filtering:** Discards reads that fall below a useful length threshold after the trimming process.
* **Ambiguous base control:** Excludes sequences containing a high number of uncalled nucleotides (`N`).

## ⚙️ Pipeline Architecture

The tool processes sequencing data through a streamlined, sequential pipeline:

1. **Data Ingestion:** Reads the raw FASTQ file iteratively (optimizing memory usage) using Biopython.
2. **Quality Assessment:** Applies a sliding window across each sequence to calculate the average Phred quality score.
3. **Trimming:** Trims the ends of the read when the window's average quality drops below the user-defined threshold.
4. **Length Validation:** Discards the trimmed read if its new length is strictly shorter than the minimum specified length.
5. **Ambiguous Base Check:** Filters out sequences exceeding the allowed limit of ambiguous `N` calls.
6. **Output Generation:** Writes the surviving, high-quality sequences into a new FASTQ file ready for downstream analysis.

## 📋 Prerequisites

To run this tool, you need Python 3.8 or higher. The **Biopython** library is highly recommended, as it facilitates the efficient parsing, manipulation, and analysis of biological formats like FASTQ.

## 🛠️ Installation

1. Clone this repository to your local environment:
   `git clone https://github.com/dariolobo/fastq-quality-trimmer.git`
   `cd fastq-quality-trimmer`

2. Install Biopython using pip:
   `pip install biopython`

## 💻 Usage

The project follows a modular design, but execution is centralized through `main.py`. Running this main file automatically initializes and invokes all the necessary filtering, trimming, and validation modules.

Run the tool from your terminal by providing the desired parameters:

`python main.py -i input.fastq -o output.fastq -w 4 -q 20 -l 35`

### Arguments and Parameters:
* `-i` / `--input`: Path to the input raw FASTQ file.
* `-o` / `--output`: Path and filename for the cleaned output FASTQ file.
* `-w` / `--window`: Size of the sliding window to evaluate quality.
* `-q` / `--quality`: Minimum acceptable Phred score within the window.
* `-l` / `--min_length`: Minimum length required to keep a read after trimming.

## 📊 Sample Output

When running the tool, the console will provide a concise summary report of the trimming process:

```text
[INFO] Starting FASTQ Quality Trimmer...
[INFO] Input file: input.fastq
[INFO] Processing reads...

======================================
         TRIMMING SUMMARY
======================================
Total reads processed:      100,000
Reads passing filters:       86,450 (86.45%)
Reads dropped (quality):      9,300 (9.30%)
Reads dropped (length):       3,500 (3.50%)
Reads dropped (N-content):      750 (0.75%)
======================================

[INFO] Clean data saved to: output.fastq
[INFO] Process completed successfully in 12.4 seconds.
```

## 📁 Project Structure

* `main.py`: The main execution script that coordinates the workflow across all modules.

## 🤝 Contributing

If you wish to improve the code or documentation, feel free to fork the repository, open an issue detailing the bug/feature, or submit a pull request.
