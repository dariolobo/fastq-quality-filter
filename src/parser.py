# src/parser.py
import gzip
from dataclasses import dataclass
from typing import Generator, List

@dataclass
class FastqRecord:
    read_id: str
    sequence: str
    description: str
    quality_str: str

    @property
    def qualities(self) -> List[int]:
        """Convert ASCII quality string to a list of Phred+33 integers."""
        return [ord(char) - 33 for char in self.quality_str]

    @property
    def length(self) -> int:
        """Return the length of the biological sequence."""
        return len(self.sequence)


def parse_fastq(file_path: str) -> Generator[FastqRecord, None, None]:
    """
    Yield FastqRecord objects sequentially from a FASTQ file.
    Supports both uncompressed (.fastq) and gzipped (.fastq.gz) files.
    """
    is_gzipped = file_path.endswith('.gz')
    open_func = gzip.open if is_gzipped else open

    with open_func(file_path, 'rt', encoding='utf-8') as handle:
        while True:
            header = handle.readline().strip()
            if not header:
                break  # End of the file

            sequence = handle.readline().strip()
            description = handle.readline().strip()
            quality_str = handle.readline().strip()

            # Basic FASTQ structure validation
            if not header.startswith('@') or not description.startswith('+'):
                raise ValueError(f"Invalid FASTQ record format near line: {header}")

            yield FastqRecord(
                read_id=header[1:],   # Strip leading '@'
                sequence=sequence,
                description=description,
                quality_str=quality_str
            )
