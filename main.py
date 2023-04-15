import logging
from pytube import YouTube, Playlist
from datetime import timedelta
import os
from pathlib import Path


class YouTubeDownloader:
	def __init__(self, path_to_downloads=os.path.join(os.getcwd(), "downloads"), log_level=logging.INFO):
		self.path_to_downloads = path_to_downloads
		self.log_level = log_level
		self.logger = self._setup_logger()

	def _setup_logger(self):
		logger = logging.getLogger(__name__)
		logger.setLevel(self.log_level)
		handler = logging.StreamHandler()
		formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
		handler.setFormatter(formatter)
		logger.addHandler(handler)
		return logger

	def _check_video_exist(self, title):
		title = f"{title}.mp4"
		return Path(self.path_to_downloads, title).exists()

	def _progress_callback(self, stream, chunk, remaining_bytes):
		filesize = stream.filesize
		bytes_downloaded = filesize - remaining_bytes
		percent = round((bytes_downloaded / filesize) * 100, 2)
		
		bar_length = 50
		completed_length = int(percent / 100 * bar_length)
		remaining_length = bar_length - completed_length
		
		bar = "[" + "=" * completed_length + " " * remaining_length + "]"
		
		print(f"Baixando: {bar} {percent}%")

	def _download_video(self, stream, yt, path=''):
		if self._check_video_exist(yt.title):
			self.logger.info("O vídeo que deseja baixar já existe")
		else:
			try:
				self.logger.info(f">>> Iniciando o download do video {yt.title}")
				yt.register_on_progress_callback(self._progress_callback)
				stream.download(os.path.join(self.path_to_downloads, path))

				
			except Exception as e:
				self.logger.error(f"Erro ao baixar o vídeo: {str(e)}")

	def _download_playlist(self, playlist):
		"""Baixar todos os vídeos da playlist"""
		print(f">>> Iniciando o download da playlist {playlist.title}")
		try:
			for video in playlist.videos:
				stream = video.streams.get_highest_resolution()
				self._download_video(stream, video, path=f'playlist/{playlist.title}')
		except KeyError:
			pass
		except Exception as e:
			self.logger.error(f"Houve um durante o download da playlist {playlist.title}: {e}")

	def download(self, yt_link):
		"""Baixar video ou playlist"""
		try:
			self.logger.info("Carreganndo informações do youtube...")
			if 'list=' in yt_link:
				playlist = Playlist(yt_link)
				self._download_playlist(playlist)
			else:
				yt = YouTube(yt_link)
				stream = yt.streams.get_highest_resolution()
				self._download_video(stream, yt)

			self.logger.info("Download realizado com sucesso!")
		except Exception as e:
			self.logger.error(f"Houve um erro ao tentar realizar o download: {str(e)}")


def main():
	to_exit = False
	def start():
			nonlocal to_exit
			yt_link = str(input("Coloque aqui o link do video ou playlist ('exit' to quit): "))
			if yt_link.lower() != 'quit':
				yt_downloader = YouTubeDownloader()
				yt_downloader.download(yt_link)

				while True:
					continue_input = str(input("\nVocê deseja baixar mais vídeos? [S/N] ")).lower()
					if continue_input in ['s', 'sim', 'y', 'yes']:
						break
					elif continue_input in ['n', 'não', 'no']:
						to_exit = True
						break
					else:
						print("Escolha uma das opções [S/N] ")
	
	while True:
		if not to_exit:
			start()
		else:
			break

	print('Bye, Bye!')
	exit()

if __name__ == '__main__':
	main()