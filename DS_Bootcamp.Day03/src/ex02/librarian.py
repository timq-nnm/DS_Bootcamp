import sys
import subprocess
import shutil

def check_venv():
    if sys.base_prefix != sys.prefix and 'athislen' in sys.prefix:
        return True
    else:
        return False
    

def install_library():
    if check_venv():
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'beautifulsoup4', 'pytest']) 
    else:
        raise Exception('Wrong venv')
    
def list_libraries(lib_list='requirements.txt'):
    try:
        lib_list_str = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'], text=True)

        with open(lib_list, 'w') as file:
            file.write(lib_list_str)

        print(lib_list_str)
    except Exception as e:
        raise e

def archiving_env(archive_path, archive_name='athislen_env', archive_extension='zip'):
    try:
        shutil.make_archive(archive_name, archive_extension, archive_path)
    except Exception as e:
        raise e



if __name__ == '__main__':
    install_library()
    list_libraries()
    archiving_env('env')