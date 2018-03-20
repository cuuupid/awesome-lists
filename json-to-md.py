import os, json

with open('curated_lists.md','w') as curated_lists_md:
    with open('curated_lists.json','r') as curated_lists_json:
        curated_lists = json.load(curated_lists_json)
        for curated_list in curated_lists:
            curated_lists_md.write('* [`{}`]({}): {}\n'.format(
                curated_list['repo'],
                'https://www.github.com/'+curated_list['repo'],
                curated_list['description']
            ))
