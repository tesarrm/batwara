# Copyright (c) 2024, Build With Hussain and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record depdendencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestExpense(UnitTestCase):
	"""
	Unit tests for Expense.
	Use this class for testing individual functions and methods.
	"""

	def test_equal_split_calculation(self):
		frappe.get_doc({"doctype": "User", "email": "friend1@email.com", "first_name": "John"}).insert(
			ignore_if_duplicate=True
		)

		frappe.get_doc({"doctype": "User", "email": "friend2@email.com", "first_name": "Jenny"}).insert(
			ignore_if_duplicate=True
		)

		test_expense = frappe.get_doc(
			{
				"doctype": "Expense",
				"description": "test expense",
				"paid_by": "friend1@email.com",
				"amount": 200,
				"splits": [{"user": "friend1@email.com"}, {"user": "friend2@email.com"}],
			}
		).insert()

		self.assertEqual(test_expense.splits[0].amount, 100)
		self.assertEqual(test_expense.splits[1].amount, 100)


class IntegrationTestExpense(IntegrationTestCase):
	"""
	Integration tests for Expense.
	Use this class for testing interactions between multiple components.
	"""

	pass
