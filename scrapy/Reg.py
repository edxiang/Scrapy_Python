# -*- coding: utf-8 -*-

import re

regBLANK = re.compile(r'\s{3,}', re.S | re.M)
regHTML = re.compile(r'<.*?>', re.S | re.M)
regNextLine = re.compile(r'<br/>')
regDoubleLine = re.compile(r'\n{3,}')

regLINE = re.compile(r'\n', re.S)


def blank(content):
    s = regBLANK.sub("", content)
    return s


def html(content):
    s = regHTML.sub("", content)
    return s


def nextLine(content):
    s = regNextLine.sub("\n", content)
    return s


def doubleLine(content):
    s = regDoubleLine.sub("", content)
    return s
