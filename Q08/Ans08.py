move_pattern = [[0, 1], [0, -1], [1, 0], [-1, 0]]
N = 12


def move(log):
    if len(log) == N + 1:
        return 1

    cnt = 0
    for pattern in move_pattern:
        next_position = []
        next_position = [log[-1][0] + pattern[0], log[-1][1] + pattern[1]]
        # 一度、この座標に来ていないのならば、座標を配列に追加する
        if next_position not in log:
            # 2次元配列を'+'で追加するときは、このように[]で囲む
            cnt += move(log + [next_position])
            continue
    return cnt


print(move([[0, 0]]))
