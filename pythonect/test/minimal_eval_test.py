#!/usr/bin/python

import unittest
import os
import sys

# Add `internal` directory (i.e. ../) to sys.path

sys.path.append(os.path.abspath('../'))


# Local imports

import eval


class TestPythonect(unittest.TestCase):

    def setUp(self):

        self.input = None

    def test_literal_hex(self):

        self.assertEqual(eval.eval('0x01', {}, {}), 1)

    def test_literal_bin(self):

        self.assertEqual(eval.eval('0b1', {}, {}), 1)

    def test_literal_float(self):

        self.assertEqual(eval.eval('1.0', {}, {}), 1)

    def test_literal_int(self):

        self.assertEqual(eval.eval('1', {}, {}), 1)

    def test_python_stmt_import(self):

        self.assertEqual(eval.eval('import math', {}, {}), self.input)

    def test_python_stmt_assignment(self):

        self.assertEqual(eval.eval('x = 1', {}, {}), self.input)

    def test_python_expr_int(self):

        self.assertEqual(eval.eval('1 + 1', {}, {}), 2)

    def test_python_expr_str(self):

        self.assertEqual(eval.eval('"Hello World"', {}, {}), "Hello World")

    def test_python_expr_list(self):

        self.assertEqual(eval.eval('[[1, 2, 3]]', {}, {}), [1, 2, 3])

    def test_python_true_expr_literal_eq_literal(self):

        self.assertEqual(eval.eval('1 == 1', {}, {}), self.input)

    def test_python_false_expr_literal_neq_literal(self):

        self.assertEqual(eval.eval('1 == 0', {}, {}), False)

    def test_python_true_expr_underscore_eq_underscore(self):

        self.assertEqual(eval.eval('_ == _', {}, {}), self.input)

    def test_python_false_expr_underscore_neq_repr_underscore(self):

        self.assertEqual(eval.eval('_ == repr(_)', {}, {}), False)

    def test_literal_int_async_none(self):

        self.assertEqual(eval.eval('1 -> None', {}, {}), 1)

    def test_literal_int_sync_none(self):

        self.assertEqual(eval.eval('1 | None', {}, {}), 1)

    def test_literal_int_async_dict(self):

        self.assertEqual(eval.eval('1 -> {1: "One", 2: "Two"}', {}, {}), "One")

    def test_literal_int_sync_dict(self):

        self.assertEqual(eval.eval('1 | {1: "One", 2: "Two"}', {}, {}), "One")

    def test_literal_str_async_autoload(self):

        self.assertEqual(eval.eval('"Hello world" -> string.split', {}, {}), ["Hello", "world"])

    def test_literal_str_sync_autoload(self):

        self.assertItemsEqual(eval.eval('"Hello world" | string.split', {}, {}), ["Hello", "world"])

    def test_literal_int_async_literal_int(self):

        self.assertEqual(eval.eval('1 -> 1', {}, {}), 1)

    def test_literal_int_sync_literal_int(self):

        self.assertEqual(eval.eval('1 | 1', {}, {}), 1)

    def test_literal_int_async_literal_array_int_float(self):

        self.assertItemsEqual(eval.eval('1 -> [int,float]', {}, {}), [1, 1.0])

    def test_literal_int_sync_literal_array_int_float(self):

        self.assertEqual(eval.eval('1 | [int,float]', {}, {}), [1, 1.0])

    def test_python_stmt_assignment_async_literal_int(self):

        self.assertEqual(eval.eval('[x = 0] -> 1', {}, {}), 1)

    def test_python_stmt_assignment_sync_literal_int(self):

        self.assertEqual(eval.eval('[x = 0] | 1', {}, {}), 1)

    def test_python_stmt_assignment_sync_variable(self):

        self.assertEqual(eval.eval('[x = 0] | x', {}, {}), 0)

    def test_python_stmt_assignment_async_variable(self):

        self.assertEqual(eval.eval('[x = 0] -> x', {}, {}), 0)

    def test_literal_array_int_int_sync_none(self):

        self.assertEqual(eval.eval('[1, 2] | None', {}, {}), [1, 2])

    def test_literal_array_int_int_async_none(self):

        self.assertItemsEqual(eval.eval('[1, 2] -> None', {}, {}), [1, 2])

    def test_literal_array_int_int_sync_dict(self):

        self.assertEqual(eval.eval('[1, 2] | {1: "One", 2: "Two"}', {}, {}), ["One", "Two"])

    def test_literal_array_int_int_async_dict(self):

        self.assertItemsEqual(eval.eval('[1, 2] -> {1: "One", 2: "Two"}', {}, {}), ["One", "Two"])

    def test_literal_array_int_str_async_none(self):

        self.assertItemsEqual(eval.eval('[1, "Hello"] -> None', {}, {}), [1, "Hello"])

    def test_literal_array_int_str_sync_none(self):

        self.assertEqual(eval.eval('[1, "Hello"] | None', {}, {}), [1, "Hello"])

    def test_literal_array_int_str_async_int(self):

        self.assertItemsEqual(eval.eval('[1, "Hello"] -> 1', {}, {}), [1, 1])

    def test_literal_array_int_str_sync_int(self):

        self.assertEqual(eval.eval('[1, "Hello"] | 1', {}, {}), [1, 1])

    def test_literal_array_int_int_sync_literal_int(self):

        self.assertEqual(eval.eval('[1, 2] | 1', {}, {}), [1, 1])

    def test_literal_array_int_int_async_literal_int(self):

        self.assertEqual(eval.eval('[1, 2] -> 1', {}, {}), [1, 1])

    def test_literal_array_int_int_sync_literal_array_int_int(self):

        self.assertEqual(eval.eval('[1, 2] | [3, 4]', {}, {}), [3, 4, 3, 4])

    def test_literal_array_int_int_async_literal_array_int_int(self):

        self.assertItemsEqual(eval.eval('[1, 2] -> [3, 4]', {}, {}), [3, 3, 4, 4])

    def test_literal_int_async_stmt_single_return_value_function_async_single_return_value_function(self):

        self.assertEqual(eval.eval('1 -> def foobar(x): return x+1 -> foobar', {}, {}), 2)

    def test_literal_int_async_stmt_single_return_value_function_sync_single_return_value_function(self):

        self.assertEqual(eval.eval('1 -> def foobar(x): return x+1 | foobar', {}, {}), 2)

    def test_literal_int_sync_stmt_single_return_value_function_async_single_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): return x+1 -> foobar', {}, {}), 2)

    def test_literal_int_sync_stmt_single_return_value_function_sync_single_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): return x+1 | foobar', {}, {}), 2)

    def test_literal_int_async_stmt_multiple_return_value_function_async_multiple_return_value_function(self):

        self.assertItemsEqual(eval.eval('1 -> def foobar(x): return [x,x+1] -> foobar', {}, {}), [1, 2])

    def test_literal_int_async_stmt_multiple_return_value_function_sync_multiple_return_value_function(self):

        self.assertEqual(eval.eval('1 -> def foobar(x): return [x,x+1] | foobar', {}, {}), [1, 2])

    def test_literal_int_sync_stmt_multiple_return_value_function_async_multiple_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): return [x,x+1] -> foobar', {}, {}), [1, 2])

    def test_literal_int_sync_stmt_multiple_return_value_function_sync_multiple_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): return [x,x+1] | foobar', {}, {}), [1, 2])

    def test_literal_int_async_stmt_generator_return_value_function_async_generator_return_value_function(self):

        self.assertItemsEqual(eval.eval('1 -> def foobar(x): yield x; yield x+1 -> foobar', {}, {}), [1, 2])

    def test_literal_int_async_stmt_generator_return_value_function_sync_generator_return_value_function(self):

        self.assertEqual(eval.eval('1 -> def foobar(x): yield x; yield x+1 | foobar', {}, {}), [1, 2])

    def test_literal_int_sync_stmt_generator_return_value_function_async_generator_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): yield x; yield x+1 -> foobar', {}, {}), [1, 2])

    def test_literal_int_sync_stmt_generator_return_value_function_sync_generator_return_value_function(self):

        self.assertEqual(eval.eval('1 | def foobar(x): yield x; yield x+1 | foobar', {}, {}), [1, 2])

    def test_singlethread_program_async(self):

        self.assertEqual(eval.eval('import threading -> x = threading.current_thread().name -> y = threading.current_thread().name -> x == y', {}, {}), None)

    def test_singlethread_program_sync(self):

        self.assertEqual(eval.eval('import threading | x = threading.current_thread().name | y = threading.current_thread().name | x == y', {}, {}), None)

    def test_multithread_program_async(self):

        r_array = eval.eval('import threading -> [threading.current_thread().name, threading.current_thread().name]', {}, {})

        self.assertEqual(r_array[0] != r_array[1], True)

    def test_multithread_program_sync(self):

        r_array = eval.eval('import threading | [threading.current_thread().name, threading.current_thread().name]', {}, {})

        self.assertEqual(r_array[0] != r_array[1], True)

    def test_multiprocess_program_async(self):

        self.assertEqual(eval.eval('import multiprocessing -> start_pid = multiprocessing.current_process().pid -> start_pid -> str & -> current_pid = multiprocessing.current_process().pid -> 1 -> current_pid != start_pid', {}, {}), 1)

    def test_multiprocess_program_sync(self):

        self.assertEqual(eval.eval('import multiprocessing | start_pid = multiprocessing.current_process().pid | start_pid | str & | current_pid = multiprocessing.current_process().pid | 1 | current_pid != start_pid', {}, {}), 1)

    def test_pseudo_none_const_as_url(self):

        self.assertEqual(eval.eval('def foobar(x): return x+1 -> 1 -> foobar@None', {}, {}), 2)

    def test_pseudo_none_str_as_url(self):

        self.assertEqual(eval.eval('def foobar(x): return x+1 -> 1 -> foobar@"None"', {}, {}), 2)

    def test_pseudo_none_value_fcn_return_value_as_url(self):

        self.assertEqual(eval.eval('def ret_none(): return None -> def foobar(x): return x+1 -> 1 -> foobar@ret_none()', {}, {}), 2)

    def test_pseudo_none_str_fcn_return_value_as_url(self):

        self.assertEqual(eval.eval('def ret_none(): return "None" -> def foobar(x): return x+1 -> 1 -> foobar@ret_none()', {}, {}), 2)

    # Bug #11

    def test_autloader_within_array(self):

        self.assertItemsEqual(eval.eval('"Hello world" | [string.split]', {}, {}), ["Hello", "world"])

    # Bug #14

    def test_print_like_statement(self):

        self.assertItemsEqual(eval.eval('range(1,10) -> print("Thread A")', {}, {}), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_multiple_stateful_x_eq_5_statement(self):

        locals_ = {}

        globals_ = {}

        eval.eval('xrange(1, 10) -> x = _', globals_, locals_)

        self.assertEqual('x' not in locals_ and 'x' not in globals_, True)

        # i.e.

        # >>> xrange(x, 10) -> x = _
        # >>> x
        # NameError: name 'x' is not defined

    def test_stateful_x_eq_5_statement(self):

        locals_ = {}

        globals_ = {}

        eval.eval('x = 5', globals_, locals_)

        self.assertEqual(eval.eval('1 -> [x == 5]', globals_, locals_), 1)

        # i.e.

        # >>> x = 5
        # >>> 1 -> [x == 5]
        # 1

    # Bug #16

    def test_typeerror_exception_not_due_to_eval(self):

        self.assertEqual(eval.eval('1 -> socket.socket(socket.AF_INET, socket.SOCK_STREAM) -> _.connect("A","B")', {}, {}), False)

    # Bug #21

    def test_list_with_str_with_comma(self):

        self.assertEqual(eval.eval('["Hello, world"]', {}, {}), 'Hello, world')
