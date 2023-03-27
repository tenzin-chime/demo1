from pathlib import Path
from bs4 import BeautifulSoup
from intertext_files_merger.filename_regrouper import regroup_filename
from intertext_files_merger.alignment_merger import merge_alignment_file

def merge_text(soup, last_p_id):  
    cur_paras = soup.find_all("p")
    for cur_para in cur_paras:
        sentences = cur_para.find_all("s")
        last_p_id+=1
        cur_para.attrs['id'] = last_p_id
        update_sentence(sentences,last_p_id)
        
def update_sentence(sentences,cur_par_id):
    cur_sentence_count =1
    for sentence in sentences:
        sentence.attrs['id'] = f"{cur_par_id}:{cur_sentence_count}"
        cur_sentence_count+=1

def get_language_text(file_paths):
    new_xml = BeautifulSoup(features='xml')
    root = new_xml.new_tag('text')
    new_xml.append(root)
    last_p_id=0
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            xml = f.read()
            soup = BeautifulSoup(xml, 'xml')
        
        cur_file_last_pid=soup.find_all('p')[-1]['id']
        merge_text(soup,last_p_id)
        create_xml(soup,root)
        last_p_id += int(cur_file_last_pid)  
    return new_xml.prettify()

def create_xml(soup,root): 
    p_tags=soup.find_all('p')
    for p_tag in p_tags:
        root.append(p_tag)    
    
def merge_xml(language_filepaths):
    merged_xmls=get_language_text(language_filepaths)
    return merged_xmls

def is_alignment_file(language):
    if "." in language:
        return True
    return False

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


if __name__ =="__main__":
   input_dir=Path('./tests/data/t001-input')
   regrouped_filenames=regroup_filename(input_dir)
   merged_texts=merge_texts(regrouped_filenames)
   output_directory = Path("./tests/data/t001_output/")
   for text_id,language_files in merged_texts.items():
        for lang,lang_text in language_files.items():
           file_name= text_id+"."+lang+".xml"           
           file_path = output_directory/file_name
           file_path.write_text(lang_text,encoding="utf-8")        