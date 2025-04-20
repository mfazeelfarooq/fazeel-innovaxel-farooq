from datetime import datetime
from bson import ObjectId

class URL:
    def __init__(self, original_url, short_code, created_at=None, _id=None, clicks=0, last_clicked=None):
        self._id = _id or ObjectId()
        self.original_url = original_url
        self.short_code = short_code
        self.created_at = created_at or datetime.utcnow()
        self.clicks = clicks
        self.last_clicked = last_clicked

    def to_dict(self):
        return {
            '_id': str(self._id),
            'original_url': self.original_url,
            'short_code': self.short_code,
            'created_at': self.created_at,
            'clicks': self.clicks,
            'last_clicked': self.last_clicked
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            original_url=data['original_url'],
            short_code=data['short_code'],
            created_at=data.get('created_at'),
            _id=ObjectId(data['_id']) if '_id' in data else None,
            clicks=data.get('clicks', 0),
            last_clicked=data.get('last_clicked')
        )
