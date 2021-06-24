RANDOM_STATE = 2245

LABELS_MAPPING_FORWARD = {
    'national': 0,
    'international': 1,
    'economics': 2,
    'entertainment': 3,
    'sports': 4
}

LABELS_MAPPING_REVERSE = {
    0: 'national', 
    1: 'international', 
    2: 'economics', 
    3: 'entertainment', 
    4: 'sports'
}

get_label_name = lambda label_id: LABELS_MAPPING_REVERSE(label_id)
get_label_class = lambda name: LABELS_MAPPING_REVERSE(name)