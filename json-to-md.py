import os, json

template='''# Curated Lists

Ever wish there was a curated list for your curated lists, including other curated lists of curated lists that may or may not contain other curated lists?

``` python
print('A curated list of '+('curated lists of '*∞)+'curated lists.')
```

_Updated as often as I can. Want to contribute? Go ahead and make a pull request._

- [x] Index top 1000 curated lists.
- [x] Make a bot do it for me
- [x] Automate the curation entirely
- [ ] Organize lists
- [ ] Create easy search for lists.

# Lists

'''


with open('README.md','w') as curated_lists_md:
    curated_lists_md.write(template)
    with open('curated_lists.json','r') as curated_lists_json:
        curated_lists = json.load(curated_lists_json)
        for curated_list in curated_lists:
            curated_lists_md.write('* [`{}`]({}): {}\n'.format(
                curated_list['repo'],
                'https://www.github.com/'+curated_list['repo'],
                curated_list['description']
            ))
