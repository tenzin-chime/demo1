from pathlib import Path
from intertext_files_merger.filename_regrouper import regroup_filename


def test_regroup_filename():
    input_dir = Path('./tests/data/t001-input')
    expected_output = {
        "t001":{
            'bo': [
            Path("./tests/data/t001-input/t001-01-padma.bo.xml"),
            Path("./tests/data/t001-input/t001-03-jc.bo.xml")
            ],
            'cn': [
            Path("./tests/data/t001-input/t001-01-padma.cn.xml"),
            Path("./tests/data/t001-input/t001-03-jc.cn.xml")
            ],
            'bo.cn': [
            Path("./tests/data/t001-input/t001-01-padma.bo.cn.xml"),
            Path("./tests/data/t001-input/t001-03-jc.bo.cn.xml")
            ]
        }   
    }
    
    regrouped_filename = regroup_filename(input_dir)
    assert regrouped_filename == expected_output

if __name__ == "__main__":
    test_regroup_filename()
