from os import path,listdir
import json
from tqdm import tqdm

from os import listdir,getcwd,path,chdir
old_cwd=getcwd()
chdir(path.join(getcwd(),"modules"))
from modules.img_tag_module import tag
chdir(old_cwd)

ID_TAGS_ARR=[]
IMPORT_IMAGE_PATH="./../../../import/images"
file_names=listdir(IMPORT_IMAGE_PATH)
for file_name in tqdm(file_names):
    file_id=int(file_name[:file_name.index('.')])
    all_tags=tag(f"{IMPORT_IMAGE_PATH}/{file_name}")
    ID_TAGS_ARR.append({"id":file_id,"tags":all_tags})

with open('./../../id_tags.txt', 'w') as outfile:
    json.dump(ID_TAGS_ARR, outfile)