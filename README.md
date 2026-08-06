# FASTQ Quality Assessment & Filtering 🧬

A lightweight Python tool for FASTQ quality assessment and read filtering in next-generation sequencing (NGS) workflows.

---

## 🧬 Project Overview & Biological Context

Raw sequencing reads can contain low-quality bases, short reads, and ambiguous nucleotide calls that may affect downstream bioinformatics analyses.

**FASTQ Quality Assessment & Filtering** provides a simple preprocessing workflow to assess sequencing quality and filter reads based on predefined quality criteria.

The pipeline:

1. Parses FASTQ sequencing records.
2. Calculates initial quality metrics.
3. Evaluates individual reads against predefined quality thresholds.
4. Filters reads that do not meet the required criteria.
5. Writes retained reads to a compressed FASTQ output file.

---

## ⚙️ Pipeline Architecture

The workflow is organized into modular processing steps:

```
 Raw FASTQ File
        │
        ▼
 FASTQ Record Parsing
        │
        ▼
 Quality Metrics Calculation
        │
        ▼
 Read-Level Quality Filtering
        │
        ├── Mean Phred Quality ≥ 20.0
        ├── Read Length ≥ 50 bp
        └── N Content ≤ 5.0%
        │
        ▼
 Filtered FASTQ Output
```

### Processing Steps

* **FASTQ Parsing:** Reads sequencing records and extracts sequence and quality information.
* **Quality Assessment:** Calculates summary metrics including total reads, total bases, mean read length, GC content, N content, and mean Phred quality.
* **Read-Level Filtering:** Evaluates individual reads according to predefined quality thresholds.
* **Quality Filtering:** Excludes reads with a mean Phred quality below the required threshold.
* **Length Filtering:** Excludes reads shorter than the minimum required length.
* **Ambiguous Base Filtering:** Excludes reads exceeding the maximum allowed percentage of ambiguous `N` bases.
* **Output Generation:** Writes retained reads to a compressed FASTQ file.

---

## 🔬 Bioinformatics Applications

Quality-filtered FASTQ reads can be used as input for downstream NGS workflows, including:

* Sequence alignment and mapping.
* Genome assembly.
* Variant calling.
* Microbial genomics.
* Viral genome analysis.
* Comparative sequence analysis.

The tool is intended as an early preprocessing component within larger bioinformatics workflows.

---

## 🚀 Getting Started

### Prerequisites

* Python 3
* Biopython

### Installation

1. Clone the repository:

   `git clone https://github.com/dariolobo/fastq-quality-filter.git`

   `cd fastq-quality-filter`

2. Install the required dependency:

   `pip install biopython`

---

## 💻 Usage

The workflow is executed through `main.py` using the sample FASTQ dataset included in the repository.

Run the tool from the project root:

```
 python main.py
```

The default workflow reads:

```
 data/sample.fastq
```

and generates:

```
 data/sample_filtered.fastq.gz
```

### Filtering Criteria

Each read is evaluated using the following thresholds:

* **Mean Phred quality:** ≥ 20.0
* **Minimum read length:** ≥ 50 bp
* **Maximum N content:** ≤ 5.0%

A read must satisfy all three criteria to be retained in the output dataset.

---

## 📊 Sample Output

A typical execution reports the input file, initial FASTQ metrics, and output location:

```
 Processing input file data/sample.fastq...
 Initial Metrics: {...}
 Filtering complete! Clean file saved to: data/sample_filtered.fastq.gz
```

The reported metrics depend on the input FASTQ dataset.

---

## 📁 Project Structure

```
 fastq-quality-filter/
 │
 ├── data/
 │   ├── sample.fastq
 │   └── sample_filtered.fastq.gz
 │
 ├── src/
 │   ├── filter.py
 │   ├── metrics.py
 │   ├── parser.py
 │   └── writer.py
 │
 ├── main.py
 ├── .gitignore
 └── README.md
```

### Core Components

* `main.py`: Coordinates the FASTQ quality assessment and filtering workflow.
* `src/parser.py`: Parses FASTQ records and extracts sequence and quality information.
* `src/metrics.py`: Calculates summary FASTQ quality metrics.
* `src/filter.py`: Applies read-level quality, length, and ambiguous-base filtering criteria.
* `src/writer.py`: Writes retained FASTQ records to the output file.

---

## 🛠️ Built With

* **Python 3** — Core programming language.
* **Biopython** — FASTQ parsing and sequence-quality handling.
* **Phred quality scores** — Used for sequencing read quality assessment.
* **Gzip** — Used for compressed FASTQ output.

---

## 📌 Workflow Position

This tool can be used as an early preprocessing step in an NGS workflow:

```
 Raw FASTQ Data
        │
        ▼
 Quality Assessment & Filtering
        │
        ▼
 Quality-Filtered Reads
        │
        ├──────────────► Alignment
        │
        ├──────────────► Genome Assembly
        │
        └──────────────► Variant Analysis
```
