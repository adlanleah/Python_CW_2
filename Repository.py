import json
import os


class Repo:
    FIELDS = ("name", "email", "phone")

    def __init__(self, path: str = "mydb.txt"):
        self.path = path
        if not os.path.exists(path):
            open(self.path, "w").close()

    def create(self, obj):
        data = obj.to_dict() if hasattr(obj, "to_dict") else obj.__dict__
        with open(self.path, "a") as db:
            db.write(json.dumps(data) + "\n")

    def read(self) -> list:
        records = []
        with open(self.path, "r") as db:
            for line in db:
                line = line.strip()
                if line:
                    records.append(json.loads(line))
        return records

    def search(self, value: str) -> list:
        value = value.strip().lower()
        results = []
        for record in self.read():
            if any(value in str(record.get(field, "")).lower() for field in self.FIELDS):
                results.append(record)
        return results

    def delete(self, key: str, value) -> int:
        records = self.read()
        kept = [r for r in records if r.get(key) != value]
        removed = len(records) - len(kept)
        with open(self.path, "w") as db:
            for record in kept:
                db.write(json.dumps(record) + "\n")
        return removed
