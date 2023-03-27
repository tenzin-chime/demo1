from pathlib import Path
from intertext_files_merger.filename_regrouper import regroup_filename
from intertext_files_merger.text_merger import merge_texts,is_alignment_file,merge_xml
from intertext_files_merger.alignment_merger import merge_alignment_file,get_alignment_text
from intertext_files_merger.text_saver import save_text
from scripts.extract_msg import get_file_names

def merge_texts(regrouped_filenames): 
    merged_text_id={}

    for text_id,regrouped_filename in regrouped_filenames.items():
        merged_xmls = {}
        for language,language_filepaths in regrouped_filename.items():
            if is_alignment_file(language):
                merged_xmls[language]=merge_alignment_file(language_filepaths)
            else:
                merged_xmls[language]=merge_xml(language_filepaths)
            merged_text_id.update({text_id:merged_xmls})
    return merged_text_id

def merge_alignment_file(alignment_filepaths):
    merged_xmls=get_alignment_text(alignment_filepaths)
    return merged_xmls


if __name__ == "__main__":
    input_dir = Path('./tests/data/t001-input')
    input_directory = "./tests/data/t001-input"
    output_dir = "./tests/data/t001_output"
    regrouped_filenames = regroup_filename(input_dir)
    merged_texts=merge_texts(regrouped_filenames)
    output_directory = Path("./tests/data/t001_output/")
    for text_id,language_files in merged_texts.items():
        for lang,lang_text in language_files.items():
           file_name= text_id+"."+lang+".xml"           
           file_path = output_directory/file_name
           file_path.write_text(lang_text,encoding="utf-8")
    save_text(input_dir)
    
