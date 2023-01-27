def family (*args):
    family_list = [
    'certificate of a large family',
    'social card',
    'maternity capital',
    'parking permit',
    'tax benefit',
    'reimbursement of expenses',
    "compensation for the purchase of children's goods"
    ]
    result = list(filter(lambda x: x in family_list, args))
    return result

print(family('newborn registration', 'parking permit', 'maternity capital', 'tax benefit', 'medical policy'))
