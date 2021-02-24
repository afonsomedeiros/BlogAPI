from peewee import Model, ModelSelect

def transfer(json: dict, model: Model, obj = None):
    if not obj:
        obj = model()
    for key, value in json.items():
        if hasattr(obj, key):
            setattr(obj, key, value)
    return obj

def get_info(data: ModelSelect, page, per_page):
    total_pages = data.count() / per_page
    total_pages_rounded = round(data.count() / per_page)
    if total_pages_rounded < total_pages:
        total_pages += 1
    obj = data.paginate(page, per_page)
    return obj, {
        "page": page,
        "per_page": obj.count(),
        "total": data.count(),
        "total_pages": total_pages_rounded if total_pages_rounded > 0 else 1,
    }