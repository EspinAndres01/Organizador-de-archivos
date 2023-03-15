import os
from PIL import Image
import mimetypes

# Obtener una lista de todas las extensiones de archivo conocidas
ext_all = set(mimetypes.types_map.values())

class FileOrganizer():
    def __init__(self, file_path, organized_folder):
        self.file_path = file_path
        self.organized_folder = organized_folder

    def organize_file(self):
        # Create organized folders
        organized_files = os.path.join(self.organized_folder, 'ArchivosOrganizados')
        organized_filesImage = os.path.join(organized_files, 'Imagenes')
        organized_filesAudios = os.path.join(organized_files, 'Audios')
        organized_filesVideos = os.path.join(organized_files, 'Videos')
        organized_filesDocumentos = os.path.join(organized_files, 'Documentos')
        organized_filesTXT = os.path.join(organized_files, 'TXT')
        organized_filesFuentes = os.path.join(organized_files, 'Fuetes')
        organized_filesComprimidos = os.path.join(organized_files, 'Comprimidos')
        organized_filesEXE = os.path.join(organized_files, 'Ejecutables')
        organized_filesScripts=os.path.join(organized_files,'Scripts')
        organized_filesMisellaneous=os.path.join(organized_files,'Miselaneos')

        os.mkdir(organized_files)
        os.mkdir(organized_filesImage)
        os.mkdir(organized_filesAudios)
        os.mkdir(organized_filesVideos)
        os.mkdir(organized_filesDocumentos)
        os.mkdir(organized_filesTXT)
        os.mkdir(organized_filesFuentes)
        os.mkdir(organized_filesComprimidos)
        os.mkdir(organized_filesEXE)
        os.mkdir(organized_filesScripts)
        os.mkdir(organized_filesMisellaneous)

        # Organize files
        ext_image = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.ico', '.svg')
        ext_audio = ('.mp3', '.wav', '.ogg', '.wma', '.m4a', '.aac', '.flac', '.alac')
        ext_video = ('.mp4', '.avi', '.mkv', '.mov', '.flv', '.wmv', '.mpeg', '.mpg')
        ext_document = ('.doc', '.docx', '.pdf', '.ppt', '.pptx', '.xls', '.xlsx', '.csv')
        ext_text = ('.txt', '.md', '.log', '.rtf')
        ext_code = ('.py', '.ipynb', '.cpp', '.c', '.java', '.js', '.html', '.css', '.php')
        ext_archive = ('.zip', '.tar', '.tar.gz', '.tar.bz2', '.tar.xz', '.rar', '.7z')
        ext_executable = ('.exe', '.msi')
        ext_font = ('.otf', '.ttf')
        ext_miscellaneous = ('.dat', '.cfg', '.ini', '.db')

        

        for dirpath, dirnames, filenames in os.walk(self.file_path):
            for filename in filenames:
                if filename.endswith(ext_image):
                    try:
                        img = Image.open(os.path.join(dirpath, filename))
                        img.verify()
                        img.close()
                        os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesImage, filename))
                    except:
                        pass
                elif filename.endswith(ext_audio):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesAudios, filename))
                elif filename.endswith(ext_video):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesVideos, filename))
                elif filename.endswith(ext_document):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesDocumentos, filename))
                elif filename.endswith(ext_font):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesFuentes, filename))
                elif filename.endswith(ext_text):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesTXT, filename))
                elif filename.endswith(ext_archive):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesComprimidos, filename))
                elif filename.endswith(ext_executable):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesEXE, filename))
                elif filename.endswith(ext_code):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesScripts, filename))  
                elif filename.endswith(ext_miscellaneous):
                    os.rename(os.path.join(dirpath, filename), os.path.join(organized_filesMisellaneous, filename))        
