#!/usr/bin/env python
# encoding: utf-8
"""
test_nend.py

Created by Keith Fahlgren on Mon Jun 13 16:12:29 PDT 2011
Copyright (c) 2011 Threepress Consulting Inc. All rights reserved.
"""

import glob
import logging
import os.path

from nose.tools import *

from lxml import etree


import nend


log = logging.getLogger(__name__)


class TestNend(object):
    def setup(self):
        self.testfiles_dir = os.path.join(os.path.dirname(__file__), 'files')

    def test_end_valid(self): 
        """An EPUB Navigation Document document should be able to be successfully validated"""
        valid_end_fn = os.path.join(self.testfiles_dir, 'good.nav.html')
        valid_end = etree.parse(valid_end_fn)
        assert(nend.validate(valid_end))

    def test_end_not_valid_rnc(self): 
        """An EPUB Navigation Document with RELAX NG errors should not be able to be successfully validated"""
        not_valid_end_fn = os.path.join(self.testfiles_dir, 'invalid.rnc.html')
        not_valid = etree.parse(not_valid_end_fn)
        assert(not(nend.validate(not_valid)))

    def test_end_not_valid_sch(self): 
        """An EPUB Navigation Document with Schematron errors should not be able to be successfully validated"""
        not_valid_end_fn = os.path.join(self.testfiles_dir, 'invalid.sch.html')
        not_valid = etree.parse(not_valid_end_fn)
        assert(not(nend.validate(not_valid)))


    def test_xhtml_nend_output_valid_smoke(self):
        """All NCX documents collected for smoketesting should be able to be transformed into a valid EPUB Navigation Document"""
        smoketests_dir = os.path.join(self.testfiles_dir, 'smoketests')
        for ncx_fn in glob.glob(smoketests_dir + '/*.ncx'):
            log.debug('\nSmoke testing transformation and validation of %s' % ncx_fn)
            ncx = etree.parse(ncx_fn)
            end = nend.ncx.as_end(self.test_tml)
            assert(nend.validate(end))

