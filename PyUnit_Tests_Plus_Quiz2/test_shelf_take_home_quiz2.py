"""CS330 Spring 2019: Quiz 2 (take home)."""

import unittest
import shelf
import book

# Steps to consider when writing any unit test:
# 1) Create an instance of the object whose behavior you want to test.
# 2) Ensure that the instance is initialized appropriately to exhibit the behavior need to meet the test objective.
# 3) Use the TestCase methods (self.assertXXXXX()) to show the test objective is met.
# 4) Verify object state before and after (where needed) to show that test actions affect the object's state.
# 5) Run your test class the same way you'd run any Python program.

# PyUnit Docs: https://docs.python.org/3/library/unittest.html


class TestShelf(unittest.TestCase):
    """Tests Shelf behavior."""

    def setUp(self):
        """Use or delete this method."""
        book1 = book.Book("Catcher in the Rye", ("J","D","Salinger"))
        book1.SetCoverType(book.CoverType.HARDCOVER)
        book1.SetPages(277)
        return(book1)               
        pass

    # Write unit tests for these Shelf class methods and behaviors:

    def test_AddBook(self):
        """Tests that a book is successfully added to a shelf."""
        book1 = self.setUp()
        shelf1 = shelf.Shelf()
        shelf1.AddBook(book1)
        self.assertEqual(shelf1.GetBookCount(), 1)
        pass

    def test_RemoveBook(self):
        """Tests that a book is successfully removed from a shelf."""
        book1 = self.setUp()
        shelf1 = shelf.Shelf()
        shelf1.AddBook(book1)
        shelf1.RemoveBook("Catcher in the Rye")
        self.assertEqual(shelf1.GetBookCount(), 0)
        pass

    def test_AddBook_reduces_shelf_capacity(self):
        """Tests that shelf capacity is reduced after adding a book."""
        book1 = self.setUp()
        shelf1 = shelf.Shelf()
        shelf1.AddBook(book1)
        self.assertEqual(shelf1.GetAvailableCapacity(), 72 - book1.GetThickness())
        pass

    def test_RemoveBook_increases_shelf_capacity(self):
        """Tests that shelf capacity is increased after removing a book."""
        book1 = self.setUp()
        shelf1 = shelf.Shelf()
        shelf1.AddBook(book1)
        shelf1.RemoveBook("Catcher in the Rye")
        self.assertEqual(shelf1.GetAvailableCapacity(), shelf1.GetInitialCapacity())
        pass

        # Extra Credit
    def test_shelf_space_exhausted(self):
        """Tests that an exception is raised when adding a book to a shelf with insufficient space."""
        book1 = self.setUp()
        shelf1 = shelf.Shelf()
        shelf1._ReduceCapacity(shelf1.GetInitialCapacity())
        with self.assertRaises(RuntimeError):
            shelf1.AddBook(book1)
        
        pass



if __name__ == '__main__':
    unittest.main()
