import json

config = {
    "versionname" : "3.13.7fix1",
    "update_time" : "2026年9月",
    "download_link" : [
        "https://files.ygom.top/files/YGOMobile_3.13.7fix1.Apk"
    ],
	"pre_release_code" : {}
}

pre_release_code = """
100200292   100200292
"""

for i in pre_release_code.split('\n'):
    if len(i) == 0:
        continue
    code = i.split()
    config["pre_release_code"][code[0]] = code[1]

path = './site/ver_code.json'
with open(path, 'w', encoding = 'utf-8') as f :
	json.dump(config, f, indent = 4, ensure_ascii=False)