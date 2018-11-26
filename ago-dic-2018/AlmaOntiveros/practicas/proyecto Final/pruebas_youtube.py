import unittest
from unittest.mock import Mock
from dos_youtube import AppYoutube
from main import *
from Youtube import Video, AbstractRepo, AbstractYoutube
from base_de_datos import SQlite

class TestYTapp(unittest.TestCase):

    def setUp(self):

        self.yt = AppYoutube()
        self.videomock = Mock(ID="1", Titulo = "Café Tacvba - Aprovéchate", Duracion = "PT4M13S", NombreCanal = "CafeTacubaVEVO",  Fecha= "2013-05-24T07:01:01.000Z", Likes = self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Likes, Vistas = self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Vistas, Descripcion = "Music video by Café Tacvba performing Aprovéchate. (C) 2013 Universal Music Latino",Compartidas="642")
        self.video = Video(self.videomock.Titulo,self.videomock.Duracion,self.videomock.NombreCanal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
        #self.sql = GuardarVideo()
        #self.sql.GuardarVideo(self.video)
        print(self.videomock)

        ################################
        self.video2 = Video("Nombrevideo",10,"Nombredelcanal", "26 nov 2018", '7524', '24642',"Descripcionvideo")
        self.video2.Id=1
        self.video2.Compartidas=75431
    #Hace las pruebas de guardar un video y que todos sus atributos estén almacenados correctamente
    def test_Video(self):

        print("test_Video")
        self.assertEqual(self.video2.Id, 1)
        self.assertEqual(self.video2.Titulo, "Nombrevideo")
        self.assertEqual(self.video2.Duracion, 10 )
        self.assertEqual(self.video2.NombreCanal, "Nombredelcanal")
        self.assertEqual(self.video2.Fecha, "26 nov 2018" )
        self.assertEqual(self.video2.Likes, "7524")
        self.assertEqual(self.video2.Vistas, "24642")
        self.assertEqual(self.video2.Descripcion, "Descripcionvideo")




    #def test_modVideo(self):

    #    print("test_modVideo")
    #    SQlite.ModificarVideo(self.video2.Id,self.video2.Compartidas)
    #    actual=SQlite.MostrarVideo(self.video2.Id)
    #    expected=[self.video2.Id,'Nombrevideo',10,'Nombredelcanal', "26 nov 2018", 7524, 24642,'Descripcionvideo',self.video2.Compartidas]
    #    self.assertListEqual(expected,actual)

    def test_borrar(self):

        print("test_borrar")
        SQlite.BorrarVideo(self.video2.Id)
        actual=SQlite.MostrarVideo(self.video2.Id)
        expected=[]
        self.assertListEqual(expected,actual)

    def mostrar_video(self):
        print("Test_Mostrar")
        x=SQlite.MostrarVideo(self.video2.Id)
        expected=["Nombrevideo",10,"Nombredelcanal", "26 nov 2018", '7524', '24642',"Descripcionvideo"]
        self.assertListEqual(expected,x)

    def test_infoVideo(self):

        print("test_infoVideo")
        #self.assertEqual((5), self.video.ID)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Titulo, self.video.Titulo)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Duracion, self.video.Duracion)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").NombreCanal, self.video.NombreCanal)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Fecha, self.video.Fecha)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Likes, self.video.Likes)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Vistas, self.video.Vistas)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=N9eroXvvCiI").Descripcion, self.video.Descripcion)
        #self.assertEqual((150), self.video.Compartidas)


if __name__ == '__main__':
    unittest.main()
