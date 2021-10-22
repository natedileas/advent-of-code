
def value_or_name(item, max_len=100):
    if isinstance(item, str):
        if len(item) < max_len:
            return item
        else:
            return [k for k, v in locals().items()][0]


def advent_assert(func, inputs, expected_values):
    for i, ev in zip(inputs, expected_values):
        try:
            recv_value = func(i)
            if recv_value != ev:
                print(f'{func.__name__}({value_or_name(i)}) => {recv_value} != {ev}')
            else:
                print(f'{func.__name__}({value_or_name(i)}) => {recv_value} == {ev}')

        except:
            import traceback
            traceback.print_exc()
