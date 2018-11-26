import unittest
from unittest.mock import Mock
from twitter_ap import AppTwitter
from Tweet import *
from baseladvd import basedb

class Test(unittest.TestCase):

    def setUp(self):

        self.tw = AppTwitter()
        self.usuariomock = Mock(user_id = "469827228", handle = "schiob", lugar = " ",\
        verificado = "Usuario no verificado.",  followers = 131, numtweets = 466, friends = 115,\
        description = "Ingeniero en sistemas y músico clásico", lenguaje = "es",\
         profile = "http://pbs.twimg.com/profile_images/961861584996806657/U4VAdOI0_normal.jpg",\
         Ranking = None,Categoria = None,Victorias = 0,Derrotas = 0)
        self.usuario = Tweeti(self.usuariomock.user_id,self.usuariomock.handle,self.usuariomock.lugar,\
        self.usuariomock.verificado,self.usuariomock.followers,self.usuariomock.numtweets,\
        self.usuariomock.friends,self.usuariomock.description,self.usuariomock.lenguaje,\
        self.usuariomock.profile,self.usuariomock.Ranking,self.usuariomock.Categoria,self.usuariomock.Victorias,\
        self.usuariomock.Derrotas)

        self.sql = basedb()
        self.sql.insert_db(self.usuario)

        self.usuario1 = Tweeti('8276239','Enormisar','Leyends never die','los pixis',456,368,901,'velocito !','supp','ruidoso',None,None,0,0)

    def tearDown(self):
        print("Fin de la prueba")

    #Hace las pruebas de guardar
    def test_Usuario(self):

        print("test_Usuario")
        self.assertEqual(self.usuario1.user_id, '8276239')
        self.assertEqual(self.usuario1.handle, 'Enormisar')
        self.assertEqual(self.usuario1.lugar, 'Leyends never die' )
        self.assertEqual(self.usuario1.verificado, "los pixis" )
        self.assertEqual(self.usuario1.followers, 456 )
        self.assertEqual(self.usuario1.numtweets, 368 )
        self.assertEqual(self.usuario1.friends, 901 )
        self.assertEqual(self.usuario1.description, 'velocito !')
        self.assertEqual(self.usuario1.lenguaje, 'supp')
        self.assertEqual(self.usuario1.profile, 'ruidoso')
        self.assertEqual(self.usuario1.Ranking, None)
        self.assertEqual(self.usuario1.Categoria, None)
        self.assertEqual(self.usuario1.Victorias, 0)
        self.assertEqual(self.usuario1.Derrotas, 0)

        #Tipo de dato
        self.assertNotEqual(self.usuario1.followers, '456' )
        self.assertNotEqual(self.usuario1.numtweets, '368' )
        self.assertNotEqual(self.usuario1.friends, '901')
        self.assertNotEqual(self.usuario1.Victorias, '0')
        self.assertNotEqual(self.usuario1.Derrotas, '0')


    def testinsert(self):
        print("testinsert")
        self.assertTrue(self.sql.insert_db(self.tw.getUsuario("Armando31647954")))

    def testupdate(self):
        print("test_update")
        self.assertTrue(self.sql.updateUsuario(self.usuario.handle,self.usuario.Ranking,\
        self.usuario.Categoria,self.usuario.Victorias,self.usuario.Derrotas))

    def testborrar(self):
        print("test_borrar")
        self.assertTrue(self.sql.deleteUsuario(self.usuario.handle))

    def test_getUsuario(self):
        print("test_getUsuario")
        self.assertEqual(self.tw.getUsuario("Armando31647954").user_id, self.usuario.user_id)
        self.assertEqual(self.tw.getUsuario("Armando31647954").handle, self.usuario.handle)
        self.assertEqual(self.tw.getUsuario("Armando31647954").lugar, self.usuario.lugar)
        self.assertEqual(self.tw.getUsuario("Armando31647954").verificado, self.usuario.verificado)
        self.assertEqual(self.tw.getUsuario("Armando31647954").followers, self.usuario.followers)
        self.assertEqual(self.tw.getUsuario("Armando31647954").numtweets, self.usuario.numtweets)
        self.assertEqual(self.tw.getUsuario("Armando31647954").friends, self.usuario.friends)
        self.assertEqual(self.tw.getUsuario("Armando31647954").description, self.usuario.description)
        self.assertEqual(self.tw.getUsuario("Armando31647954").lenguaje, self.usuario.lenguaje)
        self.assertEqual(self.tw.getUsuario("Armando31647954").profile, self.usuario.profile)
        self.assertEqual(self.tw.getUsuario("Armando31647954").Ranking, self.usuario.Ranking)
        self.assertEqual(self.tw.getUsuario("Armando31647954").Categoria, self.usuario.Categoria)
        self.assertEqual(self.tw.getUsuario("Armando31647954").Victorias, self.usuario.Victorias)
        self.assertEqual(self.tw.getUsuario("Armando31647954").Derrotas, self.usuario.Derrotas)

if __name__ == '__main__':
    unittest.main()
