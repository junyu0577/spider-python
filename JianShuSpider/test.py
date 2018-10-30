str = 'https://www.jianshu.com/c/9ca077f0fae8?order_by=added_at&page=2'
if('page' in str):
    print(str[str.index('page')+5::])

import re

count = '    收录了2652篇文章 · 3122人关注   '
count = count.strip()
count = re.findall(r'\d+', count)
print(count)
