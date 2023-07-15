import os


class LocalStorage:
    plugins_folder = os.environ.get("PLUGINS_FOLDER", "plugins")

    @classmethod
    def save(cls, path, datafile):
        file_path = os.path.join(cls.plugins_folder, path)
        with open(file_path, "wb") as file:
            file.write(datafile)

    @classmethod
    def get_filename_list(cls):
        return os.listdir(cls.plugins_folder)
