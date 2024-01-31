import os
import shutil
from PIL import Image
categories = {
    "Images": [".jpeg", ".jpg", ".png", ".gif"],
    "Text": [".doc", ".txt", ".pdf", ".xlsx", ".docx", ".xls", ".rtf"],
    "Videos": [".mp4", ".mkv"],
    "Sounds": [".mp3", ".wav", ".m4a"],
    "Applications": [".exe", ".lnk"],
    "Codes": [".c", ".py", ".java", ".cpp", ".js", ".html", ".css", ".php"],
}

other_folder = "Others"

def sort_files():
    target_directory = r"C:\Users\tvshr\Desktop\test" 
    os.chdir(target_directory)
    files = os.listdir(target_directory)

    print("Sorting the files...")

    for file in files:
        _, file_extension = os.path.splitext(file)
        dest = other_folder
        for category, extensions in categories.items():
            if file_extension.lower() in extensions:
                dest = category
                break

        dest_path = os.path.join(target_directory, dest)
        os.makedirs(dest_path, exist_ok=True)

        if dest == "Images" and file_extension.lower() in [".jpeg", ".jpg", ".png"]:
            try:
                prefix = os.path.splitext(file)[0]
                new_file_name = f"{prefix}.png"
                counter = 1
                while os.path.exists(os.path.join(dest_path, new_file_name)):
                    new_file_name = f"{prefix}_{counter}.png"
                    counter += 1

                im = Image.open(file)  
                im.save(os.path.join(dest_path, new_file_name))
                os.remove(file)

            except FileNotFoundError as e:
                print(f"Error processing {file}: {e}")
                continue

        else:
            try:
                shutil.move(file, dest_path)
            except FileNotFoundError as e:
                print(f"Error moving {file}: {e}")

    print("Sorting Completed...")

if __name__ == "__main__":
    sort_files()
