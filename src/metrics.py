# src/metrics.py
from typing import List, Dict
from src.parser import FastqRecord


def calculate_gc_content(sequence: str) -> float:
    """Calculate the GC content percentage of a DNA sequence."""
    if not sequence:
        return 0.0
    gc_count = sum(1 for base in sequence.upper() if base in ('G','C'))
    return (gc_count / len(sequence)) * 100


def calculate_mean_quality(qualities: List[int]) -> float:
    """Calculate the average Phred quality score for a list of quality values."""
    if not qualities:
        return 0.0
    return sum(qualities) / len(qualities)


def calculate_n_content(sequence: str) -> float:
    """Calculate the percentage of ambiguous bases ('N') in a sequence."""
    if not sequence:
        return 0.0
    n_count = sequence.upper().count('N')
    return (n_count / len(sequence)) * 100

def summarize_fastq_metrics(records) -> Dict[str, float]:
    """
    Compute aggregate metrics across all FastqRecord objects.
    Note: 'records' is expected to be an iterable/generator of FasqRecord.
    """
    total_reads = 0
    total_bases = 0
    total_gc_bases = 0
    total_n_bases = 0
    sum_quality_scores = 0

    for record in records:
        total_reads += 1
        seq_len = record.length
        total_bases += seq_len

        # Accumulate GC and N counts
        total_gc_bases += sum(1 for base in record.sequence.upper() if base in ('G','C'))
        total_n_bases += record.sequence.upper().count('N')

        # Accumulate Phred sum_quality_scores
        sum_quality_scores += sum(record.qualities)

    if total_reads == 0 or total_bases == 0:
        return {
            "total_reads": 0,
            "total_bases": 0,
            "mean_read_length": 0.0,
            "gc_content_pct": 0.0,
            "n_content_pct": 0.0,
            "mean_phred_score": 0.0
        }

    return {
        "total_reads": total_reads,
        "total_bases": total_bases,
        "mean_read_length": total_bases / total_reads,
        "gc_content_pct": (total_gc_bases / total_bases) * 100,
        "n_content_pct": (total_n_bases / total_bases) * 100,
        "mean_phred_score": sum_quality_scores / total_bases
    }