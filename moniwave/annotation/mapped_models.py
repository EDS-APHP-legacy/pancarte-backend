from rest_framework.exceptions import server_error

from utils.pancarte_db import http_get, http_post, http_put, http_delete


class MappedObject(object):
    @classmethod
    def get(cls, **where):
        try:
            result = http_get(*cls.path, **where)
        except RuntimeError as e:
            return server_error(None)
        return [cls(**entry) for entry in result]

    @classmethod
    def insert(cls, **params):
        params = {k: params[k] for k in cls.required_fields}
        try:
            result = http_post(*cls.path, **params)
        except RuntimeError as e:
            return server_error(None)
        return cls(**result)

    def update(self):
        params = {k: getattr(self, k) for k in self.required_fields}
        try:
            http_put(*self.path, id=self.id, **params)
        except RuntimeError as e:
            return server_error(None)

    def delete(self):
        try:
            http_delete(*self.path, id=self.id)
        except RuntimeError as e:
            return server_error(None)


class AnnotationType(MappedObject):
    path = ('annotations', 'types',)
    required_fields = ('name',)

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class AnnotationTimestamp(MappedObject):
    path = ('annotations', 'timestamp',)
    required_fields = ('source_id', 'type_id', 'value', 'comment', 'timestamp_micros')

    def __init__(self, id: int, source_id: int, type_id: int, value: float, comment: str, timestamp_micros: int):
        self.id = id
        self.source_id = source_id
        self.type_id = type_id
        self.value = value
        self.comment = comment
        self.timestamp_micros = timestamp_micros


class AnnotationTimerange(MappedObject):
    path = ('annotations', 'timerange',)
    required_fields = ('source_id', 'type_id', 'value', 'comment', 'start_micros', 'end_micros')

    def __init__(self, id: int, source_id: int, type_id: int, value: float, comment: str, start_micros: int, end_micros: int):
        self.id = id
        self.source_id = source_id
        self.type_id = type_id
        self.value = value
        self.comment = comment
        self.start_micros = start_micros
        self.end_micros = end_micros