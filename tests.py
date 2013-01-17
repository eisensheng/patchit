# -*- coding: utf-8 -*-
import os
import unittest
import patchit


def _get_path_to_asset(filename):
    return os.path.join(os.path.dirname(__file__), 'assets', filename)


class ParsingTestCase(unittest.TestCase):
    def test_patch_parsing(self):
        """simple valid patch parsing test.

        The test is successful if the filenames are set and a single hunk is
        present."""
        with open(_get_path_to_asset('a.patch')) as f_hand:
            patches = patchit.PatchSet.from_stream(f_hand)
        self.assertEqual(patches[0].source_filename,
                         'telefonliste2007.txt')
        self.assertEqual(patches[0].target_filename,
                         'telefonliste2008.txt')
        self.assertEqual(len(patches[0].hunks), 1)

    def test_patch_parsing_multi_hunks(self):
        """simple valid patch parsing with 2 hunks test."""
        with open(_get_path_to_asset('b.patch')) as f_hand:
            patches = patchit.PatchSet.from_stream(f_hand)
        self.assertEqual(patches[0].source_filename, 'a')
        self.assertEqual(patches[0].target_filename, 'b')
        self.assertEqual(len(patches[0].hunks), 2)

    def test_multi_patch_parsing(self):
        """simple valid patch parsing for multiple files."""
        with open(_get_path_to_asset('c.patch')) as f_hand:
            patches = patchit.PatchSet.from_stream(f_hand)

        self.assertEqual(patches[0].source_filename, 'a')
        self.assertEqual(patches[0].target_filename, 'b')
        self.assertEqual(len(patches[0].hunks), 2)

        self.assertEqual(patches[1].source_filename, 'abc')
        self.assertEqual(patches[1].target_filename, 'def')
        self.assertEqual(len(patches[1].hunks), 1)


class PatchingTestCase(unittest.TestCase):
    maxDiff = 2048

    def test_patch_apply_simple(self):
        """successfully merge a simple patch on a text file."""
        with open(_get_path_to_asset('a.patch')) as patch_hand, \
             open(_get_path_to_asset('original_a.txt')) as source_hand:
            patches = patchit.PatchSet.from_stream(patch_hand)
            file_iter = (x.strip('\n') for x in iter(source_hand.readline, ''))
            output = list(patches[0].merge(patchit.LineEnumerator(file_iter)))

        self.assertEqual(output, ['Mayer, Susanne, Lager, -212',
                                  'Schmid, Carola, Geschäftsleitung, -435',
                                  'Schmitt, Marie, Labor, -804',
                                  'Waldmann, Ernst, Labor, -805',
                                  'Zundel, Walter, Vertrieb, -476', ])

    def test_patch_multi_hunk(self):
        with open(_get_path_to_asset('d.patch')) as patch_hand, \
             open(_get_path_to_asset('original_d.txt')) as original_hand:
            patches = patchit.PatchSet.from_stream(patch_hand)
            file_iter = (x.strip('\n')
                         for x in iter(original_hand.readline, ''))
            output = list(patches[0].merge(file_iter))

        self.assertEqual(output, ['Lorem ipsum dolor sit amet, consetetur',
                                  'sadipscing elitr, sed diam nonumy',
                                  'eirmod tempor invidunt ut labore et',
                                  'voluptua. At vero eos et accusam et',
                                  'justo duo dolores et ea rebum. Stet',
                                  'clita kasd gubergren, no sea takimata',
                                  'sanctus est Lorem ipsum dolor sit amet.',
                                  'Lorem ipsum dolor sit amet, consetetur',
                                  'sadipscing elitr, sed diam nonumy',
                                  'eirmod tempor invidunt ut labore et',
                                  'dolore magna aliquyam erat, sed diam',
                                  'voluptua. At vero eos et accusam et',
                                  'justo duo dolores et ea rebum. Stet',
                                  'clita kasd gubergren, no sea takimata',
                                  'sanctus est Lorem ipsum dolor sit',
                                  'amet. Lorem ipsum dolor sit amet,',
                                  'nonumy eirmod tempor invidunt ut',
                                  'nonumy eirmod tempor invidunt ut',
                                  'labore et dolore magna aliquyam erat,',
                                  'labore et dolore magna aliquyam erat,',
                                  'sed diam voluptua. At vero eos et',
                                  'accusam et justo duo dolores et ea',
                                  'rebum. Stet clita kasd gubergren,',
                                  'no sea takimata sanctus est Lorem',
                                  'ipsum dolor sit amet.', ])
