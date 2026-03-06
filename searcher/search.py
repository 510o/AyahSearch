from .diacritics import diac_rooms, combining

def search(query: str, quran_index, clean_index, simple_index):
    if not query:
        return []
    
    query_plain = "".join(c for c in query if not combining(c))
    with_diac = any(combining(c) for c in query)
    results = []

    for key, clean_text in clean_index.items():
        if query_plain in clean_text:
            if with_diac:
                simple_rooms = diac_rooms(simple_index[key])
                query_rooms = diac_rooms(query)
                i = 0

                for l in simple_rooms:
                    if query_rooms[i] in l:
                        i += 1
                        if i == len(query_rooms):
                            results.append((key, quran_index[key]))
                            break

                    elif combining(l[0]) and not combining(query_rooms[i][0]):
                        continue

                    else:
                        i = 0
                        
            else:
                results.append((key, quran_index[key]))
    return results