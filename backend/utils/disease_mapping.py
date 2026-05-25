# utils/disease_mapping.py

disease_mapping = {
    "scabies": "Scabies/Mange",
    "ringworm": "Ringworm"
}


def normalize_species(species: str) -> str:
    if not species:
        return ""

    species = species.lower().strip()

    mapping = {
        "anjing": "dog",
        "dog": "dog",
        "kucing": "cat",
        "cat": "cat"
    }

    return mapping.get(species, species)


def map_disease_label(model_label: str, species: str) -> str:
    if not model_label:
        return "Unknown"

    model_label = model_label.lower().strip()

    return disease_mapping.get(model_label, model_label)