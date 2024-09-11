# video_cutter.py
from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def decouper_video(video_path, nombre_parties, dossier_sortie, fichier_log):
    """
    Découpe une vidéo en plusieurs parties égales et enregistre chaque partie dans un dossier.

    Args:
        video_path (str): Chemin vers la vidéo originale.
        nombre_parties (int): Nombre de parties dans lesquelles découper la vidéo.
        dossier_sortie (str): Dossier où les vidéos découpées seront enregistrées.
        fichier_log (str): Chemin vers le fichier texte où seront enregistrés les chemins et titres des vidéos.
    """
    video = VideoFileClip(video_path)
    duree_partie = video.duration / nombre_parties

    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)

    with open(fichier_log, 'a') as log:
        for i in range(nombre_parties):
            debut = i * duree_partie
            fin = (i + 1) * duree_partie

            nom_partie = f"partie_{i+1}.mp4"
            chemin_partie = os.path.join(dossier_sortie, nom_partie)

            partie = video.subclip(debut, fin)
            partie.write_videofile(chemin_partie, codec="libx264")

            log.write(f"{chemin_partie}, Titre: {nom_partie}\n")

    video.close()
