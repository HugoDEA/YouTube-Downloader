from pytube import YouTube

def Download(link):
  youtubeObject = YouTube(link)
  youtubeObject = youtubeObject.streams.get_highest_resolution()
  try:
    youtubeObject.download()
    print("Le téléchargement à été effectué.")
  except :
    print("Erreur !")
    
link = input("Mettez votre lien YouTube ici : ")
Download(link)