def remove_duplicates(data_list):
    """Removes duplicate elements from a list while preserving order."""
    seen = set()
    result = []
    for item in data_list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

def strip_whitespaces(string_list):
    """Strips leading and trailing whitespaces from strings in a list."""
    return [s.strip() for s in string_list]
