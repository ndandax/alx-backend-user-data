#!/usr/bin/env python3
"""encrypt password"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function which do encryption"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """checking password"""
    try:
        return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
    except ValueError:
        return False
