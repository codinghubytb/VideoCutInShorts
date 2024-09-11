from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def decouper_video(video_path, nombre_parties, dossier_sortie, fichier_log):
    # Charger la vidéo
    video = VideoFileClip(video_path)
    
    # Calculer la durée de chaque partie
    duree_partie = video.duration / nombre_parties
    
    # Vérifier si le dossier de sortie existe, sinon le créer
    if not os.path.exists(dossier_sortie):
        os.makedirs(dossier_sortie)
    
    # Ouvrir le fichier de log pour y écrire les chemins et titres
    with open(fichier_log, 'a') as log:
        for i in range(nombre_parties):
            # Définir le début et la fin de chaque segment
            debut = i * duree_partie
            fin = (i + 1) * duree_partie
            
            # Créer un nom pour chaque partie
            nom_partie = f"partie_{i+1}.mp4"
            chemin_partie = os.path.join(dossier_sortie, nom_partie)
            
            # Découper la vidéo
            partie = video.subclip(debut, fin)
            
            # Sauvegarder chaque partie dans le dossier spécifié
            partie.write_videofile(chemin_partie, codec="libx264")
            
            # Écrire dans le fichier log
            log.write(f"{chemin_partie}, Titre: {nom_partie}\n")
    
    # Fermer la vidéo originale
    video.close()

# Exemple d'utilisation
decouper_video(r"C:\GIT\Mes Projets\VideoCutInShorts\downloadfilm.mp4", 105, r"C:\GIT\Mes Projets\VideoCutInShorts\videos", r"C:\GIT\Mes Projets\VideoCutInShorts\video.txt")
