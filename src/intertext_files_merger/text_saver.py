import re
import os
import shutil
from pathlib import Path

input_directory = "./tests/data/t001-input"
output_dir = "./tests/data/t001_output"

def save_text(input_dir):
    list_of_files=list(input_dir.iterdir())
    list_of_files.sort()
    for file_path in list_of_files:
        file_name = file_path.stem
        extr=re.match(r"^([^-]*)[^\.]*\.(.*)$",file_name)
        main_file=extr.group(1)
        split_text_id_name= "split_"+str(main_file)
        xml_file=file_name+".xml"
        input_file_path = os.path.join(input_directory, xml_file)
        split_text_id_dir = os.path.join(output_dir, split_text_id_name)
        output_file_path=  os.path.join(split_text_id_dir, xml_file)
        if not os.path.exists(split_text_id_dir):
            os.makedirs(split_text_id_dir)
        shutil.copyfile(input_file_path, output_file_path)
        #print(f'Copied file {xml_file} to {split_text_id_dir}')

if __name__ == "__main__":
    input_dir = Path('./tests/data/t001-input')
    save_text(input_dir)