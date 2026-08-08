def split_by_letters(query, letters, space = " "):
    if not query.strip():
        return []

    parts, current = [], []
    neutral, check = 0, None

    for chr in query:
        if chr == space:
            neutral += 1
            continue

        in_letters = chr in letters

        if check is None:
            if in_letters and neutral:
                current.append(space)

            current.append(chr)

        elif in_letters == check:
            if neutral:
                current.append(space)

            current.append(chr)

        elif neutral > 1:
            if check:
                current.append(space)
                parts.append("".join(current))
                current = [chr]

            else:
                parts.append("".join(current))
                current = [space, chr]

        else:
            parts.append("".join(current))
            current = [chr]

        check = in_letters
        neutral = 0

    if neutral and check:
        current.append(space)

    if current:
        parts.append("".join(current))

    return parts