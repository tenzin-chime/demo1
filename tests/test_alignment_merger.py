from pathlib import Path
from intertext_files_merger.alignment_merger import get_alignment_text


def test_merge_text():
    expected_output=Path('./tests/data/t001-output/t001.bo.cn.xml').read_text(encoding="utf-8")
    file_paths=['./tests/data/t001-input/t001-01-padma.bo.cn.xml','./tests/data/t001-input/t001-03-jc.bo.cn.xml']
    merged_alignment=get_alignment_text(file_paths)
    assert merged_alignment == expected_output