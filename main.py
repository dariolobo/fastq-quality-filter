# main.py
import sys
from src.parser import parse_fastq
from src.metrics import summarize_fastq_metrics
from src.filter import filter_fastq_records
from src.writer import write_fastq_records


def main():
    # Define input and output file paths
    input_file = "data/sample.fastq"
    output_file = "data/sample_filtered.fastq.gz"

    print(f"Processing input file {input_file}...")

    # 1. Parse raw records into a list to allow multiple passes
    raw_records = list(parse_fastq(input_file))

    # 2. Calculate and display initial metrics (uses Line 4 import)
    initial_metrics = summarize_fastq_metrics(raw_records)
    print(f"Initial Metrics: {initial_metrics}")

    # 3. Filter records based on quality criteria
    filtered_records = filter_fastq_records(
        raw_records,
        min_mean_q=20.0,
        min_length=50,
        max_n_pct=5.0
    )

    # 4. Write filtered records to destination
    write_fastq_records(output_file, filtered_records)

    print(f"Filtering complete! Clean file saved to: {output_file}")


if __name__ == "__main__":
    main()
