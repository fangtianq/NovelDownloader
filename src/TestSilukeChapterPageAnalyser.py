#!/usr/bin/python
# -*- coding: gbk -*-
__author__ = 'jiangyh'

import unittest
from SilukeChapterPageAnalyser import SilukeChapterPageAnalyser
from FileTool import FileTool

class TestSilukeChapterPageAnalyser(unittest.TestCase):
    def setUp(self):
        self.__pagestr = FileTool().LoadFile('test_data/siluke_chapter_page.html')

    def test_get_chapter_title(self):
        analyser = SilukeChapterPageAnalyser(self.__pagestr)
        self.assertEqual('��һ�� ������ĸ���', analyser.get_chapter_title())

    def test_get_content(self):
        analyser = SilukeChapterPageAnalyser(self.__pagestr)
        content = analyser.get_content()
        self.assertGreater(len(content), 8000)
        self.assertEqual('>\n��һҳ&lt;\n������������', content[:25])
