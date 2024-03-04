from sys import stdin

page_titles = stdin.readlines()
query = page_titles.pop().lower().rstrip('\n')

result_idxs = (idx for idx, title in enumerate(page_titles) if query in title.lower().rstrip('\n'))
[print(page_titles[res_idx].rstrip('\n')) for res_idx in result_idxs]
