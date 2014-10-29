def dna_starts_with(dna, pattern):
    """ Return True if 'dna' starts with 'pattern' """
    # Sanitize input
    dna = dna.upper()
    pattern = pattern.upper()

    if not (set(dna) <= set('CGTA')):
        raise ValueError('DNA contains garbage: %s' % set(dna))
    if not (set(pattern) <= set('CGTA')):
        raise ValueError('Pattern contains unexpected nucleotides: %s' % set(dna))

    # Pattern is too large
    if len(pattern) > len(dna): return False

    return pattern == dna[:len(pattern)]

def convert_genotypes(genotypes):
    """ Converts list of genotypes as string to genotypes as integers """
    convertions = {'AA': 0, 'AG': 1, 'GG': 2}

    assert set(genotypes) <= set(convertions.keys())

    result = []
    for genotype in genotypes:
        result.append(convertions[genotype])
    return result
