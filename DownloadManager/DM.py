from PyQt5.QtWidgets import *
import pafy
import os
import urllib.request
from os import path
import sys

import humanize
from moviepy.editor import VideoFileClip
from Main import Ui_MainWindow


class mainapp(QMainWindow , Ui_MainWindow):
    def __init__(self , parent=None):
        super(mainapp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_Buttons()

    def Handle_UI(self):
        self.setFixedSize(777,530)

    def Handle_Buttons(self):
        self.btn_Download.clicked.connect(self.Download)
        self.btn_Browse.clicked.connect(self.Handle_Browser)
        self.btn_download_video.clicked.connect(self.Download_Youtube_Video)
        self.btn_videoinfo.clicked.connect(self.Get_Youtube_Video)
        self.btn_Browse_2.clicked.connect(self.Save_Browse)
        self.btn_Download_5.clicked.connect(self.PlayList_Download)
        self.btn_Browse_3.clicked.connect(self.Save_Browse)

    def Handle_Browser(self):
        save_loc = QFileDialog.getSaveFileName(self ,  caption="Save As" , directory=".",filter="All Files (*.*)")
        text = str(save_loc)
        savedlocation = (text[2:].split(',')[0].replace("'",""))
        self.LE_savelocation.setText(savedlocation)


    def Handle_progress(self , blocknum , blocksize , totalsize):
        read = blocknum * blocksize

        if totalsize > 0:
            precent = read * 100 / totalsize
            self.progressBar.setValue(precent)
            QApplication.processEvents() # partial solution to not responding

    def Download(self): #Download files
        url = self.LE_inserturl.text()
        save_location = self.LE_savelocation.text()

        try:
            urllib.request.urlretrieve(url , save_location , self.Handle_progress)
        except Exception:
            QMessageBox.warning(self, "Download Error", "The Download Failed")

        QMessageBox.information(self , "Download Completed" , "The Download Finished")
        self.progressBar.setValue(0)
        self.LE_inserturl.setText('')
        self.LE_savelocation.setText('')

    def Get_Youtube_Video(self):
        te = str(self.LE_insertvideourl.text())
        if (te == ''):
            QMessageBox.information(self, "Download Error", "Please insert The Video URL then Click on find video info")
        else:
            try:
                video_link = self.LE_insertvideourl.text()
                video = pafy.new(video_link)
                streams = video.videostreams
                streamsaudio = video.audiostreams
                for st in streams:
                    size = humanize.naturalsize(st.get_filesize())
                    if(st.extension == 'mp4'):
                        video_data = '{} {} {} {}' .format(st.mediatype , st.extension , st.quality , size)
                        self.cmb_videoinfo.addItem(video_data)

                for st2 in streamsaudio:
                    size2 = humanize.naturalsize(st2.get_filesize())
                    if (st2.extension == 'm4a'):
                        audio_data = '{} {} {} {}'.format(st2.mediatype, st2.extension, st2.quality, size2)
                        self.cmb_videoinfo_2.addItem(audio_data)


            except Exception:
                QMessageBox.warning(self, "Get info Error", "Cantnot get information")



    def Handle_progress_bar_video_Download(self,total, recvd, ratio, rate, eta):
        self.progressBar_4.setValue(ratio*100)
        QApplication.processEvents()

    def Handle_progress_bar_audio_Download(self,total, recvd, ratio, rate, eta):
        self.progressBar_5.setValue(ratio*100)
        QApplication.processEvents()

    def Download_Youtube_Video(self):
        te = str(self.LE_insertvideourl.text())
        te1 = str(self.LE_savelocation_2.text())
        if(self.cmb_videoinfo.currentIndex() == -1):
            QMessageBox.information(self, "Download Error", "Please click on Find Video info button to get differen qualities and sizes")
        elif(te == ''):
            QMessageBox.information(self, "Download Error", "Please insert The Video URL then Click on find video info")
        elif(te1 == ''):
            QMessageBox.information(self, "Download Error", "Browse and select folder to save video")

        else:
            try:
                video_link = self.LE_insertvideourl.text()
                video = pafy.new(video_link)
                save_location = self.LE_savelocation_2.text()
                st = video.videostreams
                st2 = video.audiostreams
                quality = self.cmb_videoinfo.currentIndex()
                quality2 = self.cmb_videoinfo_2.currentIndex()
                if(quality == -1):
                    h = video.getbest()
                    down = h.download(filepath = save_location ,quiet=True,callback=self.Handle_progress_bar_video_Download)
                else:
                    down = st[quality].download(filepath = save_location ,quiet=True,callback=self.Handle_progress_bar_video_Download)
                    down2 = st2[quality2].download(filepath = save_location ,quiet=True,callback=self.Handle_progress_bar_audio_Download)
                QMessageBox.information(self, "Download Completed", "The Download Finished, Pleeeeease Wait minute to combine the video and audio")
                try:
                    pathvideo = save_location + "/" + video.title + ".mp4"
                    pathaudio = save_location + "/" + video.title + ".m4a"
                    newpathvideo = save_location + "/" + video.title + "New" + ".mp4"
                    clip = VideoFileClip(pathvideo).subclip(0 , t_end=None)
                    clip.write_videofile(newpathvideo , audio = pathaudio)
                    QMessageBox.information(self, "Compining Completed", "The Compining between audio and video Finished")
                    QApplication.processEvents()
                except Exception:
                    QMessageBox.warning(self, "Combining Error", "The Combining Failed")

            except Exception:
                QMessageBox.warning(self, "Download Error", "The Download Failed")
            self.LE_insertvideourl.setText('')
            self.LE_savelocation_2.setText('')

    def Save_Browse(self):
        save = QFileDialog.getExistingDirectory(self , "Select Download Directory")
        self.LE_savelocation_2.setText(save)
        self.LE_savelocation_3.setText(save)

    def PlayList_Download(self):
        tex = str(self.LE_inserturl_3.text())
        tex1 = str(self.LE_savelocation_3.text())
        if (tex == ''):
            QMessageBox.information(self, "Download Error", "Please insert The playlist URL")
        elif(tex1 == ''):
            QMessageBox.information(self, "Download Error", "Browse and select folder to put playlist in")
        else:
            try:
                playlist_url = self.LE_inserturl_3.text()
                save_location = self.LE_savelocation_3.text()
                playlist = pafy.get_playlist(playlist_url)
                videos = playlist['items']
                os.chdir(save_location)
                if os.path.exists(str(playlist['title'])):
                    os.chdir(str(playlist['title']))
                else:
                    os.mkdir(str(playlist['title']))
                    os.chdir(str(playlist['title']))

                for video in videos:
                    p = video['pafy']
                    best = p.getbest(preftype='mp4')
                    best.download()
            except Exception:
                QMessageBox.warning(self, "Download Error", "The Download Failed")




def main():
    app = QApplication(sys.argv)
    window = mainapp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
