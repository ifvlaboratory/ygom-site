import json

config = {
    "versionname" : "3.13.6",
    "update_time" : "2026年7月",
    "download_link" : [
        "https://files.ygom.top/files/YGOMobile_3.13.6.Apk"
    ],
	"pre_release_code" : {}
}

pre_release_code = """
100269038	58083496
100269113	11876803
100269215	85482105
100266001	30752324
100266002	66247039
100266003	3635138
100266004	39030883
100266005	65424481
100266006	2419596
100266007	38817295
100266008	65302903
"""

for i in pre_release_code.split('\n'):
    if len(i) == 0:
        continue
    code = i.split()
    config["pre_release_code"][code[0]] = code[1]

path = './site/ver_code.json'
with open(path, 'w', encoding = 'utf-8') as f :
	json.dump(config, f, indent = 4, ensure_ascii=False)