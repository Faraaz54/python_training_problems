site_title = 'args and kwargs eg'
ex_1 = [1,2,3,4]
ex_2 = 'great'

kex_1 = 'wow'
kex_2 = [1,2,3]

def blog_post(site_title, *args, **kwargs):
    print site_title
    for arg in args:
        print arg
    for id, kwarg in kwargs.items():
        print id, kwarg


blog_post(site_title, ex_1, ex_2, kex_1 = 'wow', kex_2 = [1,2,3])