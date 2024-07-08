
km_files_mappings = {
    "properties": {
        "agent_type": {
            "type": "keyword"
        },
        "km_id": {
            "type": "keyword"
        },
        "file_id": {
            "type": "keyword"
        },
        "file_name": {
            "type": "keyword"
        },
        "file_url": {
            "type": "keyword"
        },
        "created_at": {
            "type": "date"
        },
        "document_type": {
            "type": "keyword"
        },
        "document_index": {
            "type": "short"
        },
        "document_tags": {
            "type": "text",
            "analyzer": "ik_max_word",
            "index": "true"
        },
        "document_tags_format": {
            "type": "text",
            "analyzer": "ik_max_word",
            "index": "true"
        },
        "document_tags_format_embedding": {
            "type": "dense_vector",
            "dims": 768,
            "index": "true",
            "similarity": "l2_norm"
        },
        "document_content": {
            "type": "text",
            "analyzer": "ik_max_word",
            "index": "true"
        },
        "document_content_embedding": {
            "type": "dense_vector",
            "dims": 768,
            "index": "true",
            "similarity": "l2_norm"
        }
    }
}


