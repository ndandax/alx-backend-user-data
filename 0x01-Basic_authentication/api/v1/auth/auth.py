#!/usr/bin/env python3
"""
class app
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication func"""
        if path is None:
            return True
        if excluded_paths is None or not excluded_paths:
            return True
        if path in excluded_paths:
            return False
        if not path.endswith('/'):
            path += '/'
        for i in excluded_paths:
            if path.startswith(i):
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        value = request.headers.get('Authorization')
        return value

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user"""
        return None
