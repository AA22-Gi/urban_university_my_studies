example = 'Топинамбур'

if __name__ == '__main__':
    assert example[0] == 'Т'
    assert example[-1] == 'р'
    assert (example[int(len(example) / 2)::]) == 'амбур'
    assert (example[::-1]) == 'рубманипоТ'
    assert (example[1::2]) == 'оиабр'
