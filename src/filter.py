# src/filter.py
from collections.abc import Generator
from src.parser import FastqRecord
from src.metrics import calculate_mean_quality, calculate_n_content

def is_high_quality_read(
    record: FastqRecord,
    min_mean_q: float = 20.0, 
    min_length: int = 50,
    max_n_pct: float = 5.0
) -> bool:
    """
    Evaluate if a FastqRecord meets the quality thresholds.
    Returns True if the record passes all filters, False otherwise.
    """

    # 1. Check minimum read length
    if record.length < min_length:
        return False

    # 2. Check maximum percentage of ambiguous N bases
    n_pct = calculate_n_content(record.sequence)
    if n_pct > max_n_pct:
        return False

    # 3. Check average Phred quality score
    mean_q = calculate_mean_quality(record.qualities)
    if mean_q < min_mean_q:
        return False

    return True

def filter_fastq_records(
    records,
    min_mean_q: float = 20.0,
    min_length: int = 50,
    max_n_pct: float = 5.0
) -> Generator[FastqRecord, None, None]:
    """
    Yield only the FastqRecord objects that pass quality thresholds.
    """
    for record in records:
        if is_high_quality_read(
            record,
            min_mean_q=min_mean_q,
            min_length=min_length,
            max_n_pct=max_n_pct
        ):
            yield record
