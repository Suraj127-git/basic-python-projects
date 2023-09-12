def NoteEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "note": str(item["note"])
    }


def NotesEntity(items) -> list:
    return [NoteEntity(items) for item in items]