# src/writer.py
import gzip
from typing import Iterable
from src.parser import FastqRecord


def write_fastq_records(
    output_path: str,
    records: Iterable[FastqRecord]
) -> None:
    """
    Write FastqRecord objects to an output FASTQ file.
    Supports transparent gzip compression if the output_path ends with .gz.
    """

    is_gzipped = output_path.endswith('.gz')
    open_func = gzip.open if is_gzipped else open

    with open_func(output_path, 'wt', encoding='utf-8') as handle:
        for record in records:
            # Reconstruct the 4-line FASTQ format
            handle.write(f"@{record.read_id}\n")
            handle.write(f"{record.sequence}\n")
            handle.write(f"{record.description}\n")
            handle.write(f"{record.quality_str}\n")