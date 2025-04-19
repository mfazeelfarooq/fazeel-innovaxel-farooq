from datetime import datetime
from bson import ObjectId

class URL:
    def __init__(self, original_url, short_code, created_at=None, _id=None):
        self._id = _id or ObjectId()
        self.original_url = original_url
        self.short_code = short_code
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            '_id': str(self._id),
            'original_url': self.original_url,
            'short_code': self.short_code,
            'created_at': self.created_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            original_url=data['original_url'],
            short_code=data['short_code'],
            created_at=data.get('created_at'),
            _id=ObjectId(data['_id']) if '_id' in data else None
        )
