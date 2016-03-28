from hashids import Hashids


def get_encoded_hash_id(instance):
    hashids = Hashids(salt=instance._meta.model_name, min_length=4)
    return hashids.encode(instance.id)
