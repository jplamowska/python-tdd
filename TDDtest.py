import unittest, TDD

class TESTStringMethods(unittest.TestCase):
    def test_f1(self):
        w = TDD.f1(0)
        self.assertEqual(w,0)

    def test_f1_refactor(self):
        w= TDD.f1(1)
        self.assertEqual(w,1)

    def test_f1_rf2(self):
        w=TDD.f1(2)
        self.assertEqual(w,4)

    def test_f1_rf3(self):
        w=TDD.f1(2,1)
        self.assertEqual(w,5)

    def test_f1_rf4(self):
        w=TDD.f1(2,3)
        self.assertEqual(w,7)

    def test_f2(self):
        w=TDD.f2("ala")
        self.assertEqual(w,"a")

    def test_f2_innyprzyklad(self):
        w=TDD.f2([1,2,3])
        self.assertEqual(w,1)

    def test_f2_innyprzyklad2(self):
        w=TDD.f2([])
        self.assertEqual(w,"BUUUUM")

    def test_f3_jaka_to_liczba(self):
        w=TDD.f3(1)
        self.assertEqual(w,"jeden")

    def test_f3_jaka_to_liczba2(self):
        w=TDD.f3(2)
        self.assertEqual(w,"dwa")

    def test_f3_jaka_to_liczba3(self):
        w=TDD.f3(3)
        self.assertEqual(w,"trzy")

    def test_f3_jaka_to_liczba_other(self):
        w=TDD.f3(999)
        self.assertEqual(w, "other")

    def test_f4_kto_co_ma(self):
        w=TDD.f4("kot", "mysz")
        self.assertEqual(w, "kot ma kota i mysz")

    def test_f4_kto_co_ma1(self):
        w=TDD.f4("kot", "")
        self.assertEqual(w, "kot ma kota")

    def test_f5(self):
        w=TDD.f5(0)
        self.assertEqual(w, [])

    def test_f5_jeden(self):
        w=TDD.f5(1)
        self.assertEqual(w, [0])

    def test_f5_dwa(self):
        w=TDD.f5(2)
        self.assertEqual(w, [0, 1])

    def test_f5_siedem(self):
        w=TDD.f5(7)
        self.assertEqual(w, [0, 1, 2, 3, 4, 5, 6])

    def test_f5_siedem_dwa(self):
        w=TDD.f5(7, 2)
        self.assertEqual(w, [0, 2, 4, 6])

    def test_f5_siedemnascie_dwa(self):
        w=TDD.f5(17, 2)
        self.assertEqual(w, [0, 2, 4, 6, 8, 10, 12, 14, 16])

    def test_f5_siedemnascie_piec(self):
        w=TDD.f5(17, 5)
        self.assertEqual(w, [0, 5, 10, 15])

    def test_f6_jeden(self):
        w = TDD.f6(1, '*')
        self.assertEqual(w, '*')

    def test_f6_siedem(self):
        w = TDD.f6(7, '*')
        self.assertEqual(w, '*******')

    def test_f7_slowo(self):
        w = TDD.f7('ala')
        self.assertEqual(w, 'slowo')

    def test_f7_cyfra(self):
        w = TDD.f7(1)
        self.assertEqual(w, 'cyfra')

    def test_f7_liczba(self):
        w = TDD.f7(11111)
        self.assertEqual(w, 'liczba')

    def test_f7_liczba_ze_znakiem(self):
        w = TDD.f7(-11111)
        self.assertEqual(w, 'liczba_ze_znakiem')

    def test_f7_zdanie(self):
        w=TDD.f7("Ala ma kota.")
        self.assertEqual(w, 'zdanie')

    def test_f7_tag(self):
        w=TDD.f7("<taaag>")
        self.assertEqual(w, 'tag poczatkowy')
