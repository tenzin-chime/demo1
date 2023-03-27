from bs4 import BeautifulSoup

def merge_text(soup,last_xtarget):
    cur_links = soup.find_all("link")
    for cur_link in cur_links:
        xtargets = cur_link["xtargets"].split(";")
        new_xtargets = []
        
        if xtargets[0]!="":
            part1_xtarget= xtargets[0].split(":")
            part1_xtarget[0] = str(int(part1_xtarget[0]) + last_xtarget[0])
        else:
            part1_xtarget=[]
        if xtargets[1]!="":
            part2_xtarget = xtargets[1].split(":")
            part2_xtarget[0] = str(int(part2_xtarget[0]) + last_xtarget[1])
        else:
            part2_xtarget=[]
        new_xtargets.append(":".join(part1_xtarget))
        new_xtargets.append(":".join(part2_xtarget))
        cur_link["xtargets"] = ";".join(new_xtargets)
        cur_link["status"]= cur_link["status"]       

def get_alignment_text(file_paths):
    new_xml = BeautifulSoup(features='xml')
    root = new_xml.new_tag('linkGrp')
    root['toDoc']='t001.cn.xml'
    root['fromDoc']='t001.bo.xml'
    new_xml.append(root)
    last_xtarget=[0,0]
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            xml = f.read()
            soup = BeautifulSoup(xml, 'xml')
        l_xtarget=get_last_xtarget(soup)
        merge_text(soup,last_xtarget)
        create_xml(soup,root)
        update_last_target(last_xtarget,l_xtarget)

    return new_xml.prettify()

def get_last_xtarget(soup):
    cur_file_last_xtarget=soup.find_all('link')[-1]
    xtargets = cur_file_last_xtarget["xtargets"].split(";")
    last_xtarget=[]
    for xtarget in xtargets:
        parts = xtarget.split(":")
        last_xtarget.append(parts[0])
    return last_xtarget

def create_xml(soup,root):
    link_tags=soup.find_all('link')
    for link_tag in link_tags:
        root.append(link_tag)

def update_last_target(last_xtarget,l_xtarget):
    for i in range(len(last_xtarget)):
        last_xtarget[i] += int(l_xtarget[i])
    return last_xtarget

def merge_alignment_file(alignment_filepaths):
    merged_xmls=get_alignment_text(alignment_filepaths)
    return merged_xmls
