init_h = int(input())
init_m = int(input())
del_m_total = int(input())

init_m_total = init_h * 60 + init_m
cur_m_total = init_m_total + del_m_total
cur_m_total %= 24 * 60
cur_m = cur_m_total % 60
cur_h = cur_m_total // 60

print(f"{cur_h:0>2}:{cur_m:0>2}")