# -*- coding: utf-8 -*-

from pybind11_tests import type_caster_bare_interface as m


def test_cast():
    assert m.rtrn_valu() == "cast_rref"
    assert m.rtrn_rref() == "cast_rref"
    assert m.rtrn_cref() == "cast_cref"
    assert m.rtrn_mref() == "cast_mref"
    assert m.rtrn_cptr() == "cast_cptr"
    assert m.rtrn_mptr() == "cast_mptr"


def test_load():
    assert m.pass_valu(None) == "load_valu"
    assert m.pass_rref(None) == "load_rref"
    assert m.pass_cref(None) == "load_cref"
    assert m.pass_mref(None) == "load_mref"
    assert m.pass_cptr(None) == "load_cptr"
    assert m.pass_mptr(None) == "load_mptr"


def test_cast_shared_ptr():
    assert m.rtrn_shmp() == "cast_shmp"
    assert m.rtrn_shcp() == "cast_shcp"


def test_load_shared_ptr():
    assert m.pass_shmp(None) == "load_shmp"
    assert m.pass_shcp(None) == "load_shcp"


def test_cast_unique_ptr():
    assert m.rtrn_uqmp() == "cast_uqmp"
    assert m.rtrn_uqcp() == "cast_uqcp"


def test_load_unique_ptr():
    assert m.pass_uqmp(None) == "load_uqmp"
    assert m.pass_uqcp(None) == "load_uqcp"