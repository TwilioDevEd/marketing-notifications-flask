def test():
    """Run the unit tests."""
    import sys, unittest
    tests = unittest.TestLoader().discover('.', pattern="*_tests.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)

    if not result.wasSuccessful():
        sys.exit(1)



if __name__ == "__main__":
    test()
