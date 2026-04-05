# utils/disease_mapping.py

disease_mapping = {
    "scabies": {
        "cat": "Scabies",
        "dog": "Mange"
    },
    "ringworm": {
        "cat": "Ringworm",
        "dog": "Ringworm"
    }
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
    species = normalize_species(species)

    return disease_mapping.get(model_label, {}).get(species, model_label)
