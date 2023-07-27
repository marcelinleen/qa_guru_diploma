import hashlib


def get_sign(data, api_secret):
    object_keys = []
    signed_signature = ""
    signed_object = {}

    for k, v in data.items():
        object_keys.append(k)

    object_keys.sort()

    for key in object_keys:
        signed_signature = signed_signature + key + data[key]
        signed_object[key] = data[key]

    signed_signature += api_secret

    escaped_signature = signed_signature.encode('utf-8')
    api_sign = hashlib.md5(escaped_signature).hexdigest()

    return api_sign
