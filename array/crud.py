# Create & Read & Update & Delete


def add(array, new_element, position=None):
    if not position:
        return array.append(new_element)
    else:
        return array.insert(position, new_element)


def get(array, position=None):
    if not position:
        return array[-1]
    else:
        return array[position]


def update(array, new_element, position=None):
    if not position:
        array[-1] = new_element
        return array
    else:
        array[position] = new_element
        return array


def delete(array, position=None):
    if not position:
        del(array[-1])
        return array
    else:
        del(array[position])
        return array
