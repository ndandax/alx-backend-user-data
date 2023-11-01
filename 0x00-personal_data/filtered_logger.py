#!/usr/bin/env python3
"""filtering data"""
import re
from typing import List


def filter_datum(
    fields: List[str],
    redaction: str,
    message: str,
    separator: str
) -> str:
    pattern = rf'(?<={separator}|=)({"|".join(fields)})[^{separator}]+'
    return re.sub(pattern, '=' + redaction, message)
