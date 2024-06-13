import os
import shutil

def copy_static_to_public() -> None:

    def copy_files(src, dst) -> None:
        print(f"Start copying {src} to {dst}")
        items = os.listdir(src)
        for item in items:
            old_path = os.path.join(src, item)
            new_path = os.path.join(dst, item)
            if os.path.isfile(old_path):
                print(f"Copying {old_path} to {new_path}")
                shutil.copy(old_path, new_path)
            elif os.path.isdir(old_path):
                os.mkdir(new_path)
                copy_files(old_path, new_path)
        return

    if os.path.exists("./public"):
        shutil.rmtree("./public")
    os.mkdir("./public")
    copy_files("./static", "./public")
    return